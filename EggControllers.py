import math
import random
class EggController():
    def __init__(self,Console,Next,me):
        self.me=me
        self.myWeight={}
        self.myGrowth={}
        self.destroy=[]
        self.GrowConstant=5
        self.Next=Next
        self.Console=Console
    def NewEgg(self):
        for i in range(math.floor((self.Console.chungi*0.2)+1)*self.Console.laytool):
            self.myWeight.update({self.Console.GlobalIDnumber:1})
            self.myGrowth.update({self.Console.GlobalIDnumber:0})
            self.Console.GlobalIDnumber+=1
        print(f"You managed to get your Chungi to lay sn egg.")
    def Incubate(self):
        self.destroy=[]
        for growth, key in enumerate(self.myGrowth):
            self.myGrowth[key]+=math.floor(self.Console.incubatetool*random.uniform(0,3))
            if self.myGrowth[key]>=self.GrowConstant:
                self.destroy.append(key)
        self.Hatch()
    def Hatch(self):
            for i in self.destroy:
                self.Console.chungus +=1
                self.Console.chungus_egg -=1
                self.myGrowth.pop(i)
                self.Next.myGrowth.update({i:0})
                self.Next.myWeight.update({i:math.floor(self.myWeight.pop(i)*1.5+5*random.uniform(0,1))})
                print("One of your chungus eggs hatched into grew into a chungus.")