# Will be used to hold app state in the future.
#TODO: Move app state from MyVessel to State
'''
Track State of:
    - MyVessel
    - Settings (loaded from settings json file)
    - I know there has to be something else...
'''
import models


class State:
    def __init__(self):
        self.vessels = []
        self.settings = self.get_settings()

    def get_settings(self):
        # load settings file from json file
        pass

