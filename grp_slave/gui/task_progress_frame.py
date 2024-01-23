from customtkinter import CTk, CTkFrame, CTkLabel, CTkProgressBar


class TaskProgressFrame(CTkFrame):
    def __init__(self, parent: CTk):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.label = CTkLabel(self, text="Progress:")
        self.label.grid(row=0, column=0, sticky="w", padx=4)

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=0, column=1, padx=4)
        self.progress.set(0)

        self.text = CTkLabel(self, text="0/0 (Stopped)")
        self.text.grid(row=0, column=2, padx=4)
