from tkinter import *
import tkinter.ttk
master = Tk()

#variables
player1 = "A" 
player2 = "B"
player3 = "C"
kills_p1 = IntVar()
kills_p1.set(0)
def kill_count_p1():
    kills_p1.set(kills_p1.get()+1)
kills_p2 = 0
kills_p3 = 0


#Labels
Label(master, text="Team 1", font=("Courier", 30)).grid(row=0)
Label(master, text="NAME", font=("Courier", 25)).grid(row=1)
Label(master, text="KILLS", font=("Courier", 25)).grid(column=2, row=1)
Label(master, text="kill-buttons", font=("Courier", 22)).grid(column=4, row=1)

Label(master, text=player1, font=("Courier", 20)).grid(row=2)
Label(master, text=player2, font=("Courier", 20)).grid(row=3)
Label(master, text=player3, font=("Courier", 20)).grid(row=4)

Label(master, textvariable=kills_p1, font=("Courier", 20)).grid(column = 2, row=2) 

tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=1, row=1, rowspan=4, sticky='ns')
tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=3, row=1, rowspan=4, sticky='ns')

#button_commands

    

#Buttons
Button(master, text="p1: add kill", font=("Courier", 20), command=kill_count_p1).grid(column=4, row=2)

print("this is not a fully working project yet so don't worry")

                   
                   


