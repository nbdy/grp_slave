from customtkinter import CTk

from grp_slave import log

from grp_slave.enums.task import Task

from grp_slave.gui.task_button_frame import TaskButtonFrame
from grp_slave.gui.task_progress_frame import TaskProgressFrame
from grp_slave.gui.task_setting_frame import TaskSettingFrame
from grp_slave.gui.notification_bar import LinuxNotificationBar, UACNotificationBar, WindowNotFoundNotificationBar

from grp_slave.utils.system import is_windows, is_windows_11, is_admin
from grp_slave.utils.window import find_window


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("GRP Slave")

        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.window_not_found_notification_bar = WindowNotFoundNotificationBar(self, self.handle_window_not_found_acknowledgement)

        if is_windows():
            if is_windows_11() and not is_admin():
                self.uac_notification_bar = UACNotificationBar(self)
                self.uac_notification_bar.grid(row=0, columnspan=2, padx=8, pady=8, sticky="new")
        else:
            self.linux_notification_bar = LinuxNotificationBar(self, self.handle_linux_acknowledgement)
            self.linux_notification_bar.grid(row=0, columnspan=2, padx=8, pady=8, sticky="new")

        self.task_setting_frame = TaskSettingFrame(self)
        self.task_setting_frame.grid(row=1, column=0, padx=4, pady=8, sticky="w")

        self.task_progress_bar = TaskProgressFrame(self)
        self.task_progress_bar.grid(row=1, column=1, padx=4, pady=8, sticky="e")

        self.task_frame = TaskButtonFrame(self, self.handle_task)
        self.task_frame.grid(row=2, columnspan=2, padx=8, pady=8, sticky="w")

    def handle_linux_acknowledgement(self):
        self.linux_notification_bar.grid_forget()
        self.linux_notification_bar.destroy()

    def handle_window_not_found_acknowledgement(self):
        pass

    def handle_task(self, task: Task):
        window = find_window()

        if window:
            log.debug("Running task '", task.value, "' ", self.task_setting_frame.count.get(), "times")
            for i in range(self.task_setting_frame.count.get()):
                task.run((window.top, window.left))
                self.task_progress_bar.progress.step()
        else:
            log.error("Could not find window")
            self.window_not_found_notification_bar.grid(row=0, columnspan=2, padx=8, pady=8, sticky="new")
