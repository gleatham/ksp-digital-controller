import krpc
import threading
import time
from models import MyVessel
import math


class SSTO(MyVessel.MyVessel):
    def __init__(self):
        super().__init__()

        self.name = 'SSTO'
        self.landing_gear = None

    def get_pitch(self):
        self.current_pitch = self.vessel.flight().pitch

    def turn_on_sas(self):
        self.vessel.control.sas = True
        self.vessel.control.sas_mode.stability_assist = True

    def fly_level(self):
        self.vessel.auto_pilot.target_pitch(0)
        self.vessel.auto_pilot.target_roll(0)
        self.vessel.auto_pilot.engage()
        self.vessel.auto_pilot.wait()

    def takeoff(self):
        try:
            self.landing_gear = [part for part in self.vessel.parts.wheels]
        except AttributeError:
            print(f"No landing gear available")

        print(f"Take off sequence initiated")
        self.vessel.control.brakes = False

        while self.vessel.flight(self.vessel.orbit.body.reference_frame).speed < 100:
            self.vessel.control.throttle = 0.7
            self.vessel.control.activate_next_stage()

            self.vessel.auto_pilot.target_pitch_and_heading(0, 90)
            self.vessel.auto_pilot.target_roll = 0
            self.vessel.auto_pilot.engage()
            self.vessel.auto_pilot.wait()
            time.sleep(1)

        while self.vessel.flight().mean_altitude < 300:
            if self.vessel.flight().mean_altitude > 100:
                if any(gear.deployed for gear in self.landing_gear):
                    self.vessel.control.gear = False
                    self.vessel.control.throttle = 1.0
            self.vessel.auto_pilot.target_pitch_and_heading(10, 90)
            self.vessel.auto_pilot.engage()
            self.vessel.auto_pilot.wait()

    def get_to_400_meters_per_second(self):
        print("Accelerating to 400m/s")
        while self.vessel.flight(self.vessel.orbit.body.reference_frame).speed < 400:
            self.vessel.auto_pilot.target_pitch_and_heading(15, 90)
            self.vessel.auto_pilot.target_roll = 0
            self.vessel.auto_pilot.engage()
            self.vessel.auto_pilot.wait()
            time.sleep(1)

    def climb(self):
        while self.vessel.orbit.apoapsis_altitude < self.goal_apoapsis:
            self.vessel.auto_pilot.target_roll = 0
            if self.vessel.flight().pitch < 25:
                self.get_pitch()
                self.vessel.auto_pilot.target_pitch_and_heading(self.current_pitch + 2, 90)
                self.vessel.auto_pilot.engage()
                self.vessel.auto_pilot.wait()
                time.sleep(1)
            if self.vessel.flight().pitch > 25:
                self.get_pitch()
                self.vessel.auto_pilot.target_pitch_and_heading(self.current_pitch - 2, 90)
                self.vessel.auto_pilot.engage()
                self.vessel.auto_pilot.wait()
                time.sleep(1)

            if self.vessel.flight().mean_altitude > 25000:
                pass

            print(self.vessel.orbit.apoapsis_altitude)
        self.glide_to_apoapsis()

    def glide_to_apoapsis(self):
        self.vessel.control.throttle = 0
        print("Gliding...")
        count = 0

        while self.vessel.orbit.apoapsis_altitude > self.goal_apoapsis:
            if self.vessel.flight().mean_altitude > self.goal_apoapsis - 1000:
                self.final_burn()

        if self.vessel.orbit.apoapsis_altitude < self.goal_apoapsis:
            self.climb()

    def final_burn(self):
        ut = self.conn.add_stream(getattr, self.conn.space_center, 'ut')
        # Plan circularization burn (using vis-viva equation)
        print('Planning circularization burn')
        mu = self.vessel.orbit.body.gravitational_parameter
        r = self.vessel.orbit.apoapsis
        a1 = self.vessel.orbit.semi_major_axis
        a2 = r
        v1 = math.sqrt(mu * ((2. / r) - (1. / a1)))
        v2 = math.sqrt(mu * ((2. / r) - (1. / a2)))
        delta_v = v2 - v1
        node = self.vessel.control.add_node(
            ut() + self.vessel.orbit.time_to_apoapsis, prograde=delta_v)

        # Calculate burn time (using rocket equation)
        F = self.vessel.available_thrust
        Isp = self.vessel.specific_impulse * 9.82
        m0 = self.vessel.mass
        m1 = m0 / math.exp(delta_v / Isp)
        flow_rate = F / Isp
        burn_time = (m0 - m1) / flow_rate

        # Orientate ship
        print('Orientating ship for circularization burn')
        self.vessel.auto_pilot.reference_frame = node.reference_frame
        self.vessel.auto_pilot.target_direction = (0, 1, 0)
        self.vessel.auto_pilot.wait()

        # Wait until burn
        print('Waiting until circularization burn')
        burn_ut = ut() + self.vessel.orbit.time_to_apoapsis - (burn_time / 2.)
        lead_time = 5
        self.conn.space_center.warp_to(burn_ut - lead_time)

        # Execute burn
        print('Ready to execute burn')
        time_to_apoapsis = self.conn.add_stream(getattr, self.vessel.orbit, 'time_to_apoapsis')
        while time_to_apoapsis() - (burn_time / 2.) > 0:
            pass
        print('Executing burn')
        self.vessel.control.throttle = 1.0
        time.sleep(burn_time - 0.1)
        print('Fine tuning')
        self.vessel.control.throttle = 0.05
        remaining_burn = self.conn.add_stream(node.remaining_burn_vector, node.reference_frame)
        while remaining_burn()[1] > 0:
            pass
        self.vessel.control.throttle = 0.0
        node.remove()


    def orbit(self):
        self.takeoff()
        self.get_to_400_meters_per_second()
        self.climb()
        self.glide_to_apoapsis()
        self.final_burn()

        self.vessel.control.sas = True

    def _orbit(self):
        orbit_thread = threading.Thread(target=self.orbit)
        orbit_thread.start()
