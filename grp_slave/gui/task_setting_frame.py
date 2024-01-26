from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, IntVar


class TaskSettingFrame(CTkFrame):
    def count_validator(self, count):
        return str.isdigit(count) or count == ""

    def __init__(self, parent: CTk):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.label = CTkLabel(self, text="Repeat:")
        self.label.grid(row=0, column=0, sticky="w")

        self.count = CTkEntry(self, textvariable=IntVar(value=100, name="Count"), width=80, validate="all", validatecommand=(self.count_validator, "%P"))
        self.count.grid(row=0, column=1, padx=8, sticky="e")
