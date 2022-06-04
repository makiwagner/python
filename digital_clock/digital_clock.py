# This is a simple task to get started with the Tkinter 
# library in Python, which is a built-in package that 
# comes with Python. Tkinter has some cool features that can be 
# used to build simple apps.
from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font=("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()