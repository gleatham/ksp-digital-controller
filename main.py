import tkinter as tk
import threading
import Ssto


def update_stream(ssto,
                  altitude_stream_label,
                  speed_stream_label,
                  apoapsis_stream_label,
                  periapsis_stream_label):
    while True:
        altitude_stream_label.config(text=f"Altitude: {ssto.current_altitude():.0f}")
        speed_stream_label.config(text=f"Speed: {ssto.current_speed():.0f}")
        apoapsis_stream_label.config(text=f"Apoapsis: {ssto.current_apoapsis():.0f}")
        periapsis_stream_label.config(text=f"Periapsis: {ssto.current_periapsis():.0f}")


def ssto_orbit(ssto,
               altitude_stream_label,
               speed_stream_label,
               apoapsis_stream_label,
               periapsis_stream_label):
    update_stream_thread = threading.Thread(target=lambda: update_stream(ssto,
                                                                         altitude_stream_label,
                                                                         speed_stream_label,
                                                                         apoapsis_stream_label,
                                                                         periapsis_stream_label))
    update_stream_thread.start()
    orbit_thread = threading.Thread(target=ssto.orbit)
    orbit_thread.start()


def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('KRPC - Digital Controller')

    my_vessel = Ssto.SSTO()

    # Main Streams Frame
    streams_frame = tk.LabelFrame(root, text='Telemetry', height=200, width=250,
                                  highlightthickness=3, highlightbackground='dark red',
                                  padx=5, pady=5)
    altitude_stream_label = tk.Label(streams_frame, text='Altitude:')
    speed_stream_label = tk.Label(streams_frame, text='Speed:')
    apoapsis_stream_label = tk.Label(streams_frame, text='Apoapsis:')
    periapsis_stream_label = tk.Label(streams_frame, text='Periapsis:')
    latitude_stream_label = tk.Label(streams_frame, text='Latitude:')
    longitude_stream_label = tk.Label(streams_frame, text='Longitude:')

    altitude_stream_label.grid(row=0, column=0, pady=3)
    speed_stream_label.grid(row=1, column=0)
    apoapsis_stream_label.grid(row=2, column=0)
    periapsis_stream_label.grid(row=3, column=0)
    latitude_stream_label.grid(row=4, column=0)
    longitude_stream_label.grid(row=5, column=0)

    # Specialty Controls Frame
    specialty_controls_frame = tk.LabelFrame(root, text='Auto Pilot', height=200, width=250,
                                             highlightthickness=3, highlightbackground='dark red',
                                             padx=5, pady=5)
    button_orbit_ssto = tk.Button(specialty_controls_frame, text='Orbit SSTO',
                                  command=lambda: ssto_orbit(my_vessel,
                                                             altitude_stream_label,
                                                             speed_stream_label,
                                                             apoapsis_stream_label,
                                                             periapsis_stream_label))
    button_fly_level = tk.Button(specialty_controls_frame, text='Fly Level', command=lambda: my_vessel.fly_level())
    button_orbit_ssto.grid(row=0, column=0, padx=5, pady=5)
    button_fly_level.grid(row=1, column=0, padx=5, pady=5)

    # Base Controls
    # Throttle, stage, launch, abort,
    base_controls_frame = tk.LabelFrame(root, text='Controls', height=200, width=250,
                                        highlightthickness=3, highlightbackground='dark red',
                                        padx=5, pady=5)
    throttle_up_button = tk.Button(base_controls_frame, text='Throttle Up', command=lambda: my_vessel.throttle_up())
    throttle_down_button = tk.Button(base_controls_frame, text='Throttle Down',
                                     command=lambda: my_vessel.throttle_down())
    stage_button = tk.Button(base_controls_frame, text='Stage', command=lambda: my_vessel.stage())
    launch_button = tk.Button(base_controls_frame, text='Abort', command=lambda: my_vessel.launch)

    throttle_up_button.grid(row=0, column=0, padx=5, pady=5)
    throttle_down_button.grid(row=1, column=0, padx=5, pady=5)
    stage_button.grid(row=2, column=0, padx=5, pady=5)
    launch_button.grid(row=3, column=0, padx=5, pady=5)

    # Place frames in root window
    streams_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    streams_frame.grid_propagate(False)
    specialty_controls_frame.grid(row=0, column=1, padx=5, pady=5)
    base_controls_frame.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
