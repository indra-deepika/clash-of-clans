from colorama import Fore, Back, Style 
from os import system
from src.building import *
from src.troops import *
import time
class Village():
    def __init__(self):
        self.color = Back.BLACK+' '+Style.RESET_ALL
        self.cols = 70
        self.rows = 30
        self.board = [[self.color for i in range(self.cols)] for j in range(self.rows)]
        
     
    def input_get(self,char,king):
        king.king_move(char,king)
        # print(king.x)
        # print(king.y)
     
    def render(self,char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower):
        system('clear')

        # if not hut and not cannon and not wizardtower and  not townhall.x   :
        #  print("Proceeding to level 2")
        #  return False
        
        if char == 'c':
            barb1 = Barb(Back.MAGENTA+' '+Style.RESET_ALL,100,10,[9],[24],0.005)
            barb.append(barb1)
        if char == 't':
            barb2 = Barb(Back.MAGENTA+' '+Style.RESET_ALL,100,10,[25],[56],0.005)
            barb.append(barb2)
        if char == 'f':
            barb3 = Barb(Back.MAGENTA+' '+Style.RESET_ALL,100,10,[14],[39],0.005)
            barb.append(barb3)

        if char == 'v':
            archer1 = Archer(Back.CYAN+' '+Style.RESET_ALL,50,5,[1],[24],0.01,5)
            archer.append(archer1)
        if char == 'g':
            archer2 = Archer(Back.CYAN+' '+Style.RESET_ALL,50,5,[2],[56],0.01,5)
            archer.append(archer2)
        if char == 'y':
            archer3 = Archer(Back.CYAN+' '+Style.RESET_ALL,50,5,[23],[30],0.01,5)
            archer.append(archer3)

        if char == 'b':
            balloon1 = Balloon(Back.LIGHTGREEN_EX+' '+Style.RESET_ALL,100,20,[9],[24],0.01)
            balloon.append(balloon1)
        if char == 'h':
            balloon2 = Balloon(Back.LIGHTGREEN_EX+' '+Style.RESET_ALL,100,20,[25],[56],0.01)
            balloon.append(balloon2)
        if char == 'u':
            balloon3 = Balloon(Back.LIGHTGREEN_EX+' '+Style.RESET_ALL,100,20,[14],[39],0.01)
            balloon.append(balloon3)


        if king_dead ==0:
         for h in cannon:
          h.cannon_attack(king,king_dead,h)   
     
        if king_dead ==0:
         king.king_move(char,king,wall,hut,cannon,townhall)
         

        for h in barb:
         h.barb_move(h,hut,wall,townhall)

        for h in archer:
         h.archer_movement(h,hut,wall,townhall,cannon,wizardtower)
        
        for h in balloon:
         h.balloon_move(h,hut,wall,townhall,cannon,wizardtower)
        
        for h in wizardtower:
         h.wizardtower_attack(h,king,archer,balloon,barb)
       
       

        for i in townhall.x:
            for j in townhall.y:
             self.board[i][j] =  townhall.color

        for i in king.x:
            for j in king.y:
             self.board[i][j] =  king.color

        for h in wall:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color

        for h in hut:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color
        
        for h in cannon:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color

        for h in barb:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color

        for h in archer:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color

        for h in balloon:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color
        
        for h in wizardtower:
         for i in h.x:
            for j in h.y:
             self.board[i][j] =  h.color



        self.output=("\n".join (["".join(row) for row in self.board]))
        print(self.output)

      
       
    