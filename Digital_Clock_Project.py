import tkinter
from tkinter import *  #importing all the files in tkinter lib
import time    #importing time lib


window = Tk() #creating new variable in the name of 'window'.
window.title("My Time") # "My Time" is the title of our new window

def Current_Time(): #defining a function

        Time = time.strftime("%I:%M:%S:%p") #here time is converting into stringformat
        Digital_clock.config(text=Time)
        Digital_clock.after(1000,Current_Time) #1000 milliseconds provided in this digital clock


Digital_clock = Label(window,font=("rosemary",40),bg = "white",fg = "black") #Creating font and background
Digital_clock.pack() #enclosing Labelled tkinter file with .pack()

Current_Time() #calling a function

window.mainloop()