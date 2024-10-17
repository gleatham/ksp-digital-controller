import time
from models import MyVessel
import math

class Rocket(MyVessel.MyVessel):
    def __init__(self):
        super().__init__()
        self.name = 'Rocket'
