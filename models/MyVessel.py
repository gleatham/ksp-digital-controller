import krpc
import math
import time

import controllers.connect_to_ksp_controller


class MyVessel:
    def __init__(self):
        self.is_connected = False

        self.conn = None
        self.vessel = None
        self.flight_info = None

        # Set Defaults
        self.current_pitch = 0
        self.goal_heading = 90
        self.goal_altitude = 1000
        self.goal_apoapsis = 70000
        self.goal_periapsis = 70000

        # Setup Telemetry Streams
        #flight_info = self.vessel.flight()
        self.current_altitude_stream = None
        self.current_speed = None
        self.current_apoapsis = None
        self.current_periapsis = None

        # TODO: Fix the below varibles
        #self.current_latitude = self.conn.add_stream(getattr, self.vessel.orbit, 'latitude')
        #self.current_longitude = self.conn.add_stream(getattr, self.vessel.orbit, 'longitude')

        # Parts Lists
        self.experiments = []

    # TODO: Add button to main to run connect()
    def connect(self):
        try:
            self.conn = krpc.connect()
            self.vessel = self.conn.space_center.active_vessel
            self.vessel.control.sas = False
            self.vessel.control.sas_mode.stability_assist = False
            self.is_connected = True
            controllers.connect_to_ksp_controller.ConnectToKSPController.update_status(self.is_connected)
        except ConnectionError:
            self.is_connected = False
            controllers.connect_to_ksp_controller.ConnectToKSPController.update_status(self.is_connected)


    # TODO: Add button to start telemetry, put it in the telemtry frame and make data appear after button pressed
    def start_telemetry(self):
        try:
            self.flight_info = self.vessel.flight()
            self.current_altitude_stream = self.conn.add_stream(getattr, self.flight_info, 'mean_altitude')
            self.current_speed = self.conn.add_stream(getattr, self.flight_info, 'speed')
            # TODO: Fix the below varibles
            self.current_apoapsis = self.conn.add_stream(getattr, self.vessel.orbit, 'apoapsis_altitude')
            self.current_periapsis = self.conn.add_stream(getattr, self.vessel.orbit, 'periapsis_altitude')
            #self.current_latitude = self.conn.add_stream(getattr, self.vessel.orbit, 'latitude')
            #self.current_longitude = self.conn.add_stream(getattr, self.vessel.orbit, 'longitude')
        except AttributeError:
            # TODO: Add pop-up window to warn user
            print("Unable to start streams")

    def get_altitude(self):
        if self.current_altitude_stream is None:
            pass
        else:
            return self.current_altitude_stream


    def throttle_up(self):
        if self.vessel.control.throttle == 1.0:
            pass
        self.vessel.control.throttle += 0.1

    def throttle_down(self):
        if self.vessel.control.throttle == 0.0:
            pass
        self.vessel.control.throttle -= 0.1

    def stage(self):
        self.vessel.control.activate_next_stage()

    def launch(self):
        self.vessel.control.throttle = 1.0
        self.vessel.control.activate_next_stage()

    def engage_autopilot(self):
        # Needs target pitch and target heading
        pass

    def calculate_hohmann_transfer(self):
        pass
