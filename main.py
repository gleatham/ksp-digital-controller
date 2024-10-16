import tkinter as tk
from tkinter import ttk
import threading
import views.BaseControlsFrame
'''
import views.AutopilotControlsFrame
import views.VesselResourcesFrame
import views.SpecialtyControlsFrame
import views.ExperimentsFrame
import models.MyVessel
import models.Ssto
import models.rocket
'''

class App:
    def __init__(self):
        self.name = 'derp'


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1000x800')
    root.title('KRPC - Digital Controller')

    base_controls = views.BaseControlsFrame.BaseControlsFrame(root)

    # base_controls.grid(row=0, column=0, sticky='nsew')
    base_controls.pack()

    root.mainloop()
