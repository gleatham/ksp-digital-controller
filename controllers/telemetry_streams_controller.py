import threading
import time

class TelemetryStreamsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self._bind()
        self.start_telemetry_streams()

        update_stream_thread = threading.Thread(target=lambda:self._update_streams())
        update_stream_thread.start()
        #self.run()

    def _bind(self):
        self.view.speed_stream_label.config(text="Speed: 0")

    def run(self):

        while True:
            self._update_streams()

    def start_telemetry_streams(self):
        pass
        self.model.start_telemetry()

    def _update_streams(self):
        while True:
            self.view.altitude_stream_label.config(text=f"Altitude: {self.model.get_altitude()}")
            time.sleep(0.5)
