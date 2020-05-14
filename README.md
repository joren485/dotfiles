# dotfiles [![Build Status](https://travis-ci.org/joren485/dotfiles.svg?branch=master)](https://travis-ci.org/joren485/dotfiles)
The dotfiles for my setup

# The network
This is the layout of my home network that this config is written for.

## Static, wired hosts
Subnet: `192.168.1.0/27` (`192.168.1.1` - `192.168.1.31`)

### `banaan` (Gateway)
* Operating system: OpenWRT
* IPv4: `192.168.1.1`
* IPv6: `fc00:dead:beef::1` 
* Runs DHCP for `192.168.1.128/25` (`192.168.1.129` - `192.168.1.254`)

### `Peen` (Hypervisor)
* Operating sytem: Proxmox
* IPv4: `192.168.1.2`
* IPv6: `fc00:dead:beef::2`

## Static, wireless hosts
Subnet: `192.168.1.32/27` (`192.168.1.33` - `192.168.1.62`)

### `druif` (laptop)
* Operating System: Arch Linux
* IPv4: `192.168.1.33`
* IPv6: `fc00:dead:beef::33`

### Phone
* IPv4: `192.168.1.34`

### Chromecast
* IPv4: `192.168.1.40`

## Virtual hosts
These hosts run on the Proxmox server.

### `aubergine` (Plex)
* Operating system: Arch Linux
* IPv4: `192.168.1.65`
* IPv6: `fc00:dead:beef::65`
* The Plex media directories are mounted from `courgette` using a NFS share.

### `courgette` (qBittorrent)
* Operating system: Arch Linux
* IPv4: `192.168.1.66`
* IPv6: `fc00:dead:beef::66`
* Runs OpenVPN with a Private Internet Access connection.
* Automatically sets up port forwarding for the VPN.
* Runs NFS server to share downloads.
