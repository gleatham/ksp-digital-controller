import tkinter as tk
from tkinter import ttk
import threading

from views import AutopilotControlsFrame
from views import BaseControlsFrame
from views import ExperimentsFrame
from views import SpecialtyControlsFrame
from views import TelemetryStreamsFrame
from views import VesselResourcesFrame
from views import ConnectToKSPFrame

from models import MyVessel
from models import rocket
from models import Ssto

from controllers import autopilot_controls_frame_controller
from controllers import base_controls_frame_controller
from controllers import experiments_frame_controller
from controllers import specialty_controls_frame_controller
from controllers import telemetry_streams_controller
from controllers import vessel_resources_frame_controller
from controllers import connect_to_ksp_controller

def main():
    root = tk.Tk()
    root.geometry('1000x800')
    root.title('KRPC - Digital Controller')

    # Initialize Models
    app_state = State.State()
    my_vessel = Ssto.SSTO()

    # Initialize Views
    autopilot_controls = AutopilotControlsFrame.AutopilotControlsFrame(root, 2, 0)
    base_controls = BaseControlsFrame.BaseControlsFrame(root, 1, 1)
    experiments = ExperimentsFrame.ExperimentsFrame(root, 0, 1)
    specialty_controls = SpecialtyControlsFrame.SpecialtyControlsFrame(root, 0, 2)
    telemetry_stream = TelemetryStreamsFrame.TelemetryStreamsFrame(root, 0, 0)
    vessel_resources = VesselResourcesFrame.VesselResourcesFrame(root, 1, 0)
    connect_to_ksp = ConnectToKSPFrame.ConnectToKSPFrame(root, 0, 3)

    # Grid Views
    #autopilot_controls.grid(row = autopilot_controls.row, col = autopilot_controls.col)

    # Initialize Controllers
    autopilot_controls_controller = autopilot_controls_frame_controller.AutopilotControlsFrameController(my_vessel,
                                                                                                         autopilot_controls)
    base_controls_controller = base_controls_frame_controller.BaseControlsFrameController(my_vessel, base_controls)
    experiments_controller = experiments_frame_controller
    specialty_controls_controller = specialty_controls_frame_controller.SpecialtyControlsFrameController(my_vessel,
                                                                                                         specialty_controls)
    telemetry_stream_controller = telemetry_streams_controller.TelemetryStreamsController(my_vessel, telemetry_stream)
    vessel_resources_controller = vessel_resources_frame_controller
    ksp_connect_controller = connect_to_ksp_controller.ConnectToKSPController(my_vessel, connect_to_ksp)

    # if not connected pop up a window to connect.
    # if it fails prompt to try again, ensure ksp is open and the krpc server is started.
    #main_loop_thread = threading.Thread(target=root.mainloop)
    #main_loop_thread.start()

    root.mainloop()

if __name__ == '__main__':
    main()
