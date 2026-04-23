import math
import random
class ChungusController():
    def __init__(self,Console,Next,me):
        self.myWeight={}
        self.myGrowth={}
        self.GrowConstant=7.5
        self.Next=Next
        self.Console=Console
    def Feed(self,food,Feedtype):
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
            self.GrowUp(target)
        elif Feedtype==1:
            biggest=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[biggest]:
                    biggest=ident
            self.myWeight[biggest]+=food
            self.myGrowth[biggest]+=food
            self.GrowUp(target)
        elif Feedtype==2:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
            self.GrowUp(target)
        elif Feedtype==3:
            target=list(self.myGrowth.keys())[0]
            for ident, weight in self.myGrowth.items():
                if weight>self.myGrowth[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
            self.GrowUp(target)
        elif Feedtype==4:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myGrowth.items():
                if weight>self.myGrowth[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
            self.GrowUp(target)
    def GrowUp(self,target):
            print("hi")
            if self.myGrowth[target] >= self.GrowConstant:
                self.Console.chungi +=1
                self.Console.chungus -=1
                self.myGrowth.pop(target)
                self.Next.myGrowth.update({target:0})
                self.Next.myWeight.update({target:math.floor(self.myWeight.pop(target)*1.5+5)})
                print("One of your chungus grew into a chungi.")
                self.Console.Loop()
            else:
                self.Console.Loop()
    def Butcher(self,Feedtype,tools):
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            print(target)
            print(self.myWeight)
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))})
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungus -=1
        elif Feedtype==1:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))})
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungus -=1
        elif Feedtype==2:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))})
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungus -=1
        print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
        self.Console.Loop()
    def Sell(self,target, market, day):
        pass