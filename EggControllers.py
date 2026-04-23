import math
class EggController():
    def __init__(self,Console,Next,me):
        self.me=me
        self.myWeight={}
        self.myGrowth={}
        self.GrowConstant=3
        self.Next=Next
        self.Console=Console
    def NewEgg(self):
        for i in range(math.floor(self.Console.chungi*0.2)+1):
            self.myWeight.update({self.Console.GlobalIDnumber:1})
            self.myGrowth.update({self.Console.GlobalIDnumber:0})
            self.GlobalIDnumber+=1
    def Incubate(self,target):
        pass
    def Hatch(self,target):
        pass