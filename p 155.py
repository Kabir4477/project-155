# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:19:46 2023

@author: drsau
"""

from tkinter import *
import random
root = Tk()
root.title("Dictionary")
root.geometry("600x600")



dictionary = {'Colours':["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1","deep pink","cyan"]}


def change_colour():
    random_no = random.randint(0,7)
    print(dictionary["Colours"][random_no])
    root.configure(background = dictionary["Colours"][random_no])

    

button_colour = Button(root, text = "Click me", command=change_colour)
button_colour.place(relx = 0.5 , rely = 0.5, anchor = CENTER)





root.mainloop()