import tkinter as tk
from tkinter import ttk
import threading
from views import AutopilotControlsFrame
from views import BaseControlsFrame
from views import ExperimentsFrame
from views import SpecialtyControlsFrame
from views import TelemetryStreamsFrame
from views import VesselResourcesFrame

class App:
    def __init__(self):
        self.name = 'derp'


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1000x800')
    root.title('KRPC - Digital Controller')

    telemetry_stream = TelemetryStreamsFrame.TelemetryStreamsFrame(root, 0, 0)
    base_controls = BaseControlsFrame.BaseControlsFrame(root, 1, 1)
    autopilot_controls = AutopilotControlsFrame.AutopilotControlsFrame(root, 2, 0)
    experiments = ExperimentsFrame.ExperimentsFrame(root, 0, 1)
    specialty_controls = SpecialtyControlsFrame.SpecialtyControlsFrame(root, 0, 2)
    vessel_resources = VesselResourcesFrame.VesselResourcesFrame(root, 1, 0)


    root.mainloop()
