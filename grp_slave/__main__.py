from grp_slave.gui.main_window import MainWindow
from grp_slave.utils.system import is_windows, is_windows_11, is_admin, elevate


def main():
    if is_windows() and is_windows_11() and not is_admin():
        elevate()
        exit()

    window = MainWindow()
    window.mainloop()


if __name__ == '__main__':
    main()
