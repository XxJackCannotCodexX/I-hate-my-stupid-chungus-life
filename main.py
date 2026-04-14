import time
import random
import math
import Command
import ChungusControllers
import ChungiControllers
import ChungoidControllers
import EggControllers
print("You own a chungi farm and you wake up and realize one of your chungi ate your farm hat.")
print("You hate your stupid chungus life.")


you = Command.Commands()
MainChungoidController = ChungoidControllers.ChungoidController(you,you.chungoid)
MainChungiController = ChungiControllers.ChungiController(you,MainChungoidController,you.chungi)
MainChungusController = ChungusControllers.ChungusController(you,MainChungiController,you.chungus)
MainEggController = EggControllers.EggController(you,MainChungusController,you.chungus_egg)
for i in range(you.chungus):
    MainChungusController.myWeight.update({you.GlobalIDnumber:random.randint(10,25)})
    MainChungusController.myGrowth.update({you.GlobalIDnumber:0})
    you.GlobalIDnumber+=1
for i in range(you.chungi):
    MainChungiController.myWeight.update({you.GlobalIDnumber:random.randint(30,45)})
    MainChungiController.myGrowth.update({you.GlobalIDnumber:0})
    you.GlobalIDnumber+=1
for i in range(you.chungoid):
    MainChungoidController.myWeight.update({you.GlobalIDnumber:random.randint(10,25)})
    MainChungoidController.myGrowth.update({you.GlobalIDnumber:0})
    you.GlobalIDnumber+=1
for i in range(you.chungus_egg):
    MainEggController.myWeight.update({you.GlobalIDnumber:random.randint(50,80)})
    MainEggController.myGrowth.update({you.GlobalIDnumber:0})
    you.GlobalIDnumber+=1
you.inventory.update({"Good Food": 3})
you.ChungiController=MainChungiController
you.ChungusController=MainChungusController
you.ChungoidController=MainChungoidController
you.Egg=MainEggController
print(MainChungoidController.myGrowth)
you.Loop()