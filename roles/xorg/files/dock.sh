#!/usr/bin/env bash

pkill -f "polybar --reload --quiet default"

xrandr --output eDP1 --primary --mode 1920x1080 --pos 0x0 --output DVI-I-2-2 --mode 1920x1080 --pos 1920x0 --output DVI-I-1-1 --mode 1920x1080 --pos 3840x0

setxkbmap -layout us -variant intl

MONITOR="DVI-I-1-1" polybar --reload --quiet default &
MONITOR="DVI-I-2-2" polybar --reload --quiet default &
