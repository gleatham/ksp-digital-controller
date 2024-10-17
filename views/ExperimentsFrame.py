import tkinter as tk

class ExperimentsFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__()

        self.experiments_frame = tk.LabelFrame(parent, text='Experiment(s)', height=200, width=250,)
        self.experiments_frame.grid(row=row, column=col)
        self.experiments_frame.grid_propagate(False)