import tkinter as tk

class SpecialtyControlsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.specialty_controls_frame = tk.LabelFrame(self, text='Specialty', height=200, width=250,)
        self.button_orbit_ssto = tk.Button(self.specialty_controls_frame, text='Orbit SSTO', width=10)

        self.button_orbit_ssto.grid(row=0, column=0, padx=5, pady=5)