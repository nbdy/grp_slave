import time

import tqdm
from customtkinter import CTk
from pynput.keyboard import Key, Listener as KeyListener

from grp_slave import log

from grp_slave.enums.task import Task

from grp_slave.gui.task_button_frame import TaskButtonFrame
from grp_slave.gui.task_progress_frame import TaskProgressFrame
from grp_slave.gui.task_setting_frame import TaskSettingFrame
from grp_slave.gui.notification_bar import LinuxNotificationBar, UACNotificationBar, WindowNotFoundNotificationBar

from grp_slave.utils.system import is_windows, is_windows_11, is_admin
from grp_slave.utils.window import find_window


class MainWindow(CTk):
    break_task_loop: bool = False

    def on_break_press(self, key: Key):
        if key.f9:
            self.break_task_loop = True

    def __init__(self):
        super().__init__()
        self.title("GRP Slave")

        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.window_not_found_notification_bar = WindowNotFoundNotificationBar(self, self.handle_window_not_found_acknowledgement)

        if is_windows():
            if is_windows_11() and not is_admin():
                self.uac_notification_bar = UACNotificationBar(self, self.handle_uac_callback)
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

        self.break_task_listener = KeyListener(on_press=self.on_break_press)

    def handle_linux_acknowledgement(self):
        self.linux_notification_bar.grid_forget()
        self.linux_notification_bar.destroy()

    def handle_window_not_found_acknowledgement(self):
        self.window_not_found_notification_bar.grid_forget()

    def handle_uac_callback(self):
        self.destroy()

    def get_task_progress_text(self, idx: int, stopped: bool = False) -> str:
        text = "Stopped" if stopped else "Running"
        return f"{idx}/{self.task_setting_frame.count.get()} ({text})"

    def handle_task(self, task: Task):
        window = find_window()
        window.activate()
        time.sleep(1)

        if window:
            count = int(self.task_setting_frame.count.get())
            log.debug(f"Running task '{task.value}' {count} times")
            self.task_progress_bar.progress["maximum"] = count
            self.task_progress_bar.progress["mode"] = "determinate"
            self.task_progress_bar.text["text"] = self.get_task_progress_text(0)
            for i in tqdm.tqdm(range(count)):
                if self.break_task_loop:
                    break
                task.run((window.top, window.left))
                self.task_progress_bar.progress.step()
                self.task_progress_bar.text["text"] = self.get_task_progress_text(i)
            self.task_progress_bar.text["text"] = self.get_task_progress_text(count, True)
            self.break_task_loop = False
        else:
            log.error("Could not find window")
            self.window_not_found_notification_bar.grid(row=0, columnspan=2, padx=8, pady=8, sticky="new")
