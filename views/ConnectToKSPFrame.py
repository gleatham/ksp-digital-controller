import tkinter as tk

class ConnectToKSPFrame(tk.Frame):
    def __init__(self, parent, row, col):
        super().__init__(parent)

        self.connect_frame = tk.LabelFrame(parent, text="Connect to KSP", height=200, width=200,
                                           padx=5, pady=5)
        self.connect_frame.grid(row=row, column=col)
        self.connect_frame.grid_propagate(False)

        self.connection_status = tk.StringVar()
        self.connection_status.set("Disconnected")

        self.connection_status_label = tk.Label(self.connect_frame, textvariable=self.connection_status)
        self.connection_status_label.grid(row=0, column=0, padx=5, pady=5)

        self.connect_button = tk.Button(self.connect_frame, text="Connect", width=8)
        self.connect_button.grid(row=1, column=0, padx=5, pady=5)