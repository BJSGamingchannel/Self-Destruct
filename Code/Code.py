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
    MasterWindow.geometry("1920x1080")
  
    def UserName():

        global StoredName        
        Canvas(MasterWindow, width=1920, height=1080, bg = "snow").place(x = 0, y = 0)
        StoredName = StringVar()
        NameLabel = Label(text = "Please enter your name", bg = "snow", font = font2)
        NameLabel.pack()
        NameEntryBox = Entry(bd = 4, textvariable = StoredName, bg = "snow", font = font2)
        NameEntryBox.pack()
        ButtonName = Button(text = "Continue", font = font2, bg = "snow", command = ChangeThis)
        ButtonName.pack()

    def ChangeThis():

        label1 = Label(text = StoredName, bg = "snow", font = font2)
        label1.pack()
        
    def Menu(): #The first window the user sees.

        Canvas(width = 1920, height = 1080, bg = "snow").place(x = 0, y = 0)
        TitleMain = Label(MasterWindow, text = "Self Destruct", font = font1, fg = "deep sky blue", bg = "snow").place( x = 845, y = 1)
        ButtonStart = Button(MasterWindow, text = "Start", font = font2, fg = "deep sky blue", bg = "snow", command = UserName).place( x = 909, y = 60)
        ButtonExit = Button(MasterWindow, text ="Exit", font = font2, fg = "deep sky blue", bg = "snow", command = exit).place( x = 915, y = 130)

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
