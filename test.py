from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('500x500')
root.title('KRPC - Digital Controller')

throttle = IntVar()
heading = IntVar()
pitch = IntVar()
roll_angle = IntVar()

# Main Streams Frame
guidance_frame = tk.LabelFrame(root, text="Guidance", height=200, width=250, highlightthickness=3,
                               highlightbackground='dark red')
guidance_frame.grid(row=0, column=0)

throttle_slider = tk.Scale(guidance_frame, variable=throttle,
                           from_=100, to=0,
                           orient=VERTICAL)
throttle_label = tk.Label(guidance_frame, text="Throttle")
throttle_slider.grid(row=0, column=0)
throttle_label.grid(row=1, column=0)

heading_slider = tk.Scale(guidance_frame, variable=heading,
                          from_=359, to=0,
                          orient=VERTICAL)
heading_label = tk.Label(guidance_frame, text="Heading")
heading_slider.grid(row=0, column=1)
heading_label.grid(row=1, column=1)

pitch_slider = tk.Scale(guidance_frame, variable=pitch,
                        from_=-90, to=90,
                        orient=VERTICAL)
pitch_label = tk.Label(guidance_frame, text="Pitch")
pitch_slider.grid(row=0, column=2)
pitch_label.grid(row=1, column=2)

roll_slider = tk.Scale(guidance_frame, variable=roll_angle,
                       from_=359, to=0,
                       orient=VERTICAL)
roll_label = tk.Label(guidance_frame, text="Roll")
roll_slider.grid(row=0, column=3)
roll_label.grid(row=1, column=3)

root.mainloop()
