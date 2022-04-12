from colorama import Fore, Back, Style
import time
class Troops():
    def __init__(self,color,health,damage,x,y,speed):
         self.color = color
         self.health = health
         self.damage = damage
         self.speed = speed
         self.x = x
         self.y = y
         self.prev_balloon_attack_time = 0

         
class Barb(Troops):
    def __init__(self,color,health,damage,x,y,speed):
        super().__init__(color,health,damage,x,y,speed)
    def barb_move(self,barb,hut,wall,townhall):
     pres_time = time.time()
     self.prev_barb_attack_time = 0

     if not hut:
       if not townhall.x:
       
         return
       else: 
        nearestu = 1000000
        nearestd = 1000000
        nearestl = 1000000
        nearestr = 1000000
        barb_x = barb.x[0] + 1
        barb_y = barb.y[0]
        for i in townhall.x:
              for j in townhall.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestd):
                    nearestd = (i-barb_x)**2 + (j-barb_y)**2
          
        barb_x = barb.x[0]-1         
        barb_y = barb.y[0]
        for i in townhall.x:
              for j in townhall.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestu):
                    nearestu = (i-barb_x)**2 + (j-barb_y)**2
                
        barb_x = barb.x[0] 
        barb_y = barb.y[0] - 1
        for i in townhall.x:
              for j in townhall.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestl):
                    nearestl = (i-barb_x)**2 + (j-barb_y)**2
                   
        barb_x = barb.x[0] 
        barb_y = barb.y[0] + 1
        for i in townhall.x:
              for j in townhall.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestr):
                    nearestr = (i-barb_x)**2 + (j-barb_y)**2
                    
      
        if min(nearestd,nearestl,nearestr,nearestu) == nearestd:
          flag1 = 0 
          if nearestd != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:    
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0]+1 == i and barb.y[0] == j:
                 h.health = h.health - barb.damage
                 if h.health <= 0:
                  wall.remove(h)
                 return
            self.prev_barb_attack_time = time.time()
            barb.x[0] = barb.x[0]+1
               
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestu:
          if nearestu != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0]-1 == i and barb.y[0] == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                  wall.remove(h)
                return
            self.prev_barb_attack_time = time.time()  
            barb.x[0] = barb.x[0]-1
           
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestl:
          if nearestl != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0] == i and barb.y[0]-1 == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                 wall.remove(h)
                return
            self.prev_barb_attack_time = time.time() 
            barb.y[0] = barb.y[0]-1
                
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestr:
          if nearestr != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0] == i and barb.y[0]+1 == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                   wall.remove(h)
                return
            self.prev_barb_attack_time = time.time()
            barb.y[0] = barb.y[0]+1
        nearest = 1000000
        if min(nearestd,nearestl,nearestr,nearestu) == 0: 
    
          barb_x = barb.x[0]
          barb_y = barb.y[0]  
          for i in townhall.x:
              for j in townhall.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 == 1):
                       townhall.health = townhall.health - barb.damage
                       if townhall.health == 0:
                            del townhall.x[:]
                            del townhall.y[:]
 

     else :
       
        ind = 0 
        nearestu = 1000000
        nearestd = 1000000
        nearestl = 1000000
        nearestr = 1000000
        barb_x = barb.x[0] + 1
        barb_y = barb.y[0]
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestd):
                    nearestd = (i-barb_x)**2 + (j-barb_y)**2
          
        barb_x = barb.x[0]-1         
        barb_y = barb.y[0]
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestu):
                    nearestu = (i-barb_x)**2 + (j-barb_y)**2
                
        barb_x = barb.x[0] 
        barb_y = barb.y[0] - 1
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestl):
                    nearestl = (i-barb_x)**2 + (j-barb_y)**2
                   
        barb_x = barb.x[0] 
        barb_y = barb.y[0] + 1
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 < nearestr):
                    nearestr = (i-barb_x)**2 + (j-barb_y)**2
                    
        nearest = 1000000
        if min(nearestd,nearestl,nearestr,nearestu) == 0: 
          barb_x = barb.x[0]
          barb_y = barb.y[0]  
          for h in hut:
           for i in h.x:
              for j in h.y:
                  if((i-barb_x)**2 + (j-barb_y)**2 == 1):
                       h.health = h.health - barb.damage
                       if h.health <= 0:
                         hut.remove(h)
        if min(nearestd,nearestl,nearestr,nearestu) == nearestd:
          if nearestd != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0]+1 == i and barb.y[0] == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                   wall.remove(h)
                return
           self.prev_barb_attack_time = time.time()
           barb.x[0] = barb.x[0]+1
              
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestu:
          if nearestu != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0]-1 == i and barb.y[0] == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                  wall.remove(h)
                return
            self.prev_barb_attack_time = time.time()  
            barb.x[0] = barb.x[0]-1

        elif min(nearestd,nearestl,nearestr,nearestu) == nearestl:
          if nearestl != 0:  
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0] == i and barb.y[0]-1 == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                 wall.remove(h)
                return
            self.prev_barb_attack_time = time.time()
            barb.y[0] = barb.y[0]-1
              
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestr:
          if nearestr != 0:
           if pres_time - self.prev_barb_attack_time > barb.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if barb.x[0] == i and barb.y[0]+1 == j:
                h.health = h.health - barb.damage
                if h.health <= 0:
                   wall.remove(h)
                return
            self.prev_barb_attack_time = time.time()
            barb.y[0] = barb.y[0]+1
                    

class King(Troops):
    def __init__(self,color,health,damage,x,y,avatar,speed):
        super().__init__(color,health,damage,x,y,speed)
        self.avatar = avatar
        self.press_time =0 
        self.high_aoe = 0

    def king_move(self,char,king,wall,hut,cannon,townhall):
      
      try:
        if(char=="w"):
            self.king_prev_move = char
            flag=0
            for h in wall:
                for i in h.x:
                   for j in h.y:
                      if king.x[0]-1 == i and king.y[0] == j:
                        flag=1 
            for h in hut:
                for i in h.x:
                   for j in h.y:
                      if king.x[0]-1 == i and king.y[0] == j:
                        flag=1 
            for h in cannon:
                for i in h.x:
                   for j in h.y:
                      if king.x[0]-1 == i and king.y[0] == j:
                        flag=1 

            for i in townhall.x:
                   for j in townhall.y:
                      if king.x[0]-1 == i and king.y[0] == j:
                        flag=1 
            if flag == 0 :
                king.x[0] = king.x[0]-1

        if(char=="s"):
            self.king_prev_move = char
            flag=0
            for h in wall:
                for i in h.x:
                   for j in h.y:
                      if king.x[0]+1 == i and king.y[0] == j:
                        flag=1 
            for h in hut:
                for i in h.x:
                   for j in h.y:
                      if king.x[0]+1 == i and king.y[0] == j:
                        flag=1  
            for h in cannon:
                for i in h.x:
                   for j in h.y:
                      if king.x[0]+1 == i and king.y[0] == j:
                        flag=1  
            for i in townhall.x:
                for j in townhall.y:
                      if king.x[0]+1 == i and king.y[0] == j:
                        flag=1 
                        
                        
            if flag == 0 :
                king.x[0] = king.x[0]+1
          
        if(char=="a"):
            self.king_prev_move = char
            flag=0
            for h in wall:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        flag=1 
            for h in hut:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        flag=1 
            for h in cannon:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        flag=1 
            for i in townhall.x:
                for j in townhall.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        flag=1 
            if flag == 0 :
                king.y[0] = king.y[0]-1
    
        if(char=="d"):
          self.king_prev_move = char
          flag=0
          for h in wall:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]+1 == j:
                        flag=1 
          for h in hut:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]+1 == j:
                        flag=1 
          for h in cannon:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]+1 == j:
                        flag=1 
          for i in townhall.x:
                for j in townhall.y:
                      if king.x[0] == i and king.y[0]+1 == j:
                        flag=1 
          if flag == 0 :
                king.y[0] = king.y[0]+1

        if(char==" "):
        #  print(king.avatar)
         if king.avatar == 'k':
            for i in townhall.x:
                for j in townhall.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        if townhall.health > 0 :
                         townhall.health = townhall.health - king.damage
                        else:
                            del townhall.x[:]
                            del townhall.y[:]
                      if king.x[0] == i and king.y[0]+1== j:
                        if townhall.health > 0 :
                         townhall.health = townhall.health - king.damage
                        else:
                            del townhall.x[:]
                            del townhall.y[:]
                      if king.x[0]-1 == i and king.y[0] == j:
                        if townhall.health > 0 :  
                         townhall.health = townhall.health - king.damage
                        else:
                            del townhall.x[:]
                            del townhall.y[:]
                      if king.x[0]+1 == i and king.y[0] == j:
                        if townhall.health > 0 :
                         townhall.health = townhall.health - king.damage
                        else:
                            del townhall.x[:]
                            del townhall.y[:]
            for h in cannon:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            cannon.remove(h)
                      if king.x[0] == i and king.y[0]+1== j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            cannon.remove(h)
                      if king.x[0]-1 == i and king.y[0] == j:
                        if h.health > 0 :  
                         h.health = h.health - king.damage
                        else:
                            cannon.remove(h)
                      if king.x[0]+1 == i and king.y[0] == j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            cannon.remove(h)

            for h in wall:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            wall.remove(h)
                      if king.x[0] == i and king.y[0]+1== j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            wall.remove(h)
                      if king.x[0]-1 == i and king.y[0] == j:
                        if h.health > 0 :  
                         h.health = h.health - king.damage
                        else:
                            wall.remove(h)
                      if king.x[0]+1 == i and king.y[0] == j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            wall.remove(h)
            for h in hut:
                for i in h.x:
                   for j in h.y:
                      if king.x[0] == i and king.y[0]-1 == j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            hut.remove(h)
                      if king.x[0] == i and king.y[0]+1== j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            hut.remove(h)
                      if king.x[0]-1 == i and king.y[0] == j:
                        if h.health > 0 :  
                         h.health = h.health - king.damage
                        else:
                            hut.remove(h)
                      if king.x[0]+1 == i and king.y[0] == j:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                          hut.remove(h)

         elif king.avatar == 'j':
          #  print("inside ")
           print(self.king_prev_move)
           self.centre_x = king.x[0] 
           self.centre_y = king.y[0]

           if self.king_prev_move == "w":
            self.centre_x = self.centre_x - 8
           if self.king_prev_move == "s":
            self.centre_x = self.centre_x + 8
           if self.king_prev_move == "a":
            self.centre_y = self.centre_y - 8
           if self.king_prev_move == "d":
            self.centre_y = self.centre_y + 8

           for h in hut:
              for i in h.x:
                   for j in h.y:
                     if i<=self.centre_x+2 and i >= self.centre_x-2 and j <= self.centre_y+2 and j >= self.centre_y-2:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            hut.remove(h)
           for h in cannon:
              for i in h.x:
                   for j in h.y:
                     if i<=self.centre_x+2 and i >= self.centre_x-2 and j <= self.centre_y+2 and j >= self.centre_y-2:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            cannon.remove(h)
           for h in wall:
              for i in h.x:
                   for j in h.y:
                     if i<=self.centre_x+2 and i >= self.centre_x-2 and j <= self.centre_y+2 and j >= self.centre_y-2:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            wall.remove(h)
           for i in townhall.x:
               for j in townhall.y:
                     if i<=self.centre_x+2 and i >= self.centre_x-2 and j <= self.centre_y+2 and j >= self.centre_y-2:
                        if townhall.health > 0 :
                         townhall.health = townhall.health - king.damage

                        else:
                            del townhall.x[:]
                            del townhall.y[:]


          
        if char == "i": 
           time.sleep(1)
          #  print(self.king_prev_move)
           self.centre_x = king.x[0] 
           self.centre_y = king.y[0]

           if self.king_prev_move == "w":
            self.centre_x = self.centre_x - 16
           if self.king_prev_move == "s":
            self.centre_x = self.centre_x + 16
           if self.king_prev_move == "a":
            self.centre_y = self.centre_y - 16
           if self.king_prev_move == "d":
            self.centre_y = self.centre_y + 16

           for h in hut:
              for i in h.x:
                   for j in h.y:
                     if i<=self.centre_x+4 and i >= self.centre_x-4 and j <= self.centre_y+4 and j >= self.centre_y-4:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            hut.remove(h)
           for h in cannon:
              for i in h.x:
                   for j in h.y:
                     if i<=self.centre_x+4 and i >= self.centre_x-4 and j <= self.centre_y+4 and j >= self.centre_y-4:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            cannon.remove(h)
           for h in wall:
              for i in h.x:
                   for j in h.y:
                     if i<=self.centre_x+4 and i >= self.centre_x-4 and j <= self.centre_y+4 and j >= self.centre_y-4:
                        if h.health > 0 :
                         h.health = h.health - king.damage
                        else:
                            wall.remove(h)
           for i in townhall.x:
               for j in townhall.y:
                     if i<=self.centre_x+4 and i >= self.centre_x-4 and j <= self.centre_y+4 and j >= self.centre_y-4:
                        if townhall.health > 0 :
                         townhall.health = townhall.health - king.damage

                        else:
                            del townhall.x[:]
                            del townhall.y[:]

      except:
       pass

class Balloon(Troops):
  def __init__(self,color,health,damage,x,y,speed):
        super().__init__(color,health,damage,x,y,speed)
     
  def balloon_move(self,balloon,hut,wall,townhall,cannon, wizardtower):

    pres_time = time.time()
    if not cannon and not wizardtower : #and wizard tower
      if not townhall.x and not hut: #huts and townhall
         return
      else: 
     
       if hut:
        nearestu = 1000000
        nearestd = 1000000
        nearestl = 1000000
        nearestr = 1000000

        balloon_x = balloon.x[0] + 1
        balloon_y = balloon.y[0]

        for h in hut:
           for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestd):
                    nearestd = (i-balloon_x)**2 + (j-balloon_y)**2
          
        balloon_x = balloon.x[0]-1         
        balloon_y = balloon.y[0]
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestu):
                    nearestu = (i-balloon_x)**2 + (j-balloon_y)**2
                
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] - 1
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestl):
                    nearestl = (i-balloon_x)**2 + (j-balloon_y)**2
                   
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] + 1
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestr):
                    nearestr = (i-balloon_x)**2 + (j-balloon_y)**2
                    
      
        if min(nearestd,nearestl,nearestr,nearestu) == nearestd:
          flag1 = 0 
          if nearestd != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:    
            self.prev_balloon_attack_time = time.time()
            balloon.x[0] = balloon.x[0]+1
               
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestu:
          if nearestu != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()  
            balloon.x[0] = balloon.x[0]-1
           
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestl:
          if nearestl != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time() 
            balloon.y[0] = balloon.y[0]-1
                
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestr:
          if nearestr != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()
            balloon.y[0] = balloon.y[0]+1
        nearest = 1000000
        if min(nearestd,nearestl,nearestr,nearestu) == 0: 
          balloon_x = balloon.x[0]
          balloon_y = balloon.y[0] 
          for h in hut: 
            for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 == 1):
                       h.health = h.health - balloon.damage
                       if h.health <= 0:
                            hut.remove(h)

       elif townhall.x: #if townhall is there
        nearestu = 1000000
        nearestd = 1000000
        nearestl = 1000000
        nearestr = 1000000

        balloon_x = balloon.x[0] + 1
        balloon_y = balloon.y[0]
        for i in townhall.x:
              for j in townhall.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestd):
                    nearestd = (i-balloon_x)**2 + (j-balloon_y)**2
          
        balloon_x = balloon.x[0]-1         
        balloon_y = balloon.y[0]
        for i in townhall.x:
              for j in townhall.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestu):
                    nearestu = (i-balloon_x)**2 + (j-balloon_y)**2
                
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] - 1
        for i in townhall.x:
              for j in townhall.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestl):
                    nearestl = (i-balloon_x)**2 + (j-balloon_y)**2
                   
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] + 1
        for i in townhall.x:
              for j in townhall.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestr):
                    nearestr = (i-balloon_x)**2 + (j-balloon_y)**2

        # print(nearestd)
        # print(nearestl)
        # print(nearestr)
        # print(nearestu)
        nearest = 1000000
        if min(nearestd,nearestl,nearestr,nearestu) == 0: 
    
          if nearestd == 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:    
            self.prev_balloon_attack_time = time.time()
            balloon.x[0] = balloon.x[0]+1
          if nearestu == 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()  
            balloon.x[0] = balloon.x[0]-1
          if nearestl == 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time() 
            balloon.y[0] = balloon.y[0]-1
          if nearestr == 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()
            balloon.y[0] = balloon.y[0]+1
                

          balloon_x = balloon.x[0]
          balloon_y = balloon.y[0]  
          for i in townhall.x:
              for j in townhall.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 == 0):
                       townhall.health = townhall.health - balloon.damage
                       if townhall.health == 0:
                            del townhall.x[:]
                            del townhall.y[:]
          return

        elif min(nearestd,nearestl,nearestr,nearestu) == nearestd:
          flag1 = 0 
          if nearestd != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:    
            self.prev_balloon_attack_time = time.time()
            balloon.x[0] = balloon.x[0]+1
               
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestu:
          if nearestu != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()  
            balloon.x[0] = balloon.x[0]-1
           
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestl:
          if nearestl != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time() 
            balloon.y[0] = balloon.y[0]-1
                
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestr:
          if nearestr != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()
            balloon.y[0] = balloon.y[0]+1
        

    else :
     
        ind = 0 
        nearestu = 1000000
        nearestd = 1000000
        nearestl = 1000000
        nearestr = 1000000
        balloon_x = balloon.x[0] + 1
        balloon_y = balloon.y[0]
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestd):
                    nearestd = (i-balloon_x)**2 + (j-balloon_y)**2
          
        balloon_x = balloon.x[0]-1         
        balloon_y = balloon.y[0]
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestu):
                    nearestu = (i-balloon_x)**2 + (j-balloon_y)**2
                
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] - 1
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestl):
                    nearestl = (i-balloon_x)**2 + (j-balloon_y)**2
                   
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] + 1
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestr):
                    nearestr = (i-balloon_x)**2 + (j-balloon_y)**2
        
        balloon_x = balloon.x[0] + 1
        balloon_y = balloon.y[0]
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestd):
                    nearestd = (i-balloon_x)**2 + (j-balloon_y)**2
          
        balloon_x = balloon.x[0]-1         
        balloon_y = balloon.y[0]
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestu):
                    nearestu = (i-balloon_x)**2 + (j-balloon_y)**2
                
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] - 1
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestl):
                    nearestl = (i-balloon_x)**2 + (j-balloon_y)**2
                   
        balloon_x = balloon.x[0] 
        balloon_y = balloon.y[0] + 1
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 < nearestr):
                    nearestr = (i-balloon_x)**2 + (j-balloon_y)**2
                    
                    
        nearest = 1000000
        if min(nearestd,nearestl,nearestr,nearestu) == 0: 
          balloon_x = balloon.x[0]
          balloon_y = balloon.y[0]  
          for h in cannon:
           for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 == 1):
                       h.health = h.health - balloon.damage
                       if h.health <= 0:
                         cannon.remove(h)
          balloon_x = balloon.x[0]
          balloon_y = balloon.y[0]  
          for h in wizardtower:
           for i in h.x:
              for j in h.y:
                  if((i-balloon_x)**2 + (j-balloon_y)**2 == 1):
                       h.health = h.health - balloon.damage
                       if h.health <= 0:
                         wizardtower.remove(h)
            
        if min(nearestd,nearestl,nearestr,nearestu) == nearestd:
          if nearestd != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()
            balloon.x[0] = balloon.x[0]+1
              
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestu:
          if nearestu != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()  
            balloon.x[0] = balloon.x[0]-1

        elif min(nearestd,nearestl,nearestr,nearestu) == nearestl:
          if nearestl != 0:  
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
            self.prev_balloon_attack_time = time.time()
            balloon.y[0] = balloon.y[0]-1
              
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestr:
          if nearestr != 0:
           if pres_time - self.prev_balloon_attack_time > balloon.speed:
             self.prev_balloon_attack_time = time.time()
             balloon.y[0] = balloon.y[0]+1




      



class Archer(Troops):
  def __init__(self,color,health,damage,x,y,speed,range):
        super().__init__(color,health,damage,x,y,speed)
        self.range = range
        self.prev_archer_attack_time = 0

  def archer_movement(self,archer,hut,wall,townhall,cannon,wizardtower):
    # print("in movement")
    pres_time = time.time()
    # if there is no cannon huts townhall in its range move 
    flagc =0
    flagh =0
    flagt =0 
    flagw = 0

    for h in cannon: 
      for i in h.x:
        for j in h.y:
          if((archer.x[0] - i)**2 + (archer.y[0]-j)**2 < archer.range**2):
          #  print("Damamging cannon")
           h.health = h.health - archer.damage
           if h.health <= 0:
             cannon.remove(h)
           flagc = 1

    for h in wizardtower: 
      for i in h.x:
        for j in h.y:
          if((archer.x[0] - i)**2 + (archer.y[0]-j)**2 < archer.range**2):
          #  print("Damamging wiz tower")
           h.health = h.health - archer.damage
           if h.health <= 0:
             wizardtower.remove(h)
           flagc = 1

    for h in hut: 
      for i in h.x:
        for j in h.y:
          if((archer.x[0] - i)**2 + (archer.y[0]-j)**2 < archer.range**2):
            # print("Damamging hut")
            h.health = h.health - archer.damage
            if h.health <= 0:
              hut.remove(h)
            flagh = 1
    if not cannon and not wizardtower and not hut:
     for i in townhall.x:
      for j in townhall.y:
          if((archer.x[0] - i)**2 + (archer.y[0]-j)**2 < archer.range**2):
            # print("Damamging townhall")
            townhall.health = townhall.health  - archer.damage
            if townhall.health == 0:
                 del townhall.x[:]
                 del townhall.y[:]
            flagt = 1
    
    if flagc==0 and flagh ==0 and  flagw==0 and flagt==0:  
      if not hut and not cannon and not townhall.x and not wizardtower:
        return
      else:
       archer.archer_move(archer,cannon,hut,townhall,wall,wizardtower)

  def archer_move(self,archer,cannon,hut,townhall,wall,wizardtower):
        
        # print("In move")
        pres_time = time.time()
        nearestu = 1000000
        nearestd = 1000000
        nearestl = 1000000
        nearestr = 1000000
        
        ############
        archer_x = archer.x[0]+1         
        archer_y = archer.y[0]
        
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestd):
                    nearestd = (i-archer_x)**2 + (j-archer_y)**2
          
        archer_x = archer.x[0]-1         
        archer_y = archer.y[0]
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestu):
                    nearestu = (i-archer_x)**2 + (j-archer_y)**2
                
        archer_x = archer.x[0] 
        archer_y = archer.y[0] - 1
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestl):
                    nearestl = (i-archer_x)**2 + (j-archer_y)**2
                   
        archer_x = archer.x[0] 
        archer_y = archer.y[0] + 1
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestr):
                    nearestr = (i-archer_x)**2 + (j-archer_y)**2

        #######
      
        archer_x = archer.x[0]+1         
        archer_y = archer.y[0]
        
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestd):
                    nearestd = (i-archer_x)**2 + (j-archer_y)**2
          
        archer_x = archer.x[0]-1         
        archer_y = archer.y[0]
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestu):
                    nearestu = (i-archer_x)**2 + (j-archer_y)**2
                
        archer_x = archer.x[0] 
        archer_y = archer.y[0] - 1
        for h in wizardtower:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestl):
                    nearestl = (i-archer_x)**2 + (j-archer_y)**2
                   
        archer_x = archer.x[0] 
        archer_y = archer.y[0] + 1
        for h in cannon:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestr):
                    nearestr = (i-archer_x)**2 + (j-archer_y)**2

        #######

        archer_x = archer.x[0] + 1
        archer_y = archer.y[0]

        for h in hut:
           for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestd):
                    nearestd = (i-archer_x)**2 + (j-archer_y)**2
          
        archer_x = archer.x[0]-1         
        archer_y = archer.y[0]
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestu):
                    nearestu = (i-archer_x)**2 + (j-archer_y)**2
                
        archer_x = archer.x[0] 
        archer_y = archer.y[0] - 1
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestl):
                    nearestl = (i-archer_x)**2 + (j-archer_y)**2 

        archer_x = archer.x[0] 
        archer_y =archer.y[0] + 1
        for h in hut:
          for i in h.x:
              for j in h.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestr):
                    nearestr = (i-archer_x)**2 + (j-archer_y)**2

            
        
        if not cannon and not hut and not wizardtower:
          archer_x = archer.x[0] + 1
          archer_y = archer.y[0]
          for i in townhall.x:
              for j in townhall.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestd):
                    nearestd = (i-archer_x)**2 + (j-archer_y)**2
          
          archer_x = archer.x[0]-1         
          archer_y = archer.y[0]
          for i in townhall.x:
              for j in townhall.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestu):
                    nearestu = (i-archer_x)**2 + (j-archer_y)**2
                
          archer_x = archer.x[0] 
          archer_y = archer.y[0] - 1
          for i in townhall.x:
              for j in townhall.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestl):
                    nearestl = (i-archer_x)**2 + (j-archer_y)**2
                   
          archer_x = archer.x[0] 
          archer_y = archer.y[0] + 1
          for i in townhall.x:
              for j in townhall.y:
                  if((i-archer_x)**2 + (j-archer_y)**2 < nearestr):
                    nearestr = (i-archer_x)**2 + (j-archer_y)**2
          

        if min(nearestd,nearestl,nearestr,nearestu) == nearestd:
          if nearestd != 0:
           if pres_time - self.prev_archer_attack_time > archer.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if archer.x[0]+1 == i and archer.y[0] == j:
                h.health = h.health - archer.damage
                if h.health <= 0:
                   wall.remove(h)
                return    
           self.prev_archer_attack_time = time.time()
           archer.x[0] = archer.x[0]+1
               
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestu:
          if nearestu != 0:
           if pres_time - self.prev_archer_attack_time > archer.speed:
             for h in wall:
              for i in h.x:
               for j in h.y:
                if archer.x[0]-1 == i and archer.y[0] == j:
                 h.health = h.health - archer.damage
                 if h.health <= 0:
                   wall.remove(h)
                 return
           self.prev_archer_attack_time = time.time()  
           archer.x[0] = archer.x[0]-1
           
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestl:
          if nearestl != 0:
           if pres_time - self.prev_archer_attack_time > archer.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if archer.x[0] == i and archer.y[0]-1 == j:
                h.health = h.health - archer.damage
                if h.health <= 0:
                   wall.remove(h)
                return
           self.prev_archer_attack_time = time.time() 
           archer.y[0] = archer.y[0]-1
                
        elif min(nearestd,nearestl,nearestr,nearestu) == nearestr:
          if nearestr != 0:
           if pres_time - self.prev_archer_attack_time > archer.speed:
            for h in wall:
             for i in h.x:
              for j in h.y:
               if archer.x[0] == i and archer.y[0]+1 == j:
                h.health = h.health - archer.damage
                if h.health <= 0:
                   wall.remove(h)
                return
           self.prev_archer_attack_time = time.time()
           archer.y[0] = archer.y[0]+1
