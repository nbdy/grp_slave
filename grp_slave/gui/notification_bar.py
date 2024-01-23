from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton

from grp_slave.utils.system import elevate


class LinuxNotificationBar(CTkFrame):
    def __init__(self, parent: CTk, callback: callable):
        super().__init__(parent, fg_color="#fcb900")
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.info_text_label = CTkLabel(self, text="This is not tested yet on linux", text_color="#fc3b00")
        self.info_text_label.grid(row=0, column=0, sticky="w")

        self.restart_button = CTkButton(self, text="Acknowledge", width=80, command=callback)
        self.restart_button.grid(row=0, column=1, sticky="e")


class UACNotificationBar(CTkFrame):
    def __init__(self, parent: CTk):
        super().__init__(parent, fg_color="#fcb900")
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.info_text_label = CTkLabel(self, text="This application needs admin privileges on Windows 11!", text_color="#fc3b00")
        self.info_text_label.grid(row=0, column=0, sticky="w")

        self.restart_button = CTkButton(self, text="Restart as admin", width=80, command=elevate)
        self.restart_button.grid(row=0, column=1, sticky="e")


class WindowNotFoundNotificationBar(CTkFrame):
    def __init__(self, parent: CTk, callback: callable):
        super().__init__(parent, fg_color="#fcb900")
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.info_text_label = CTkLabel(self, text="GTA window could not be found", text_color="#fc3b00")
        self.info_text_label.grid(row=0, column=0, sticky="w")

        self.restart_button = CTkButton(self, text="Acknowledge", width=80, command=callback)
        self.restart_button.grid(row=0, column=1, sticky="e")
