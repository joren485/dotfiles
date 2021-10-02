#!/usr/bin/env bash
# Ansible managed

set -e

HEADSET_MAC_ADDRESS="F8:5C:7D:31:8E:3F"

if bluetoothctl show | grep --quiet "Powered: no"; then
    echo "Powering on bluetooth";
    if bluetoothctl power on > /dev/null; then
        echo "Successfully powered on";
    else
        echo "Power on failed";
        exit 1;
    fi
fi

if [[ $1 == "connect" ]]; then
    echo "Connecting to headset";
    if bluetoothctl connect "$HEADSET_MAC_ADDRESS" > /dev/null; then
        echo "Successfully connected";
    else
        echo "Connection failed";
        exit 1;
    fi

elif [[ $1 == "disconnect" ]]; then
    echo "Disconnecting headset";
    if bluetoothctl disconnect "$HEADSET_MAC_ADDRESS" > /dev/null; then
        echo "Successfully disconnected";
    else
        echo "Disconnecting failed";
        exit 1;
    fi

else
    echo -e "Unknown option given: $1\nUsage: headset.sh connect|disconnect"
    exit 1;
fi
