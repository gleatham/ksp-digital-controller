class BaseControlsFrameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self._bind()

    def _bind(self):
        self.view.throttle_up_button.config(command=self.model.throttle_up)
        self.view.throttle_down_button.config(command=self.model.throttle_down)
        self.view.stage_button.config(command=self.model.stage)
        self.view.launch_button.config(command=self.model.launch)