#!/usr/bin/env python


def SendKeys(keys):
    if keys == '{ENTER}':
        keys = 'return'
    from os import system
    system('osascript -e \'tell application "System Events" to keystroke ' + keys + "'")