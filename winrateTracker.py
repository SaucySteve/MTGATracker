"""
Written by Sebastian
"""
import time
import json
from pprint import pprint

class tracker:
    def gamemode(self):
        self.listOfGamemodes=['ladderPlayWin','ladderPlayLoss','ladderCompetitiveWin','ladderCompetitiveLoss','constructedWin','constructedLoss','competitiveConstructedWin','competitiveConstructedLoss']
        gamemode_input = input("What gamemode were you playing? \n 1.Ladder Play \n 2.Ladder Competitive Play \n 3.Constructed \n 4.Competitive Constructed \n")
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


                
                

            
        

c=tracker()
c.gamemode()
c.clearScore()
