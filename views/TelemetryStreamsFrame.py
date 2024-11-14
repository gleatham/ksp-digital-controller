import tkinter as tk

class TelemetryStreamsFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__(parent)
        #self.altitude = tk.IntVar()
        #self.speed = tk.IntVar()
        #self.apoapsis = tk.IntVar()
        #self.periapsis = tk.IntVar()
        #self.latitude = tk.DoubleVar()
        #self.longitude = tk.DoubleVar()

        #self.altitude = altitude

        # Main Streams Frame
        self.streams_frame = tk.LabelFrame(parent, text='Telemetry', height=200, width=250,
                                      highlightthickness=3, highlightbackground='dark red',
                                      padx=5, pady=5)
        self.streams_frame.grid(row=row, column=col)
        self.streams_frame.grid_propagate(False)

        self.altitude_stream_label = tk.Label(self.streams_frame, text=f'Altitude: ')
        self.speed_stream_label = tk.Label(self.streams_frame, text=f'Speed: ')
        self.apoapsis_stream_label = tk.Label(self.streams_frame, text=f'Apoapsis: ')
        self.periapsis_stream_label = tk.Label(self.streams_frame, text=f'Periapsis: ')
        self.latitude_stream_label = tk.Label(self.streams_frame, text=f'Latitude: ')
        self.longitude_stream_label = tk.Label(self.streams_frame, text=f'Longitude: ')

        self.altitude_stream_label.grid(row=0, column=0, pady=3)
        self.speed_stream_label.grid(row=1, column=0)
        self.apoapsis_stream_label.grid(row=2, column=0)
        self.periapsis_stream_label.grid(row=3, column=0)
        self.latitude_stream_label.grid(row=4, column=0)
        self.longitude_stream_label.grid(row=5, column=0)
