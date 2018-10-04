"""
Written by Sebastian Ovenden
"""
import time
import json
from pprint import pprint
from tkinter import Tk, Label, Button
class tracker:
    def gamemode(self, gamemode_input):
        if gamemode_input == '1':
            var=input("Did you win? \n y/n: ")
            if var=='y':
                self.gamemode='ladderPlayWin'
            elif var=='n':
                self.gamemode='ladderPlayLoss'
        elif gamemode_input == '2':
            var=input("Did you win? \n y/n: ")
            if var=='y':
                self.gamemode='ladderCompetitiveWin'
            elif var=='n':
                self.gamemode='ladderCompetitiveLoss'
        elif gamemode_input == '3':
            var=input("Did you win? \n y/n: ")
            if var=='y':
                self.gamemode='constructedWin'
            elif var=='n':
                self.gamemode='constructedLoss'
        elif gamemode_input == '4':
            var=input("Did you win? \n y/n: ")
            if var=='y':
                self.gamemode='competitiveConstructedWin'
            elif var=='n':
                self.gamemode='competitiveConstructedLoss'
        self.winrate()


        
    def winrate(self):
        with open('text.json','r+') as f:
            data = json.load(f)
            data[self.gamemode]+=1
            f.seek(0)
            json.dump(data,f)

    def clearScore(self):
        user_input=input("Are you sure you want to clear your stats? \n y/n: ")
        if user_input == 'y':
            with open('text.json','r+') as x:
                data1=json.load(x)
                for i in self.listOfGamemodes:
                    print(i)
                    data1[i]=0
                x.seek(0)
                json.dump(data1,x)
        else:
            print("Keep up the grind")
    def PrintScore(self):
        with open('text.json','r') as var:
            data = json.load(var)
            for x in data:
                print(x,end=': ')
                pprint(data[x])

class myFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("MTGA  Winrate Tracker")
        self.label = Label(master, text="What gamemode were you playing?")
        self.label.pack()

        self.ladderPlay=Button(master, text="Standard Ladder", command=self.findGamemode(1))
        self.ladderPlay.pack()
        self.ladderCompetitive=Button(master, text="Competitive Ladder", command=self.findGamemode(2))
        self.ladderCompetitive.pack()
        self.constructedWin=Button(master, text="Constructed Event", command=self.findGamemode(3))
        self.constructedWin.pack()
        self.constructedCompetitive=Button(master, text="Competitive Event", command=self.findGamemode(4))
        self.constructedCompetitive.pack()
    def findGamemode(self, var):
        c.gamemode(var)

        
        
        
            
        


                
                

            
        
c=tracker()
root = Tk()
y=myFirstGUI(root)
c.gamemode(var)
root.mainloop()


