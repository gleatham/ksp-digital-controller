import tkinter as tk

class ExperimentsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        experiments_frame = tk.LabelFrame(self, text='Experiment(s)', height=200, width=250,)