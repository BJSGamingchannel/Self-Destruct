#Welcome to Self-Destruct
#Author: BJSGamingchannel
#Programming Language: Python

#Start of program.

import tkinter as Tk
from tkinter import *
import os as OS
import random as rand
import math as M
import time as time

font1 = ("Times New Roman", "30", "bold")
font2 = ("Times New Roman", "25", "bold")

def MasterFunction():

    MasterWindow = Tk()
    MasterWindow.title("Self Destruct")
    MasterWindow.geometry("1350x740")
  
    def FirstWindow():
        
        Can2 = Canvas(MasterWindow, width=500, height=500, bg = "snow")
        StoredName = StringVar()
        NameLabel = Label(Can2, text = "Please enter your name", bg = "snow")
        NameLabel.pack()
        NameEntryBox = Entry(Can2, bd = 4, textvariable = StoredName, bg = "snow")
        NameEntryBox.pack()
        
    def Menu():

        Can1 = Canvas(width = 1350, height = 740, bg = "snow")
        Can1.pack(expand = YES, fill = BOTH)
        TitleMain = Label(MasterWindow, text = "Self Destruct", font = font1, fg = "deep sky blue", bg = "snow").place( x = 570, y = 1)
        ButtonStart = Button(MasterWindow, text = "Start", font = font2, fg = "deep sky blue", bg = "snow", command = FirstWindow).place( x = 630, y = 60)
        ButtonExit = Button(MasterWindow, text ="Exit", font = font2, fg = "deep sky blue", bg = "snow", command = exit).place( x = 637, y = 130)

    Menu()

MasterFunction()

##The below needs to be tested / edited in Python:
##
##Score = 0
##
##Label(MasterWindow, text = Score, font = font1)
##
##If Score > 10:
##    Label(MasterWindow, text = "Your good at this!", (Score), font = font1)
##
##ScoreAdd = false
##
##If ScoreAdd = true:
##    Score + 1
##    Label(MasterWindow, text = Score, font = font1)
