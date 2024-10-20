import threading

class TelemetryStreamsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self._bind()

        update_stream_thread = threading.Thread(target=self._update_streams())
        self.run()

    def _bind(self):
        pass

    def run(self):
        while True:
            self._update_streams()

    def _update_streams(self):
        pass
        self.view.altitude_stream_label.config(text=f"Altitude: {self.model.current_altitude}")