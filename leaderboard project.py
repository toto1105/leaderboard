#general
from tkinter import *
import tkinter.ttk
master = Tk()

#input
gamemode = input("which gamemode do you want to play? 1 life gamemode = '1' or respawn gamemode = '2' ")

#variables players and ranks team 1
player1 = "player 1"
player2 = "player 2"
player3 = "player 3"
player4 = "player 4"
player5 = "player 5"
player6 = "player 6"
player7 = "player 7"

rank_p1 = "Assault"
rank_p2 = "Assault"
rank_p3 = "Assault"
rank_p4 = "Assault"
rank_p5 = "Heavy"
rank_p6 = "Heavy"
rank_p7 = "Officer"

#start color team 1
colour_p1 = '#%02x%02x%02x' % (217, 217, 217)
colour_p2 = '#%02x%02x%02x' % (217, 217, 217)
colour_p3 = '#%02x%02x%02x' % (217, 217, 217)
colour_p4 = '#%02x%02x%02x' % (217, 217, 217)
colour_p5 = '#%02x%02x%02x' % (217, 217, 217)
colour_p6 = '#%02x%02x%02x' % (217, 217, 217)
colour_p7 = '#%02x%02x%02x' % (217, 217, 217)

#kill_stuff team 1
kills_p1 = IntVar()
kills_p1.set(0)
kills_p2 = IntVar()
kills_p2.set(0)
kills_p3 = IntVar()
kills_p3.set(0)
kills_p4 = IntVar()
kills_p4.set(0)
kills_p5 = IntVar()
kills_p5.set(0)
kills_p6 = IntVar()
kills_p6.set(0)
kills_p7 = IntVar()
kills_p7.set(0)


amount_kills_for_colorYellow = 0
amount_kills_for_colorOrange = 0
amount_kills_for_colorRed = 0

if gamemode == "1":
    amount_kills_for_colorYellow = 1
    amount_kills_for_colorOrange = 3
    amount_kills_for_colorRed = 5
elif gamemode == "2":
    amount_kills_for_colorYellow = 2
    amount_kills_for_colorOrange = 5
    amount_kills_for_colorRed = 10

def kill_count_p1():
    global colour_p1
    kills_p1.set(kills_p1.get()+1)
    if kills_p1.get() >= amount_kills_for_colorYellow:
        colour_p1 = "Yellow"
        Label(master, textvariable=kills_p1, bg=colour_p1, font=("Courier", 20)).grid(column = 4, row=2)
    if kills_p1.get() >= amount_kills_for_colorOrange:
        colour_p1 = "Orange"
        Label(master, textvariable=kills_p1, bg=colour_p1, font=("Courier", 20)).grid(column = 4, row=2)
    if kills_p1.get() >= amount_kills_for_colorRed:
        colour_p1 = "Red"
        Label(master, textvariable=kills_p1, bg=colour_p1, font=("Courier", 20)).grid(column = 4, row=2)
def kill_count_p2():
    global colour_p2
    kills_p2.set(kills_p2.get()+1)
    if kills_p2.get() >= amount_kills_for_colorYellow:
        colour_p2 = "Yellow"
        Label(master, textvariable=kills_p2, bg=colour_p2, font=("Courier", 20)).grid(column = 4, row=3)
    if kills_p2.get() >= amount_kills_for_colorOrange:
        colour_p2 = "Orange"
        Label(master, textvariable=kills_p2, bg=colour_p2, font=("Courier", 20)).grid(column = 4, row=3)
    if kills_p2.get() >= amount_kills_for_colorRed:
        colour_p2 = "Red"
        Label(master, textvariable=kills_p2, bg=colour_p2, font=("Courier", 20)).grid(column = 4, row=3)
def kill_count_p3():
    global colour_p3
    kills_p3.set(kills_p3.get()+1)
    if kills_p3.get() >= amount_kills_for_colorYellow:
        colour_p3 = "Yellow"
        Label(master, textvariable=kills_p3, bg=colour_p3, font=("Courier", 20)).grid(column = 4, row=4)
    if kills_p3.get() >= amount_kills_for_colorOrange:
        colour_p3 = "Orange"
        Label(master, textvariable=kills_p3, bg=colour_p3, font=("Courier", 20)).grid(column = 4, row=4)
    if kills_p3.get() >= amount_kills_for_colorRed:
        colour_p3 = "Red"
        Label(master, textvariable=kills_p3, bg=colour_p3, font=("Courier", 20)).grid(column = 4, row=4)
def kill_count_p4():
    global colour_p4
    kills_p4.set(kills_p4.get()+1)
    if kills_p4.get() >= amount_kills_for_colorYellow:
        colour_p4 = "Yellow"
        Label(master, textvariable=kills_p4, bg=colour_p4, font=("Courier", 20)).grid(column = 4, row=5)
    if kills_p4.get() >= amount_kills_for_colorOrange:
        colour_p4 = "Orange"
        Label(master, textvariable=kills_p4, bg=colour_p4, font=("Courier", 20)).grid(column = 4, row=5)
    if kills_p4.get() >= amount_kills_for_colorRed:
        colour_p4 = "Red"
        Label(master, textvariable=kills_p4, bg=colour_p4, font=("Courier", 20)).grid(column = 4, row=5)
def kill_count_p5():
    global colour_p5
    kills_p5.set(kills_p5.get()+1)
    if kills_p5.get() >= amount_kills_for_colorYellow:
        colour_p5 = "Yellow"
        Label(master, textvariable=kills_p5, bg=colour_p5, font=("Courier", 20)).grid(column = 4, row=6)
    if kills_p5.get() >= amount_kills_for_colorOrange:
        colour_p5 = "Orange"
        Label(master, textvariable=kills_p5, bg=colour_p5, font=("Courier", 20)).grid(column = 4, row=6)
    if kills_p5.get() >= amount_kills_for_colorRed:
        colour_p5 = "Red"
        Label(master, textvariable=kills_p5, bg=colour_p5, font=("Courier", 20)).grid(column = 4, row=6)
def kill_count_p6():
    global colour_p6
    kills_p6.set(kills_p6.get()+1)
    if kills_p6.get() >= amount_kills_for_colorYellow:
        colour_p6 = "Yellow"
        Label(master, textvariable=kills_p6, bg=colour_p6, font=("Courier", 20)).grid(column = 4, row=7)
    if kills_p6.get() >= amount_kills_for_colorOrange:
        colour_p6 = "Orange"
        Label(master, textvariable=kills_p6, bg=colour_p6, font=("Courier", 20)).grid(column = 4, row=7)
    if kills_p6.get() >= amount_kills_for_colorRed:
        colour_p6 = "Red"
        Label(master, textvariable=kills_p6, bg=colour_p6, font=("Courier", 20)).grid(column = 4, row=7)
def kill_count_p7():
    global colour_p7
    kills_p7.set(kills_p7.get()+1)
    if kills_p7.get() >= amount_kills_for_colorYellow:
        colour_p7 = "Yellow"
        Label(master, textvariable=kills_p7, bg=colour_p7, font=("Courier", 20)).grid(column = 4, row=8)
    if kills_p7.get() >= amount_kills_for_colorOrange:
        colour_p7 = "Orange"
        Label(master, textvariable=kills_p7, bg=colour_p7, font=("Courier", 20)).grid(column = 4, row=8)
    if kills_p7.get() >= amount_kills_for_colorRed:
        colour_p7 = "Red"
        Label(master, textvariable=kills_p7, bg=colour_p7, font=("Courier", 20)).grid(column = 4, row=8)

#death-stuff team 1
if gamemode == "1":
    deaths_p1 = StringVar()
    deaths_p1.set("No")
    deaths_p2 = StringVar()
    deaths_p2.set("No")
    deaths_p3 = StringVar()
    deaths_p3.set("No")
    deaths_p4 = StringVar()
    deaths_p4.set("No")
    deaths_p5 = StringVar()
    deaths_p5.set("No")
    deaths_p6 = StringVar()
    deaths_p6.set("No")
    deaths_p7 = StringVar()
    deaths_p7.set("No")
elif gamemode == "2":
    deaths_p1 = IntVar()
    deaths_p1.set(0)
    deaths_p2 = IntVar()
    deaths_p2.set(0)
    deaths_p3 = IntVar()
    deaths_p3.set(0)
    deaths_p4 = IntVar()
    deaths_p4.set(0)
    deaths_p5 = IntVar()
    deaths_p5.set(0)
    deaths_p6 = IntVar()
    deaths_p6.set(0)
    deaths_p7 = IntVar()
    deaths_p7.set(0)

def death_count_p1():
    global deaths_p1
    if gamemode == "1":
        deaths_p1.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=2)
    elif gamemode == "2":
        deaths_p1.set(deaths_p1.get()+1)
def death_count_p2():
    global deaths_p2
    if gamemode == "1":
        deaths_p2.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=3)
    elif gamemode == "2":
        deaths_p2.set(deaths_p2.get()+1)
def death_count_p3():
    global deaths_p3
    if gamemode == "1":
        deaths_p3.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=4)
    elif gamemode == "2":
        deaths_p3.set(deaths_p3.get()+1)
def death_count_p4():
    global deaths_p4
    if gamemode == "1":
        deaths_p4.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=5)
    elif gamemode == "2":
        deaths_p4.set(deaths_p4.get()+1)
def death_count_p5():
    global deaths_p5
    if gamemode == "1":
        deaths_p5.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=6)
    elif gamemode == "2":
        deaths_p5.set(deaths_p5.get()+1)
def death_count_p6():
    global deaths_p6
    if gamemode == "1":
        deaths_p6.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=7)                                               
    elif gamemode == "2":
        deaths_p6.set(deaths_p6.get()+1)
def death_count_p7():
    global deaths_p7
    if gamemode == "1":
        deaths_p7.set("Yes")
        Label(text="         ", font=("Courier", 25)).grid(column=10, row=8)                                               
    elif gamemode == "2":
        deaths_p7.set(deaths_p7.get()+1)
#main labels team 1
Label(master, text="Team 1", font=("Courier", 40)).grid(row=0, columnspan=2)
Label(master, text="NAME", font=("Courier", 25)).grid(row=1)
Label(master, text="RANK", font=("Courier", 25)).grid(row=1, column=2)
Label(master, text="KILLS", font=("Courier", 25)).grid(column=4, row=1)
Label(master, text="kill-buttons", font=("Courier", 22)).grid(column=6, row=1)
if gamemode == "1":
    Label(master, text="DEAD?", font=("Courier", 25)).grid(column=8, row=1)
elif gamemode == "2":
    Label(master, text="DEATHS", font=("Courier", 25)).grid(column=8, row=1)
else:
    Label(master, text="DEAD?", font=("Courier", 25)).grid(column=8, row=1)

Label(master, text="death-buttons", font=("Courier", 22)).grid(column=10, row=1)

#player names labels team 1
Label(master, text=player1, font=("Courier", 20)).grid(row=2)
Label(master, text=player2, font=("Courier", 20)).grid(row=3)
Label(master, text=player3, font=("Courier", 20)).grid(row=4)
Label(master, text=player4, font=("Courier", 20)).grid(row=5)
Label(master, text=player5, font=("Courier", 20)).grid(row=6)
Label(master, text=player6, font=("Courier", 20)).grid(row=7)
Label(master, text=player7, font=("Courier", 20)).grid(row=8)

#rank labels team 1
Label(master, text=rank_p1, background = "Red", font=("Courier", 20)).grid(row=2, column=2)
Label(master, text=rank_p2, background = "Red", font=("Courier", 20)).grid(row=3, column=2)
Label(master, text=rank_p3, background = "Red", font=("Courier", 20)).grid(row=4, column=2)
Label(master, text=rank_p4, background = "Red", font=("Courier", 20)).grid(row=5, column=2)
Label(master, text=rank_p5, background = "Green", font=("Courier", 20)).grid(row=6, column=2)
Label(master, text=rank_p6, background = "Green", font=("Courier", 20)).grid(row=7, column=2)
Label(master, text=rank_p7, background = "deep sky blue", font=("Courier", 20)).grid(row=8, column=2)


#kills labels team 1
Label(master, textvariable=kills_p1, font=("Courier", 20)).grid(column = 4, row=2)
Label(master, textvariable=kills_p2, font=("Courier", 20)).grid(column = 4, row=3)
Label(master, textvariable=kills_p3, font=("Courier", 20)).grid(column = 4, row=4)
Label(master, textvariable=kills_p4, font=("Courier", 20)).grid(column = 4, row=5)
Label(master, textvariable=kills_p5, font=("Courier", 20)).grid(column = 4, row=6)
Label(master, textvariable=kills_p6, font=("Courier", 20)).grid(column = 4, row=7)
Label(master, textvariable=kills_p7, font=("Courier", 20)).grid(column = 4, row=8)

#deaths labels team 1
def one_life_gamemode():
    global deaths_p1
    Label(master, textvariable=deaths_p1, font=("Courier", 20)).grid(column = 8, row=2)
    Label(master, textvariable=deaths_p2, font=("Courier", 20)).grid(column = 8, row=3)
    Label(master, textvariable=deaths_p3, font=("Courier", 20)).grid(column = 8, row=4)
    Label(master, textvariable=deaths_p4, font=("Courier", 20)).grid(column = 8, row=5)
    Label(master, textvariable=deaths_p5, font=("Courier", 20)).grid(column = 8, row=6)
    Label(master, textvariable=deaths_p6, font=("Courier", 20)).grid(column = 8, row=7)
    Label(master, textvariable=deaths_p7, font=("Courier", 20)).grid(column = 8, row=8)
    
def respawn_gamemode():
    Label(master, textvariable=deaths_p1, font=("Courier", 20)).grid(column = 8, row=2)
    Label(master, textvariable=deaths_p2, font=("Courier", 20)).grid(column = 8, row=3)
    Label(master, textvariable=deaths_p3, font=("Courier", 20)).grid(column = 8, row=4)
    Label(master, textvariable=deaths_p4, font=("Courier", 20)).grid(column = 8, row=5)
    Label(master, textvariable=deaths_p5, font=("Courier", 20)).grid(column = 8, row=6)
    Label(master, textvariable=deaths_p6, font=("Courier", 20)).grid(column = 8, row=7)
    Label(master, textvariable=deaths_p7, font=("Courier", 20)).grid(column = 8, row=8)

if gamemode == "1":
    one_life_gamemode()
elif gamemode == "2":
    respawn_gamemode()


#seperators team 1
tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=1, row=1, rowspan=8, sticky='ns')
tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=3, row=1, rowspan=8, sticky='ns')
tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=5, row=1, rowspan=8, sticky='ns')
tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=7, row=1, rowspan=8, sticky='ns')
tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=9, row=1, rowspan=8, sticky='ns')

#kill buttons team 1
Button(master, text="p1: add kill", font=("Courier", 20), command=kill_count_p1).grid(column=6, row=2)
Button(master, text="p2: add kill", font=("Courier", 20), command=kill_count_p2).grid(column=6, row=3)
Button(master, text="p3: add kill", font=("Courier", 20), command=kill_count_p3).grid(column=6, row=4)
Button(master, text="p4: add kill", font=("Courier", 20), command=kill_count_p4).grid(column=6, row=5)
Button(master, text="p5: add kill", font=("Courier", 20), command=kill_count_p5).grid(column=6, row=6)
Button(master, text="p6: add kill", font=("Courier", 20), command=kill_count_p6).grid(column=6, row=7)
Button(master, text="p7: add kill", font=("Courier", 20), command=kill_count_p7).grid(column=6, row=8)

if gamemode == "1":
    Button(master, text="p1: dead", font=("Courier", 20), command=death_count_p1).grid(column=10, row=2)
    Button(master, text="p2: dead", font=("Courier", 20), command=death_count_p2).grid(column=10, row=3)
    Button(master, text="p3: dead", font=("Courier", 20), command=death_count_p3).grid(column=10, row=4)
    Button(master, text="p4: dead", font=("Courier", 20), command=death_count_p4).grid(column=10, row=5)
    Button(master, text="p5: dead", font=("Courier", 20), command=death_count_p5).grid(column=10, row=6)
    Button(master, text="p6: dead", font=("Courier", 20), command=death_count_p6).grid(column=10, row=7)
    Button(master, text="p7: dead", font=("Courier", 20), command=death_count_p7).grid(column=10, row=8)
elif gamemode == "2":
    Button(master, text="p1: add death", font=("Courier", 20), command=death_count_p1).grid(column=10, row=2)
    Button(master, text="p2: add death", font=("Courier", 20), command=death_count_p2).grid(column=10, row=3)
    Button(master, text="p3: add death", font=("Courier", 20), command=death_count_p3).grid(column=10, row=4)
    Button(master, text="p4: add death", font=("Courier", 20), command=death_count_p4).grid(column=10, row=5)
    Button(master, text="p5: add death", font=("Courier", 20), command=death_count_p5).grid(column=10, row=6)
    Button(master, text="p6: add death", font=("Courier", 20), command=death_count_p6).grid(column=10, row=7)
    Button(master, text="p7: add death", font=("Courier", 20), command=death_count_p7).grid(column=10, row=8)
    
