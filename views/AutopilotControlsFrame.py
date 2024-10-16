import tkinter as tk


class AutopilotControlsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.autopilot_controls_frame = tk.LabelFrame(self, text='Auto Pilot', height=200, width=250,
                                                 highlightthickness=3, highlightbackground='dark red',
                                                 padx=5, pady=5)

        self.fly_level_button = tk.Button(self.autopilot_controls_frame, text='Fly Level', width=8)
        self.engage_button = tk.Button(self.autopilot_controls_frame, text='Engage', width=8)
        self.target_pitch_default = tk.IntVar(self.autopilot_controls_frame, value=0)
        self.target_pitch_spinbox = tk.Spinbox(self.autopilot_controls_frame, from_=-90, to=90, width=5,
                                          repeatdelay=500, repeatinterval=100,
                                          textvariable=self.target_pitch_default)
        self.target_pitch_label = tk.Label(self.autopilot_controls_frame, text='Target Pitch:')
        self.target_heading_default = tk.IntVar(self.autopilot_controls_frame, value=90)
        self.target_heading_spinbox = tk.Spinbox(self.autopilot_controls_frame, from_=0, to=359, width=5,
                                            repeatdelay=500, repeatinterval=100,
                                            textvariable=self.target_heading_default)
        self.target_heading_label = tk.Label(self.autopilot_controls_frame, text='Target Heading:')

        # Grid
        self.fly_level_button.grid(row=0, column=0, padx=5, pady=5)
        self.engage_button.grid(row=0, column=1, padx=5, pady=5)
        self.target_pitch_label.grid(row=1, column=0)
        self.target_pitch_spinbox.grid(row=1, column=1, padx=5, pady=5)
        self.target_heading_label.grid(row=2, column=0)
        self.target_heading_spinbox.grid(row=2, column=1, padx=5, pady=5)

    def connect_interface(self):
        pass