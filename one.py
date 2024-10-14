import krpc
import time

class FirstLaunch:
    def __init__(self):
        self.conn = krpc.connect(name='FirstLaunch')
        self.vessel = self.conn.space_center.active_vessel

    def launch(self):
        self.vessel.auto_pilot.target_pitch_and_heading(90, 90)
        self.vessel.control.throttle = 1.0

        self.vessel.control.activate_next_stage()

        while (self.vessel.flight().vertical_speed > 10):
            time.sleep(1.0)

