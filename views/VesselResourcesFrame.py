import tkinter as tk
from tkinter import ttk

class VesselResourcesFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__(parent)
        # Vessel Resources Frame
        self.rocket_fuel_value = tk.IntVar()

        self.vessel_resources_frame = tk.LabelFrame(parent, text='Fuel', height=200, width=250)
        self.vessel_resources_frame.grid(row=row, column=col, padx=5, pady=5)
        self.vessel_resources_frame.grid_propagate(False)

        self.rocket_fuel_progressbar = ttk.Progressbar(self.vessel_resources_frame, orient=tk.HORIZONTAL, length=100,
                                                  mode='determinate', variable=self.rocket_fuel_value)
        self.rocket_fuel_progressbar_label = tk.Label(self.vessel_resources_frame, text='Rocket Fuel')
        self.rocket_fuel_percentage_label = tk.Label(self.vessel_resources_frame, text='100%', width=3)
        self.oxidizer_progressbar = ttk.Progressbar(self.vessel_resources_frame, orient=tk.HORIZONTAL, length=100)
        self.oxidizer_progressbar_label = tk.Label(self.vessel_resources_frame, text='Oxidizer')
        self.oxidizer_percentage_label = tk.Label(self.vessel_resources_frame, text='100%', width=3)

        self.rocket_fuel_progressbar_label.grid(row=0, column=0)
        self.rocket_fuel_progressbar.grid(row=0, column=1, padx=5, pady=5)
        self.rocket_fuel_percentage_label.grid(row=0, column=2, padx=5, pady=5)
        self.oxidizer_progressbar_label.grid(row=1, column=0, padx=5, pady=5)
        self.oxidizer_progressbar.grid(row=1, column=1, padx=5, pady=5)
        self.oxidizer_percentage_label.grid(row=1, column=2, padx=5, pady=5)

        '''
        Test Shit
        '''
        self.rocket_fuel_value.set(74)