"""
Written by Sebastian
"""
import time
import json
from pprint import pprint

class tracker:
    def gamemode(self):
        gamemode_input = input("What gamemode were you playing? \n 1.Ladder Play \n 2.Ladder Competitive Play \n 3.Constructed \n 4.Competitive Constructed \n")
        if gamemode_input == '1':
            var=input("Did you win? \n y/n: ")
            if var=='y':
                self.gamemode='ladderPlayWin'
                self.winrate()
            elif var=='n':
                self.gamemode='ladderPlayLoss'
                self.winrate()
        elif gamemode_input == 2:
            self.gamemode='ladderCompetitivePlay'
        elif gamemode_input == 3:
            self.gamemode='constructed'
        elif gamemode_input == 4:
            self.gamemode='competitiveConstructed'

        
    def winrate(self):
        with open('text.json','r+') as f:
            data = json.load(f)
            var=data[self.gamemode]
            data[self.gamemode]+=1
            f.seek(0)
            
            json.dump(data,f)
            




        
            
        #pprint(data['ladderPlay'])
        

                
                

            
        

c=tracker()
c.gamemode()
