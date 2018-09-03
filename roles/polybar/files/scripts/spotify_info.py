#!/usr/bin/env python

import dbus
session_bus = dbus.SessionBus()

try:
    spotify_bus = session_bus.get_object(
        'org.mpris.MediaPlayer2.spotify',
        '/org/mpris/MediaPlayer2'
    )

    spotify_properties = dbus.Interface(
        spotify_bus,
        'org.freedesktop.DBus.Properties'
    )

    metadata = spotify_properties.Get(
        'org.mpris.MediaPlayer2.Player',
        'Metadata'
    )

except dbus.exceptions.DBusException:
    print(' ~ ')

else:
    string = (
        f"{','.join(metadata['xesam:artist'])}"
        f" ~ "
        f"{ metadata['xesam:title'].strip() }"
    )

    if len(string) > 80:
        string = string[:77] + '...'

    print(string)
