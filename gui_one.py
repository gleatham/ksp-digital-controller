import tkinter as tk
from tkinter import ttk
import threading
import Ssto

def connect_ship():
    pass

def main():
    root = tk.Tk()
    root.geometry('1000x800')
    root.title('KRPC - Digital Controller')

    # my_vessel = Ssto.SSTO()
    button_test = tk.Button(root, text='Test', command=connect_ship)

    # Telemetry Streams Frame
    telemetry_streams_frame = tk.LabelFrame(root, text='Telemetry', height=200, width=250,
                                  highlightthickness=3, highlightbackground='dark red',
                                  padx=5, pady=5)
    altitude_stream_label = tk.Label(telemetry_streams_frame, text='Altitude:')
    speed_stream_label = tk.Label(telemetry_streams_frame, text='Speed:')
    apoapsis_stream_label = tk.Label(telemetry_streams_frame, text='Apoapsis:')
    periapsis_stream_label = tk.Label(telemetry_streams_frame, text='Periapsis:')
    latitude_stream_label = tk.Label(telemetry_streams_frame, text='Latitude:')
    longitude_stream_label = tk.Label(telemetry_streams_frame, text='Longitude:')
    vertical_speed_stream_label = tk.Label(telemetry_streams_frame, text='Vertical Speed:')

    altitude_stream_label.grid(row=0, column=0, pady=3)
    speed_stream_label.grid(row=1, column=0)
    apoapsis_stream_label.grid(row=2, column=0)
    periapsis_stream_label.grid(row=3, column=0)
    latitude_stream_label.grid(row=4, column=0)
    longitude_stream_label.grid(row=5, column=0)
    vertical_speed_stream_label.grid(row=6, column=0)

    # Auto Pilot Controls Frame
    autopilot_controls_frame = tk.LabelFrame(root, text='Auto Pilot', height=200, width=250,
                                             highlightthickness=3, highlightbackground='dark red',
                                             padx=5, pady=5)

    fly_level_button = tk.Button(autopilot_controls_frame, text='Fly Level', width=8)
    engage_button = tk.Button(autopilot_controls_frame, text='Engage', width=8)
    target_pitch_default = tk.IntVar(autopilot_controls_frame, value=0)
    target_pitch_spinbox = tk.Spinbox(autopilot_controls_frame, from_=-90, to=90, width=5,
                                      repeatdelay=500, repeatinterval=100,
                                      textvariable=target_pitch_default)
    target_pitch_label = tk.Label(autopilot_controls_frame, text='Target Pitch:')
    target_heading_default = tk.IntVar(autopilot_controls_frame, value=90)
    target_heading_spinbox = tk.Spinbox(autopilot_controls_frame, from_=0, to=359, width=5,
                                        repeatdelay=500, repeatinterval=100,
                                        textvariable=target_heading_default)
    target_heading_label = tk.Label(autopilot_controls_frame, text='Target Heading:')

    # Grid
    fly_level_button.grid(row=0, column=0, padx=5, pady=5)
    engage_button.grid(row=0, column=1, padx=5, pady=5)
    target_pitch_label.grid(row=1, column=0)
    target_pitch_spinbox.grid(row=1, column=1, padx=5, pady=5)
    target_heading_label.grid(row=2, column=0)
    target_heading_spinbox.grid(row=2, column=1, padx=5, pady=5)

    # Base Controls Frame
    # Throttle, stage, launch, abort,
    base_controls_frame = tk.LabelFrame(root, text='Controls', height=200, width=250,
                                        highlightthickness=3, highlightbackground='dark red',
                                        padx=5, pady=5)
    throttle_up_button = tk.Button(base_controls_frame, text='Throttle +', width=8)
    throttle_down_button = tk.Button(base_controls_frame, text='Throttle -', width=8)
    stage_button = tk.Button(base_controls_frame, text='Stage', width=8)
    launch_button = tk.Button(base_controls_frame, text='Abort', width=8)

    throttle_up_button.grid(row=0, column=0, padx=5, pady=5)
    throttle_down_button.grid(row=1, column=0, padx=5, pady=5)
    stage_button.grid(row=2, column=0, padx=5, pady=5)
    launch_button.grid(row=3, column=0, padx=5, pady=5)

    # Experiments Frame
    experiments_frame = tk.LabelFrame(root, text='Experiment(s)', height=200, width=250,)

    # Specialty Controls Frame
    specialty_controls_frame = tk.LabelFrame(root, text='Specialty', height=200, width=250,)
    button_orbit_ssto = tk.Button(specialty_controls_frame, text='Orbit SSTO', width=10)

    button_orbit_ssto.grid(row=0, column=0, padx=5, pady=5)

    # Vessel Resources Frame
    rocket_fuel_value = tk.IntVar()

    vessel_resources_frame = tk.LabelFrame(root, text='Fuel', height=200, width=250)
    rocket_fuel_progressbar = ttk.Progressbar(vessel_resources_frame, orient=tk.HORIZONTAL, length=100,
                                              mode='determinate', variable=rocket_fuel_value)
    rocket_fuel_progressbar_label = tk.Label(vessel_resources_frame, text='Rocket Fuel')
    rocket_fuel_percentage_label = tk.Label(vessel_resources_frame, text='100%', width=3)
    oxidizer_progressbar = ttk.Progressbar(vessel_resources_frame, orient=tk.HORIZONTAL, length=100)
    oxidizer_progressbar_label = tk.Label(vessel_resources_frame, text='Oxidizer')
    oxidizer_percentage_label = tk.Label(vessel_resources_frame, text='100%', width=3)

    rocket_fuel_progressbar_label.grid(row=0, column=0)
    rocket_fuel_progressbar.grid(row=0, column=1, padx=5, pady=5)
    rocket_fuel_percentage_label.grid(row=0, column=2, padx=5, pady=5)
    oxidizer_progressbar_label.grid(row=1, column=0, padx=5, pady=5)
    oxidizer_progressbar.grid(row=1, column=1, padx=5, pady=5)
    oxidizer_percentage_label.grid(row=1, column=2, padx=5, pady=5)

    '''
    Test Shit
    '''
    rocket_fuel_value.set(74)


    # Place frames in root window
    telemetry_streams_frame.grid(row=0, column=0, padx=5, pady=5)
    telemetry_streams_frame.grid_propagate(False)
    autopilot_controls_frame.grid(row=1, column=1, padx=5, pady=5)
    autopilot_controls_frame.grid_propagate(False)
    base_controls_frame.grid(row=2, column=0, padx=5, pady=5)
    base_controls_frame.grid_propagate(False)
    experiments_frame.grid(row=0, column=1, padx=5, pady=5)
    experiments_frame.grid_propagate(False)
    specialty_controls_frame.grid(row=0, column=2, padx=5, pady=5)
    specialty_controls_frame.grid_propagate(False)
    vessel_resources_frame.grid(row=1, column=0, padx=5, pady=5)
    vessel_resources_frame.grid_propagate(False)

    root.mainloop()


if __name__ == '__main__':
    main()
