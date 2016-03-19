#Welcome to Self-Destruct
#Author: BJSGamingchannel
#Programming Language: Python

#Start of program.

import tkinter as Tk
from tkinter import *
import os as OS
import random as rand
import math as M

font1 = ("Times New Roman", "20", "bold")
font2 = ("Times New Roman", "18", "bold")

def MasterFunction():
  
    MasterWindow = Tk()
    MasterWindow.geometry("1350x740")
    MasterWindow.title("Self Destruct")
    #MasterWindow.wm_iconbitmap ('C:\Users\bjsga_000\Documents\GitHub\Self-Destruct-master\Bomb.ico')#This don't work yet.
    Can1 = Canvas(MasterWindow, width=500, height=500, bg = "snow")
    TitleMain = Label(MasterWindow, text = "Self Destruct", font = font1, fg = "deep sky blue", bg = "snow")
    TitleMain.pack()
    ButtonStart = Button(MasterWindow, text = "Start", font = font2, fg = "deep sky blue", bg = "snow", command = FirstWindow)
    ButtonStart.pack()
    ButtonExit = Button(MasterWindow, text ="Exit", font = font2, g = "deep sky blue", bg = "snow", command = exit)
    ButtonExit.pack()

    def FirstWindow():
        
        Can2 = Canvas(MasterWindow, width=500. height=500, bg = "snow")
        StoredName = StringVar()
        NameEntryBox = Entry(Can2, bd = 4, textvariable = StoredName, bg = "snow")
        NameEntryBox.pack()

MasterFunction()

#The below needs to be tested / edited in Python:

Score = 0

Label(MasterWindow, text = Score, font = font1)

If Score > 10:
    Label(MasterWindow, text = "Your good at this!", (Score), font = font1)

ScoreAdd = false

If ScoreAdd = true:
    Score + 1
    Label(MasterWindow, text = Score, font = font1)
