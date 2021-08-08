#!/usr/bin/env python
# Ansible managed

import dbus

from enum import Enum


class PlaybackStatus(Enum):
    PAUSED = "Paused"
    PLAYING = "Playing"
    STOPPED = "Stopped"


ICON_PLAY = ""
ICON_PAUSE = ""
ICON_STOP = ""

try:

    session_bus = dbus.SessionBus()

    spotify_bus = session_bus.get_object(
        "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2"
    )

    spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")

    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    playback_status = spotify_properties.Get(
        "org.mpris.MediaPlayer2.Player", "PlaybackStatus"
    )

except dbus.exceptions.DBusException:
    print(" ~ ")

else:

    icon = ""
    if PlaybackStatus(playback_status) == PlaybackStatus.PAUSED:
        icon = ICON_PAUSE
    elif PlaybackStatus(playback_status) == PlaybackStatus.PLAYING:
        icon = ICON_PLAY
    elif PlaybackStatus(playback_status) == PlaybackStatus.STOPPED:
        icon = ICON_STOP

    string = (
        f"{ icon }"
        f"{','.join(metadata['xesam:artist'])}"
        " ~ "
        f"{ metadata['xesam:title'].strip() }"
    )

    if len(string) > 80:
        string = string[:77] + "..."

    print(string)
