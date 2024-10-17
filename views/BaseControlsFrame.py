import tkinter as tk
from tkinter import ttk

class BaseControlsFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__()

        self.base_controls_frame = tk.LabelFrame(parent, text='Controls', height=200, width=250,
                                            highlightthickness=3, highlightbackground='dark red',
                                            padx=5, pady=5)
        self.base_controls_frame.grid(row=row, column=col, padx=5, pady=5)
        self.base_controls_frame.grid_propagate(False)
        self.throttle_up_button = tk.Button(self.base_controls_frame, text='Throttle +', width=8)
        self.throttle_down_button = tk.Button(self.base_controls_frame, text='Throttle -', width=8)
        self.stage_button = tk.Button(self.base_controls_frame, text='Stage', width=8)
        self.launch_button = tk.Button(self.base_controls_frame, text='Abort', width=8)

        self.throttle_up_button.grid(row=0, column=0, padx=5, pady=5)
        self.throttle_down_button.grid(row=1, column=0, padx=5, pady=5)
        self.stage_button.grid(row=2, column=0, padx=5, pady=5)
        self.launch_button.grid(row=3, column=0, padx=5, pady=5)