class AutopilotControlsFrameController:
    def __init__(self, model, view):
        self.model = model
        self.view =view

        self._bind()

    def _bind(self):
        self.view.fly_level_button.config(command=self.model.fly_level)
        self.view.engage_button.config(command=self.model.engage_autopilot)