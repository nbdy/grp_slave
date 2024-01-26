from customtkinter import CTk, CTkFrame, CTkButton
from functools import partial

from grp_slave.enums.task import Task


class TaskButtonFrame(CTkFrame):
    def __init__(self, parent: CTk, task_function: callable):
        super().__init__(parent)
        self.task_buttons = {}

        i = 0
        for task in Task:
            self.grid_columnconfigure(i, weight=1)
            self.task_buttons[task] = CTkButton(self, text=task.value, command=partial(task_function, task), state=task.button_state())
            self.task_buttons[task].grid(row=0, column=i, padx=4)
            i += 1
