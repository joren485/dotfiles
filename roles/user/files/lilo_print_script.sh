#!/bin/bash

# Author: Daan Sprenkels <dsprenkels@science.ru.nl>
# Description: script for easy printing to P�age from lilo

PROGNAME="peage-print"
VERSION="0.1.2 (2016-08-30)"
PRINT_SERVER="payprint01.ru.nl"
PRINT_QUEUE="RU-Print"
SNUMBER_CACHE_FILE="$HOME/.cache/snumber.txt"

function show_help {
    cat << END
Script for easy printing to P�age from lilo

Usage:
    $APP_BASENAME [options] file

Options:
    -h, --help          Display this message
    -v, --version       Print version info and exit

Bugs:
    Please report bugs to Daan Sprenkels <dsprenkels@science.ru.nl>.
END
}

function show_version {
    echo "$PROGNAME $VERSION"
}

# Parse command line arguments
APP_BASENAME=$0
while [[ $# -gt 0 ]]; do
    case "$1" in
        "-h"|"--help")
            show_help
            exit 0
        ;;
        "-v"|"--version")
            show_version
            exit 0
        ;;
        *)
            if [[ $1 == "-"* ]]; then
                # This is an unknown option
                echo "Unknown option: $1" >&2
                exit 1
            else
                # We will assume that this is the to-be-printed file
                if [ -z ${FILE+x} ]; then
                    FILE=$1
                else
                    echo "More than one file supplied" >&2
                    exit 1
                fi
            fi
            shift
        ;;
    esac
done

# Read student number from cache
if [[ -f "$SNUMBER_CACHE_FILE" && -r "$SNUMBER_CACHE_FILE" ]]; then
    SNUMBER=$(cat "$SNUMBER_CACHE_FILE")
else
    read -r -p 'RU domain username (e.g. `ru\s1234567`): ' SNUMBER
fi

# Build smbclient input string
if [[ ! -f "$FILE" || ! -r "$FILE" ]]; then
    echo "Cannot read specified file $FILE" >&2
    exit 1
fi

# Send print jobs
echo "Connecting as '$SNUMBER' to $PRINT_SERVER" >&2
smbclient -g -U "$SNUMBER" -c "print \"$FILE\"" '\\'"$PRINT_SERVER"'\'"$PRINT_QUEUE"
SMBSTATUS=$?

# If no problems occurred; save student number for next time
[ $SMBSTATUS -eq 0 ] && \
mkdir -p $(dirname $SNUMBER_CACHE_FILE) && \
echo "$SNUMBER" >"$SNUMBER_CACHE_FILE"

exit 0
