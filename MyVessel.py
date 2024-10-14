import krpc
import math
import time


class MyVessel:
    def __init__(self):
        self.conn = krpc.connect()
        self.vessel = self.conn.space_center.active_vessel
        self.vessel.control.sas = False
        self.vessel.control.sas_mode.stability_assist = False

        # Setup Streams
        flight_info = self.vessel.flight()
        self.current_altitude = self.conn.add_stream(getattr, flight_info, 'mean_altitude')
        self.current_speed = self.conn.add_stream(getattr, flight_info, 'speed')
        # TODO: Fix the below varibles
        self.current_apoapsis = self.conn.add_stream(getattr, self.vessel.orbit, 'apoapsis_altitude')
        self.current_periapsis = self.conn.add_stream(getattr, self.vessel.orbit, 'periapsis_altitude')
        #self.current_latitude = self.conn.add_stream(getattr, self.vessel.orbit, 'latitude')
        #self.current_longitude = self.conn.add_stream(getattr, self.vessel.orbit, 'longitude')

        # Parts Lists
        self.experiments = []

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

    def calculate_hohmann_transfer(self):
        pass
