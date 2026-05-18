# Proxmox VE Best Practices Guide

## Table of Contents
1. [Security](#security)
2. [Network Configuration](#network-configuration)
3. [Storage Management](#storage-management)
4. [Backup & Disaster Recovery](#backup--disaster-recovery)
5. [Performance Optimization](#performance-optimization)
6. [High Availability & Clustering](#high-availability--clustering)
7. [Resource Management](#resource-management)
8. [Monitoring & Logging](#monitoring--logging)
9. [Maintenance & Updates](#maintenance--updates)
10. [Compliance & Auditing](#compliance--auditing)

---

## Security

### Access Control
- **Restrict Root SSH Access**: Disable direct root login via SSH
  ```
  PermitRootLogin no
  ```
- **Use SSH Keys**: Implement key-based authentication instead of passwords
- **Change Default Ports**: Move SSH to non-standard port (e.g., 2222)
- **Implement Firewall**: Use `iptables` or `ufw` for host-level firewall rules
- **Two-Factor Authentication (2FA)**: Enable for web UI access when possible

### User & Permission Management
- **Principle of Least Privilege**: Grant minimum required permissions
- **Role-Based Access Control (RBAC)**: Use Proxmox roles (Administrator, PVEAdmin, PVEOperator, etc.)
- **API Token Management**: 
  - Generate tokens for automation instead of using user credentials
  - Regularly rotate tokens
  - Use expiration dates
- **Audit User Activities**: Monitor login attempts and administrative actions

### Web UI & API Security
- **HTTPS Only**: Ensure self-signed certificates are replaced with valid ones
- **Strong Passwords**: Enforce complex password policies
  - Minimum 12 characters
  - Mix of uppercase, lowercase, numbers, and special characters
- **Session Management**: 
  - Set appropriate session timeouts (15-30 minutes)
  - Implement logout on idle
- **API Rate Limiting**: Implement to prevent brute force attacks

### Certificate Management
- **Replace Default Certificates**: Generate and install valid SSL/TLS certificates
- **Certificate Monitoring**: Set up alerts for expiring certificates
- **Certificate Renewal**: Automate renewal process (use Let's Encrypt or equivalent)

### Firewall Configuration
- **Host Firewall**: 
  ```bash
  ufw default deny incoming
  ufw default allow outgoing
  ufw allow 22/tcp
  ufw allow 8006/tcp
  ufw allow 3412/tcp
  ufw allow 5900:5999/tcp
  ```
- **VM Firewall Rules**: Enable and configure per-VM firewall policies
- **Network Segmentation**: Isolate management network from VM traffic

### Vulnerability Management
- **Regular Security Updates**: Apply patches promptly
- **Security Scanning**: Use tools like Lynis or OpenVAS for vulnerability assessment
- **Monitor Security Advisories**: Subscribe to Proxmox security mailing lists

---

## Network Configuration

### Network Architecture
- **Separate Management Network**: Use dedicated NIC for cluster and management traffic
- **Live Migration Network**: Dedicated network for VM migrations (separate from management)
- **Storage Network**: Isolated network for storage traffic (if using iSCSI/NFS)
- **VM Network**: Separate bridges for different VM network segments

### Bridge Configuration
```bash
# Example /etc/network/interfaces configuration
auto lo
iface lo inet loopback

auto eno1
iface eno1 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 8.8.4.4

auto vmbr0
iface vmbr0 inet static
    address 192.168.100.1
    netmask 255.255.255.0
    bridge-ports eno2
    bridge-stp off
    bridge-fd 0

# Storage network
auto eno3
iface eno3 inet static
    address 192.168.200.10
    netmask 255.255.255.0
```

### Bonding & Redundancy
- **NIC Bonding**: Use LACP (802.3ad) for redundancy
  ```bash
  auto bond0
  iface bond0 inet static
      slaves eno1 eno2
      bond-mode active-backup
      bond-miimon 100
      address 192.168.1.10
      netmask 255.255.255.0
  ```
- **Multiple Uplinks**: Configure multiple network paths for failover

### VLAN Configuration
- **Management VLAN**: Isolate cluster communication
- **VM VLANs**: Segregate tenant/service networks
- **Storage VLAN**: Isolate storage traffic
- **Guest Isolation**: Use tags for VM network isolation

### DNS & DHCP
- **Primary & Secondary DNS**: Configure redundant DNS servers
- **Local DNS Records**: Maintain entries for cluster nodes
- **DHCP Configuration**: Use centralized DHCP for consistent IP management

### MTU Optimization
- **Jumbo Frames**: Set MTU to 9000 for storage networks (if supported)
  ```bash
  ip link set dev eno3 mtu 9000
  ```
- **Network Testing**: Use `ping -M do -s 8972` to test MTU

---

## Storage Management

### Storage Types & Selection
- **Local Storage**: Good for single-node setups, limited for HA
- **Shared Storage (Recommended for HA)**:
  - **NFS**: Simple, no hardware RAID required
  - **iSCSI**: Better performance, requires hardware
  - **Ceph**: Distributed, self-healing, high availability
  - **GlusterFS**: Distributed, scalable

### Storage Configuration Best Practices
- **Dedicated Storage Network**: Use separate network for storage traffic
- **Storage Redundancy**: 
  - RAID 6 or RAID 10 for traditional storage
  - Replication for Ceph
- **Performance Testing**: Benchmark storage with `fio` or `iozone`

### Local Storage
```bash
# Check available storage
df -h

# Monitor I/O performance
iostat -x 1

# Verify storage pool health
pvs  # Physical Volumes
vgs  # Volume Groups
lvs  # Logical Volumes
```

### NFS Storage
```bash
# Mount NFS storage
mount -t nfs 192.168.200.50:/export/proxmox /mnt/pve/nfs_storage

# In /etc/pve/storage.cfg
dir: nfs_storage
    path /mnt/pve/nfs_storage
    content images,rootdir
    disable 0
    maxfiles 0
```

### iSCSI Storage
```bash
# Discover iSCSI targets
iscsiadm -m discovery -t st -p 192.168.200.100

# Connect to target
iscsiadm -m node -T iqn.target.name -p 192.168.200.100 -l
```

### Ceph Storage
- **Cluster Planning**: Minimum 3 nodes for production
- **OSD Monitoring**: Use `ceph osd tree` and `ceph status`
- **Replication Factor**: Set to 3 for production (3 copies minimum)
- **Placement Groups**: Configure appropriately for cluster size

### Storage Quotas & Monitoring
- **Set Disk Quotas**: Limit storage per user/project
- **Monitor Disk Usage**: Set up alerts at 70%, 80%, 90% capacity
- **Thin Provisioning**: Use wisely to avoid over-allocation
- **Regular Cleanup**: Remove unused snapshots and backups

---

## Backup & Disaster Recovery

### Backup Strategy (3-2-1 Rule)
- **3 Copies**: Data, backup 1, backup 2
- **2 Different Media**: Local storage + offsite
- **1 Offsite**: Remote location for disaster recovery

### Backup Methods

#### Proxmox Native Backups
```bash
# Command-line backup
vzdump 100 --stdout | gzip > backup_vm100_$(date +%Y%m%d).tar.gz

# Scheduled backups
# Configure in Proxmox UI: Datacenter > Backup
# Or use Proxmox Backup Server (PBS)
```

#### Backup Configuration
- **Backup Frequency**: Daily for critical VMs, weekly for others
- **Retention Policy**:
  - Daily: Keep 7 days
  - Weekly: Keep 4 weeks
  - Monthly: Keep 12 months
- **Backup Window**: Schedule during low-usage periods

### Proxmox Backup Server (PBS)
- **Dedicated Backup Appliance**: Recommended for production
- **Deduplication**: Reduces storage overhead
- **Encryption**: End-to-end encryption support
- **Verification**: Regular integrity checks

### Backup Testing & Verification
```bash
# Test backup integrity
tar -tzf backup_vm100.tar.gz > /dev/null

# Verify backup restoration periodically
# Test restore to temporary VM monthly
```

### Disaster Recovery Plan
- **RTO (Recovery Time Objective)**: Target recovery time (e.g., 4 hours)
- **RPO (Recovery Point Objective)**: Acceptable data loss (e.g., 1 hour)
- **Documentation**: Maintain updated recovery procedures
- **Regular Drills**: Test recovery procedures quarterly

### Off-site Backup
- **Remote Location**: Geographically separate backup location
- **Network**: Secure, encrypted connection for off-site backups
- **Cloud Backup**: Consider cloud storage for long-term retention
- **Encryption**: Always encrypt before transmitting off-site

---

## Performance Optimization

### CPU Optimization
- **CPU Pinning**: Pin VM CPUs to host CPUs for better performance
  ```
  # In VM config: /etc/pve/qemu-server/100.conf
  cpuunits: 1024
  cores: 4
  sockets: 1
  ```
- **NUMA Awareness**: On multi-socket systems, enable NUMA
- **CPU Type**: Set appropriate CPU model for VM
  - `host`: Best performance, reduced migration capability
  - `kvm64`: Standard, good compatibility

### Memory Optimization
- **Memory Ballooning**: Enable for flexible memory allocation
- **Page Sharing**: Enable KSM (Kernel Samepage Merging) for identical page consolidation
- **Memory Limits**: Set reasonable limits per VM
- **Swap Configuration**: Monitor and limit swap usage

### Disk I/O Optimization
- **Cache Mode**: Configure appropriate cache settings
  ```
  # Write-through cache (safest)
  # Write-back cache (faster, riskier)
  # None (direct I/O, depends on guest OS)
  ```
- **I/O Throttling**: Limit noisy neighbors
  ```
  # In VM config
  iothread: 1
  scsi0: local-lvm:vm-100-disk-0,iothread=1,cache=writethrough
  ```

### Network Optimization
- **VirtIO Network Driver**: Use VirtIO for better performance
- **Multiple Queues**: Enable multi-queue for better throughput
- **Network Bridges**: Use native bridges, avoid adding unnecessary VLANs

### VM Configuration Example
```
# Balanced performance config
agent: 1
cores: 4
cpu: host
memory: 8192
net0: virtio=XX:XX:XX:XX:XX:XX,bridge=vmbr0
scsi0: local-lvm:vm-100-disk-0,cache=writethrough,iothread=1
sockets: 1
```

### Monitoring Performance
```bash
# CPU usage
top -p $(pgrep -f 'qemu-system')

# Memory usage
free -h
slabtop

# Disk performance
iostat -x 5

# Network performance
iftop
nethogs
```

---

## High Availability & Clustering

### Cluster Planning
- **Minimum 3 Nodes**: Odd number for quorum (3, 5, 7...)
- **Cluster Network**: Dedicated, low-latency network required
- **Hardware**: Similar specifications for better load balancing
- **Time Synchronization**: NTP on all nodes (within 5ms)

### Cluster Setup
```bash
# Node 1 - Create cluster
pvecm create mycluster

# Node 2 & 3 - Join cluster
pvecm add <node1-ip> -nodeid 2
pvecm add <node1-ip> -nodeid 3

# Verify cluster status
pvecm status
```

### Quorum & Corosync
- **Quorum**: Majority of nodes must be online
- **Corosync**: Handles cluster communication
- **Network Loss**: Design for split-brain prevention
- **Watchdog**: Configure hardware watchdog for failover

### High Availability (HA)
- **Enable HA**: Configure HA group for critical VMs
  ```bash
  # Command-line
  ha-manager add vm:100,enabled=1
  ```
- **HA Manager**: Automatic VM restart on node failure
- **Migration Policies**: Define behavior on node failure
- **Fencing**: Prevent split-brain scenarios

### Load Balancing
- **Distributed VMs**: Spread VMs across cluster nodes
- **Resource Limits**: Configure per-node resource caps
- **Automatic Migration**: Use HA for automatic failover

### Cluster Monitoring
```bash
# Cluster status
pvecm status

# Node status
pvecm nodes

# Logs
journalctl -xe -u pve-ha-crm
```

---

## Resource Management

### CPU Management
- **CPU Shares**: Allocate CPU resources proportionally
  - Default: 1024 shares per vCPU
  - Adjust for priority VMs
- **CPU Limits**: Set hard limits to prevent resource starvation
- **vCPU Allocation**: Don't over-allocate beyond physical cores (2:1 max)

### Memory Management
- **Memory Overcommit**: Limit to 1.5:1 ratio
- **Balloon Driver**: Enable for dynamic memory adjustment
- **Swap**: Configure appropriately for burst capacity
- **Memory Alerts**: Alert at 80% utilization

### Storage Resource Allocation
```bash
# Set quota per storage
# Edit /etc/pve/storage.cfg
# Add maxfiles or other limits

# Monitor quota usage
df -h /mnt/pve/storage_name
```

### Network QoS (Quality of Service)
- **Rate Limiting**: Limit VM network bandwidth
  ```
  # Example: 100Mbps limit
  net0: model=virtio,rate=100
  ```
- **Traffic Shaping**: Prioritize critical traffic
- **Bandwidth Management**: Prevent one VM affecting others

### VM Resource Profiles
```
# High-priority VM
cores: 8, memory: 16GB, disk: 200GB

# Standard VM
cores: 4, memory: 8GB, disk: 100GB

# Low-priority VM
cores: 2, memory: 4GB, disk: 50GB
```

---

## Monitoring & Logging

### Monitoring Infrastructure
- **Proxmox Built-in**: Basic monitoring in web UI
- **Prometheus + Grafana**: Advanced monitoring stack
- **Zabbix**: Enterprise monitoring solution
- **Check_MK/Nagios**: Alternative monitoring platforms

### Key Metrics to Monitor
- **Host Metrics**:
  - CPU usage, temperature
  - Memory usage, swap
  - Disk I/O, space utilization
  - Network throughput, errors
- **VM Metrics**:
  - CPU and memory usage
  - Disk I/O and space
  - Network traffic
  - Uptime and status
- **Cluster Metrics**:
  - Node health and quorum
  - Cluster communication latency
  - Storage replication status (if applicable)

### Prometheus Integration
```yaml
# /etc/prometheus/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'proxmox'
    static_configs:
      - targets: ['192.168.1.10:9100']  # Node exporter
```

### Alerting Rules
```yaml
# Critical alerts
- CPU usage > 90%
- Memory usage > 85%
- Disk usage > 90%
- Node down or not responsive
- VM crashes or unexpected shutdown
- Cluster member offline
```

### Logging Strategy
- **Centralized Logging**: Use ELK Stack or Splunk
- **Log Retention**: Keep logs for minimum 90 days
- **Log Levels**: Appropriate verbosity (ERROR, WARN, INFO)
- **Audit Logging**: Track all administrative actions

### Log Locations
```bash
/var/log/syslog          # System log
/var/log/pve/           # Proxmox logs
/var/log/auth.log       # Authentication log
/var/log/daemon.log     # Daemon log
/var/log/qemu-server/   # VM logs
```

### Log Monitoring Commands
```bash
# Real-time log viewing
tail -f /var/log/syslog

# Search for errors
grep -i error /var/log/syslog

# Monitor specific service
journalctl -u pvestatd -f

# Check VM logs
cat /var/log/qemu-server/100.log
```

---

## Maintenance & Updates

### Update Management
- **Update Schedule**: Plan regular maintenance windows
- **Patch Testing**: Test updates in non-production first
- **Update Procedure**:
  ```bash
  apt update
  apt dist-upgrade
  ```
- **Kernel Updates**: Consider impact on running VMs

### Pre-Update Checklist
- [ ] Backup all VMs
- [ ] Document current state
- [ ] Notify users of maintenance window
- [ ] Check disk space (at least 2GB free)
- [ ] Verify cluster health

### Node Maintenance
```bash
# Prepare node for maintenance
pvecm add-nodes-leave
ha-manager disable

# Evacuate VMs
pvecm remove-node <nodename>

# Or migrate running VMs
qm migrate <vmid> <target-node>

# Perform maintenance
reboot

# Rejoin cluster
pvecm add <other-node-ip>
```

### Post-Update Validation
```bash
# Check system status
pveversion -v

# Verify cluster health
pvecm status

# Check node connectivity
ping <cluster-nodes>

# Verify HA status
ha-manager status

# Monitor for errors
journalctl -xe
```

### Scheduled Maintenance Tasks
- **Weekly**: Check cluster health, verify backups
- **Monthly**: Review logs, update packages, test restoration
- **Quarterly**: Full backup verification, security scan, capacity planning
- **Annually**: Firmware updates, hardware inspection, disaster recovery drill

---

## Compliance & Auditing

### Audit Logging
- **Enable Audit Logs**: All administrative actions logged
- **Access Logging**: Track login attempts, both successful and failed
- **Change Tracking**: Document all configuration changes
- **Log Protection**: Ensure logs cannot be tampered with

### Compliance Requirements
- **Data Protection**: GDPR, HIPAA, PCI-DSS compliance
- **Encryption**: At-rest and in-transit encryption
- **Access Control**: Role-based access, multi-factor authentication
- **Incident Response**: Documented procedures

### User Activity Audit
```bash
# Check user login history
lastlog

# Failed login attempts
grep 'Failed password' /var/log/auth.log

# Sudo command history
grep 'sudo' /var/log/auth.log
```

### Configuration Audit
```bash
# Configuration version control
git init /etc/pve
git add .
git commit -m "Initial config"

# Regularly commit changes
git add -A
git commit -m "Configuration update"
```

### Security Assessment
- **Regular Audits**: Quarterly security reviews
- **Penetration Testing**: Annual third-party testing
- **Vulnerability Scanning**: Monthly automated scans
- **Compliance Validation**: Verify adherence to policies

### Incident Response
- **Incident Plan**: Documented procedures
- **Response Team**: Designated contacts
- **Investigation Process**: Evidence preservation, root cause analysis
- **Notification**: Timely notification of affected parties
- **Post-Incident Review**: Lessons learned documentation

### Retention Policies
- **VMs & Data**: Per business requirements (typically 1-3 years)
- **Logs**: Minimum 1 year, audit logs 3-7 years
- **Backups**: Daily (7 days), Weekly (4 weeks), Monthly (12 months)
- **Configuration**: Keep indefinitely with version control

---

## Additional Resources

### Documentation
- [Proxmox VE Official Documentation](https://pve.proxmox.com/wiki/Main_Page)
- [Proxmox Community Forum](https://forum.proxmox.com/)
- [Proxmox Backup Documentation](https://pbs.proxmox.com/)

### Useful Commands
```bash
# Get system info
pveversion -v
pvesyslog

# VM management
qm list
qm start <vmid>
qm stop <vmid>
qm status <vmid>

# Storage management
pvesm list
pvesm status

# Cluster management
pvecm status
pvecm nodes
ha-manager status

# Performance monitoring
top
vmstat 1
iostat -x 1
iftop
```

### Troubleshooting Commands
```bash
# Check service status
systemctl status pvestatd
systemctl status pvedaemon

# Check cluster synchronization
pvecm status
pvecm nodes

# Verify storage connectivity
showmount -e <storage-server>
iscsiadm -m session

# Check network connectivity
ping <target>
traceroute <target>
netstat -tupan
```

---

## Conclusion

Implementing these best practices ensures:
- ✅ Enhanced security posture
- ✅ Improved performance and reliability
- ✅ Simplified maintenance and troubleshooting
- ✅ Better disaster recovery capability
- ✅ Regulatory compliance
- ✅ Scalable infrastructure

Regular review and updates of these practices keep your Proxmox environment secure, efficient, and production-ready.

---

**Last Updated**: 2026-05-15  
**Version**: 1.0  
**Author**: Proxmox Best Practices Guide