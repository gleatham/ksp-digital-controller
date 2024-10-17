class SpecialtyControlsFrameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self._bind()

    def _bind(self):
        self.view.button_orbit_ssto.config(command=self.model.orbit)