#!/usr/bin/env bash

pkill -f "polybar --reload --quiet default"
xrandr --output eDP1 --primary --mode 1920x1080 --pos 0x0 --output DVI-I-2-2 --off --output DVI-I-1-1 --off
