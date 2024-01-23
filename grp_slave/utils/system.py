import sys
import ctypes

from grp_slave import log


def is_windows():
    return sys.platform.startswith('win')


def is_windows_11():
    version = sys.getwindowsversion()
    log.debug(version)
    return version.build >= 22000


def is_admin():
    ret = False

    try:
        ret = ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as ex:
        log.error(ex)
        pass

    log.debug(ret)

    return ret


def elevate():
    log.debug("Restarting as admin")
    ctypes.windll.shell32.ShellExecuteW(None, sys.executable, " ".join(sys.argv), None, 1)
