class TelemetryStreamsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self._bind()

    def _bind(self):
        pass