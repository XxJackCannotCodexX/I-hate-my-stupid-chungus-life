import math
import random
class ChungoidController():
    def __init__(self,Console,me):
        self.myWeight={}
        self.myGrowth={}
        self.Console=Console
    def Butcher(self,Feedtype,tools):
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+5})
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+5)
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungoid -=1
        elif Feedtype==1:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+5})
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+5)
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungoid -=1
        elif Feedtype==2:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+5})
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+5)
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungoid -=1
        self.Console.Loop()
    def Sell(self,target,market,day):
        pass
    def Milk(self,target):
        pass
    def Feed(self,food,Feedtype):
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
        elif Feedtype==1:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
        elif Feedtype==2:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
        self.Console.Loop()