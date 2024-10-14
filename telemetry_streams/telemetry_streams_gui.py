import tkinter as tk

class TelemetryStreamsGUI(root):
    def __init__(self, parent):


streams_frame = tk.LabelFrame(root, text='Telemetry', height=200, width=250,
                             highlightthickness=3, highlightbackground='dark red',
                             padx=5, pady=5)
altitude_stream_label = tk.Label(streams_frame, text='Altitude:')
speed_stream_label = tk.Label(streams_frame, text='Speed:')
apoapsis_stream_label = tk.Label(streams_frame, text='Apoapsis:')
periapsis_stream_label = tk.Label(streams_frame, text='Periapsis:')

altitude_stream_label.grid(row=0, column=0, pady=3)
speed_stream_label.grid(row=1, column=0)
apoapsis_stream_label.grid(row=2, column=0)
periapsis_stream_label.grid(row=3, column=0)