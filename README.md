# dotfiles [![Build Status](https://travis-ci.org/joren485/dotfiles.svg?branch=master)](https://travis-ci.org/joren485/dotfiles)
The dotfiles for my setup.

# The network
This is the layout of my home network that this config is written for.

## Static, wired hosts
Subnet: `192.168.1.0/27` (`192.168.1.1` - `192.168.1.31`)

### `appel` (Edgerouter X)
* Operating system: EdgeOS
* IPv4: `192.168.1.1`
* Runs local DNS server
* Runs DHCP (from `192.168.1.128` to `192.168.1.200`)

### `peen` (Hypervisor)
* Operating system: Proxmox
* IPv4: `192.168.1.2`

#### Virtual hosts
These hosts run on the Proxmox server.
Subnet: `192.168.1.64/27` (`192.168.1.65` - `192.168.1.94`)

##### `aubergine` (Plex)
* Operating system: Arch Linux
* IPv4: `192.168.1.65`
* The Plex media directories are mounted from `courgette` using a NFS share.

##### `courgette` (qBittorrent)
* Operating system: Arch Linux
* IPv4: `192.168.1.66`
* Runs OpenVPN with a Private Internet Access connection.
* Automatically sets up port forwarding for the VPN.
* Runs NFS server to share downloads.

##### `pompoen` (Netdata, Unifi Controller)
* Operating system: Arch Linux
* IPv4: `192.168.1.67`
* Runs Netdata server
  * Runs a ping monitor 
* Runs Unifi Controller

### `banaan` (UniFi AP-AC-Lite)
* Operating system: OpenWrt/LEDE
* IPv4: `192.168.1.3` 
* Runs Wifi network with ESSID "Banaan"

## Static, wireless hosts
Subnet: `192.168.1.32/27` (`192.168.1.33` - `192.168.1.62`)

### `druif` (laptop)
* Operating System: Arch Linux
* IPv4: `192.168.1.33`
