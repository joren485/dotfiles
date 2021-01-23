#!/usr/bin/env bash

pacmd set-default-sink "alsa_output.pci-0000_00_1f.3.analog-stereo"

pkill -f "polybar --reload --quiet default"
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --output DVI-I-2-2 --off --output DVI-I-1-1 --off
