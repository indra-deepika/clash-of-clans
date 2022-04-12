from colorama import Fore, Back, Style
import time
class Building():
     def __init__(self,color,health,x,y):
         self.color = color
         self.health = health
         self.x = x
         self.y = y
         self.nearest = 1000000

class Townhall(Building):
    def __init__(self,color,health,x,y):
        super().__init__(color,health,x,y)
class Wall(Building):
    def __init__(self,color,health,x,y):
        super().__init__(color,health,x,y)
class Hut(Building):
    def __init__(self,color,health,x,y):
        super().__init__(color,health,x,y,)

class Cannon(Building):
    def __init__(self,color,health,x,y,range,damage):
        super().__init__(color,health,x,y)
        self.range = range
        self.damage = damage
    def cannon_attack(self,king,king_dead,h):

             if (king.health > 0 and ((king.x[0]-h.x[0])**2 + (king.y[0]-h.y[0])**2 ) < h.range**2 ) :
                 king.health = king.health - h.damage
                #  h.color = Back.WHITE+' '+Style.RESET_ALL
            
                 if king.health <=0 :
                            del king.x[:]
                            del king.y[:]
                            king_dead = 1

                 return
             elif king.health <=0 :
                     king_dead = 1
                     return

class WizardTower(Building):
    def __init__(self,color,health,x,y,range,damage):
        super().__init__(color,health,x,y)
        self.range = range
        self.damage = damage
    
    

    def wizardtower_attack_near(self,wizardtower,nearestroop,index,king,archer,balloon,barb):

        print("entered")
        if nearestroop == "k":
            if king.health  > 0 :
               print("Decreasing king health by wiz")
               king.health = king.health - wizardtower.damage       

               for h in archer:
                  for i in h.x:
                    for j in h.y:
                        if(i <= king.x[0]+1 and i >=king.x[0]-1 and j <= king.y[0]+1 and j >=king.y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                archer.remove(h)
               for h in balloon:
                  for i in h.x:
                    for j in h.y:
                        if(i <= king.x[0]+1 and i >=king.x[0]-1 and j <= king.y[0]+1 and j >=king.y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                balloon.remove(h)
               for h in barb:
                  for i in h.x:
                    for j in h.y:
                        if(i <= king.x[0]+1 and i >=king.x[0]-1 and j <= king.y[0]+1 and j >=king.y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                barb.remove(h)
            else : 
                 del king.x[:]
                 del king.y[:]
                 self.nearest = 1000000


        if nearestroop == "a":
            if archer[index].health  > 0 :
               print("Decreasing arch health by wiz ")
               archer[index].health = archer[index].health - wizardtower.damage

               for i in king.x:
                   for j in king.y:
                        if(i <= archer[index].x[0]+1 and i >=archer[index].x[0]-1 and j <= archer[index].y[0]+1 and j >=archer[index].y[0]-1):
                            king.health =  king.health - wizardtower.damage
                            if king.health <=0:
                                 del king.x[:]
                                 del king.y[:]
                
               for h in balloon:
                  for i in h.x:
                    for j in h.y:
                        if(i <= archer[index].x[0]+1 and i >=archer[index].x[0]-1 and j <= archer[index].y[0]+1 and j >=archer[index].y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                balloon.remove(h)
               for h in barb:
                  for i in h.x:
                    for j in h.y:
                        if(i <= archer[index].x[0]+1 and i >=archer[index].x[0]-1 and j <= archer[index].y[0]+1 and j >=archer[index].y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                barb.remove(h)

            else :
                 archer.remove(archer[index])
                 self.nearest = 1000000

        if nearestroop == "b":
            if balloon[index].health  > 0 :
               print("Decreasing balllon health by wiz")
               balloon[index].health = balloon[index].health - wizardtower.damage

               for i in king.x:
                   for j in king.y:
                        if(i <= balloon[index].x[0]+1 and i >=balloon[index].x[0]-1 and j <= balloon[index].y[0]+1 and j >=balloon[index].y-1):
                            king.health =  king.health - wizardtower.damage
                            if king.health <=0:
                                 del king.x[:]
                                 del king.y[:]

               for h in archer:
                  for i in h.x:
                    for j in h.y:
                        if(i <= balloon[index].x[0]+1 and i >=balloon[index].x[0]-1 and j <= balloon[index].y[0]+1 and j >=balloon[index].y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                archer.remove(h)
                                
               for h in barb:
                  for i in h.x:
                    for j in h.y:
                        if(i <= balloon[index].x[0]+1 and i >=balloon[index].x[0]-1 and j <= balloon[index].y[0]+1 and j >=balloon[index].y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                barb.remove(h)
            else :
                 balloon.remove(balloon[index]) 
                 self.nearest = 1000000


        if nearestroop == "ba":
            if barb[index].health  > 0 :
               print("Decreasing barb health by wiz ")
               barb[index].health = barb[index].health - wizardtower.damage

               for i in king.x:
                   for j in king.y:
                        if(i <= barb[index].x[0]+1 and i>=barb[index].x-1 and j<= barb[index].y[0]+1 and j >=barb[index].y[0]-1):
                            king.health =  king.health - wizardtower.damage
                            if king.health <=0:
                                 del king.x[:]
                                 del king.y[:]

               for h in archer:
                  for i in h.x:
                    for j in h.y:
                        if(i <= barb[index].x[0]+1 and i >=barb[index].x[0]-1 and j <= barb[index].y[0]+1 and j >=barb[index].y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                archer.remove(h)

               for h in balloon:
                  for i in h.x:
                    for j in h.y:
                        if(i <= barb[index].x[0]+1 and i >=barb[index].x[0]-1 and j <= barb[index].y[0]+1 and j >=barb[index].y[0]-1):
                            h.health =  h.health - wizardtower.damage
                            if h.health <=0:
                                balloon.remove(h)
            else :
                 barb.remove(barb[index])
                 self.nearest = 1000000


    
    def wizardtower_attack(self,wizardtower,king,archer,balloon,barb):
        # check nearest
        #fix target
        # attack untill dies 
        #check nearest ..

        # king, balloon , barbs ,archers 
        self.nearest = 100000
        nearestroop = ""
        wt_x = wizardtower.x[0]
        wt_y = wizardtower.y[0]
        index = 0  
        for i in king.x:
            for j in king.y:
                if((wt_x-i)**2+ (wt_y-j)**2 < self.nearest and (wt_x-i)**2+ (wt_y-j)**2 < wizardtower.range**2 ):
                    self.nearest = (wt_x-i)**2+ (wt_y-j)**2
                    nearestroop = "k"
        
        ind = 0 
        for h in archer:
            for i in h.x:
                for j in h.y:
                  if((wt_x-i)**2+ (wt_y-j)**2 < self.nearest and (wt_x-i)**2+ (wt_y-j)**2 < wizardtower.range**2 ):
                    self.nearest = (wt_x-i)**2+ (wt_y-j)**2
                    nearestroop = "a"
                    index = ind
        ind = ind + 1

        ind = 0 
        for h in balloon:
            for i in h.x:
                for j in h.y:
                  if((wt_x-i)**2+ (wt_y-j)**2 < self.nearest  and (wt_x-i)**2+ (wt_y-j)**2 < wizardtower.range**2 ):
                    self.nearest = (wt_x-i)**2+ (wt_y-j)**2
                    nearestroop = "b"
                    index = ind
        ind = ind + 1

        ind = 0 
        for h in barb:
            for i in h.x:
                for j in h.y:
                  if((wt_x-i)**2+ (wt_y-j)**2 < self.nearest and (wt_x-i)**2+ (wt_y-j)**2 < wizardtower.range**2 ):
                    self.nearest = (wt_x-i)**2+ (wt_y-j)**2
                    self.nearestroop = "ba"
                    index = ind
        ind = ind + 1

        wizardtower.wizardtower_attack_near(wizardtower,nearestroop,index,king,archer,balloon,barb)
