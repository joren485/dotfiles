#!/usr/bin/env bash

pkill -f "polybar --reload --quiet default"

for screen in DVI-I-1-1 DVI-I-2-2; do
    if ! xrandr --query | grep --quiet "${screen} connected"; then
        echo "${screen} not connected";
        exit 1;
    fi
done;

xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --output DVI-I-2-2 --mode 1920x1080 --pos 1920x0 --output DVI-I-1-1 --mode 1920x1080 --pos 3840x0
MONITOR="DVI-I-1-1" polybar --reload --quiet default &
MONITOR="DVI-I-2-2" polybar --reload --quiet default &

setxkbmap -model pc104 -layout us -variant altgr-intl

pacmd set-default-sink "alsa_output.usb-DisplayLink_ThinkPad_Hybrid_USB-C_with_USB-A_Dock_10660913-02.analog-stereo"
