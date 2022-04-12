# from src.village import Village
# from colorama import Fore, Back, Style 
# from os import system
# from src.input import *
# from src.building import *
# from src.troops import *
# import time
# # village = Village()
# level = 1
# while(1):

#  if level == 1:
#   townhall = Townhall(Back.GREEN+' '+Style.RESET_ALL,1000,[15,16,17,18,19,20],[20,21,22,23,24,25]) 
#   wall1 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[18])
#   wall2 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[27])
#   wall3 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[13],[18,19,20,21,22,23,24,25,26,27])
#   wall4 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[22],[18,19,20,21,22,23,24,25,26,27])
#   hut1 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[4])
#   hut2 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[10],[16])
#   hut3 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[27],[28])
#   hut4 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[29],[12])
#   hut5 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[20],[62])
#   hut11 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[1],[4])
#   hut22 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[1],[5])
#   hut33 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[5])
#   hut44 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[4])
#   hut55 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[3],[5])

#   wall=[]
#   wall.append(wall1)
#   wall.append(wall2)
#   wall.append(wall3)
#   wall.append(wall4)
#   hut=[]
#   hut.append(hut1)
#   hut.append(hut2)
#   hut.append(hut3)
#   hut.append(hut4)
#   hut.append(hut5)
#   hut.append(hut11)
#   hut.append(hut22)
#   hut.append(hut33)
#   hut.append(hut44)
#   hut.append(hut55)
#   cannon1 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[9],[2],5,1)
#   cannon2 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[14],[55],5,1)
#   cannon=[]
#   cannon.append(cannon1)
#   cannon.append(cannon2)

#   wizardtower = []
#   wizardtower1 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[20],[2],5,1)
#   wizardtower2 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[25],[10],5,1)
#   wizardtower3 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[2],[35],5,1)

#   wizardtower.append(wizardtower1)
#   wizardtower.append(wizardtower2)
#   wizardtower.append(wizardtower3)

#   barb=[]
#   archer=[]
#   balloon=[]


#   print(" Choose if you want to play as the king or archer queen :))")
#   print("To choose queen avatar press j for king press k")
#   avatar = input()
#   king = King(Back.RED+' '+Style.RESET_ALL,100,10,[10],[28],avatar,1)
#   king_dead = 0


#   while(True):
#    village = Village()
#    char = get_input()
#    if char == "q":
#         print("Quit")
#         break
   
#    village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower)
#    if village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower) == False:
#         level = 2
#         print("Proceeding to level 2")
#         break


#    print(king.health)
#   if level == 1:
#         break


#  if level == 2:
#   townhall = Townhall(Back.GREEN+' '+Style.RESET_ALL,1000,[15,16,17,18,19,20],[20,21,22,23,24,25]) 
#   wall1 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[18])
#   wall2 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[27])
#   wall3 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[13],[18,19,20,21,22,23,24,25,26,27])
#   wall4 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[22],[18,19,20,21,22,23,24,25,26,27])
#   hut1 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[4])
#   hut2 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[10],[16])
#   hut3 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[27],[28])
#   hut4 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[27],[12])
#   hut5 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[20],[62])

#   wall=[]
#   wall.append(wall1)
#   wall.append(wall2)
#   wall.append(wall3)
#   wall.append(wall4)
#   hut=[]
#   hut.append(hut1)
#   hut.append(hut2)
#   hut.append(hut3)
#   hut.append(hut4)
#   hut.append(hut5)
#   cannon1 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[9],[2],5,1)
#   cannon2 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[14],[55],5,1)
#   cannon3 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[21],[46],5,1)

#   cannon=[]
#   cannon.append(cannon1)
#   cannon.append(cannon2)
#   cannon.append(cannon3)

#   wizardtower = []
#   wizardtower1 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[20],[2],5,1)
#   wizardtower2 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[25],[10],5,1)
#   wizardtower3 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[2],[60],5,1)

#   wizardtower.append(wizardtower1)
#   wizardtower.append(wizardtower2)
#   wizardtower.append(wizardtower3)

#   barb=[]
#   archer=[]
#   balloon=[]


#   print(" Choose if you want to play as the king or archer queen :))")
#   print("To choose queen avatar press j for king press k")
#   avatar = input()
#   king = King(Back.RED+' '+Style.RESET_ALL,100,10,[10],[28],avatar,1)
#   king_dead = 0


#   while(True):
#    village = Village()
#    char = get_input()
#    if char == "q":
#         print("Quit")
#         break
   
#    village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower)
#    if village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower) == False:
#         level = 3
#         print("Proceeding to level 3")
#         break
#    print(king.health)
  


#  if level == 3:
#   townhall = Townhall(Back.GREEN+' '+Style.RESET_ALL,1000,[15,16,17,18,19,20],[20,21,22,23,24,25]) 
#   wall1 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[18])
#   wall2 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[27])
#   wall3 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[13],[18,19,20,21,22,23,24,25,26,27])
#   wall4 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[22],[18,19,20,21,22,23,24,25,26,27])
#   hut1 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[4])
#   hut2 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[10],[16])
#   hut3 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[28])
#   hut4 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[17],[12])
#   hut5 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[20],[62])

#   wall=[]
#   wall.append(wall1)
#   wall.append(wall2)
#   wall.append(wall3)
#   wall.append(wall4)
#   hut=[]
#   hut.append(hut1)
#   hut.append(hut2)
#   hut.append(hut3)
#   hut.append(hut4)
#   hut.append(hut5)
#   cannon1 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[9],[2],5,1)
#   cannon2 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[14],[55],5,1)
#   cannon3 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[21],[46],5,1)
#   cannon4 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[21],[34],5,1)
 
#   cannon=[]
#   cannon.append(cannon1)
#   cannon.append(cannon2)
#   cannon.append(cannon3)
#   cannon.append(cannon4)
 

#   wizardtower=[]
#   wizardtower1 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[20],[2],5,1)
#   wizardtower2 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[25],[10],5,1)
#   wizardtower3 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[2],[60],5,1)

#   wizardtower.append(wizardtower1)
#   wizardtower.append(wizardtower2)
#   wizardtower.append(wizardtower3)
#   barb=[]
#   archer=[]
#   balloon=[]


#   print(" Choose if you want to play as the king or archer queen :))")
#   print("To choose queen avatar press j for king press k")
#   avatar = input()
#   king = King(Back.RED+' '+Style.RESET_ALL,100,10,[10],[28],avatar,1)
#   king_dead = 0


#   while(True):
#    village = Village()
#    char = get_input()
#    if char == "q":
#         print("Quit")
#         break
   
#    village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower)
#    if village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower) == False:
#         level = 2
#         print("Won")
#         break

#    print(king.health)
#    break



from src.village import Village
from colorama import Fore, Back, Style 
from os import system
from src.input import *
from src.building import *
from src.troops import *
import time
# village = Village()
level = 1


if level == 1:
  townhall = Townhall(Back.GREEN+' '+Style.RESET_ALL,1000,[15,16,17,18,19,20],[20,21,22,23,24,25]) 
  wall1 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[18])
  wall2 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[14,15,16,16,17,18,19,20,21],[27])
  wall3 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[13],[18,19,20,21,22,23,24,25,26,27])
  wall4 = Wall(Back.YELLOW+' '+Style.RESET_ALL,100,[22],[18,19,20,21,22,23,24,25,26,27])
  hut1 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[4])
  hut2 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[10],[16])
  hut3 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[27],[28])
  hut4 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[29],[12])
  hut5 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[20],[62])
  hut11 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[1],[4])
  hut22 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[1],[5])
  hut33 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[5])
  hut44 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[2],[4])
  hut55 = Hut(Back.WHITE+' '+Style.RESET_ALL,100,[3],[5])

  wall=[]
  wall.append(wall1)
  wall.append(wall2)
  wall.append(wall3)
  wall.append(wall4)
  hut=[]
  hut.append(hut1)
  hut.append(hut2)
  hut.append(hut3)
  hut.append(hut4)
  hut.append(hut5)
  hut.append(hut11)
  hut.append(hut22)
  hut.append(hut33)
  hut.append(hut44)
  hut.append(hut55)
  cannon1 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[9],[2],5,1)
  cannon2 = Cannon(Back.BLUE+' '+Style.RESET_ALL,100,[14],[55],5,1)
  cannon=[]
  cannon.append(cannon1)
  cannon.append(cannon2)

  wizardtower = []
  wizardtower1 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[20],[2],5,1)
  wizardtower2 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[25],[10],5,1)
  wizardtower3 = WizardTower(Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL,100,[2],[35],5,1)

  wizardtower.append(wizardtower1)
  wizardtower.append(wizardtower2)
  wizardtower.append(wizardtower3)

  barb=[]
  archer=[]
  balloon=[]


  print(" Choose if you want to play as the king or archer queen :))")
  print("To choose queen avatar press j for king press k")
  avatar = input()
  king = King(Back.RED+' '+Style.RESET_ALL,100,10,[10],[28],avatar,1)
  king_dead = 0


  while(True):
   village = Village()
   char = get_input()
   if char == "q":
        print("Quit")
        break
   
   if not townhall.x and not cannon and not wizardtower and not hut:
        print("You won")
        break
   if not cannon and not archer and not balloon and not king:
        print("you lost")
        break
   
   village.render(char,townhall,wall,hut,cannon,king,king_dead,barb,archer,balloon,wizardtower)
   print(king.health)





 