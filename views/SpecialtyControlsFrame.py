import tkinter as tk

class SpecialtyControlsFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__(parent)

        self.row = row
        self.col = col

        self.specialty_controls_frame = tk.LabelFrame(parent, text='Specialty', height=200, width=250,)
        self.specialty_controls_frame.grid(row=row, column=col, padx=5, pady=5)
        self.specialty_controls_frame.grid_propagate(False)

        self.button_orbit_ssto = tk.Button(self.specialty_controls_frame, text='Orbit SSTO', width=10)

        self.button_orbit_ssto.grid(row=0, column=0, padx=5, pady=5)