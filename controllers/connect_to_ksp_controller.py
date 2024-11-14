class ConnectToKSPController:
    def __init__(self, vessel, view):
        self.vessel = vessel #MyVessel object
        self.view = view

        self.bind()

    def bind(self):
        self.view.connect_button.config(command=self.vessel.connect)

    def update_status(self, is_connected):
        if is_connected:
            self.view.connection_status.set("Connected")
        else:
            self.view.connection_status.set("Disconnected")