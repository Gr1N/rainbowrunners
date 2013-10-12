# -*- coding: utf-8 -*-

import fcntl
import os
import termios
import struct

__all__ = (
    'Colors',

    'get_terminal_size',
)


class Colors(object):
    SUCCESS = 32
    ERROR = 31
    FAIL = 36
    RESULT = 33
    SEPARATOR1 = 35
    SEPARATOR2 = 90


def get_terminal_size():
    def ioctl_GWINSZ(fd):
        try:
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except Exception:  # Pokémon Exception Handling =(
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            with os.open(os.ctermid(), os.O_RDONLY) as fd:
                cr = ioctl_GWINSZ(fd)
        except Exception:  # Pokémon Exception Handling again =(
            pass
    if not cr:
        cr = os.environ.get('LINES', 25), os.environ.get('COLUMNS', 80)

    return int(cr[1]), int(cr[0])
