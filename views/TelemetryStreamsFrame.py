import tkinter as tk

class TelemetryStreamsFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__(parent)

        # Main Streams Frame
        self.streams_frame = tk.LabelFrame(parent, text='Telemetry', height=200, width=250,
                                      highlightthickness=3, highlightbackground='dark red',
                                      padx=5, pady=5)
        self.streams_frame.grid(row=row, column=col)
        self.streams_frame.grid_propagate(False)

        self.altitude_stream_label = tk.Label(self.streams_frame, text='Altitude:')
        self.speed_stream_label = tk.Label(self.streams_frame, text='Speed:')
        self.apoapsis_stream_label = tk.Label(self.streams_frame, text='Apoapsis:')
        self.periapsis_stream_label = tk.Label(self.streams_frame, text='Periapsis:')
        self.latitude_stream_label = tk.Label(self.streams_frame, text='Latitude:')
        self.longitude_stream_label = tk.Label(self.streams_frame, text='Longitude:')

        self.altitude_stream_label.grid(row=0, column=0, pady=3)
        self.speed_stream_label.grid(row=1, column=0)
        self.apoapsis_stream_label.grid(row=2, column=0)
        self.periapsis_stream_label.grid(row=3, column=0)
        self.latitude_stream_label.grid(row=4, column=0)
        self.longitude_stream_label.grid(row=5, column=0)
