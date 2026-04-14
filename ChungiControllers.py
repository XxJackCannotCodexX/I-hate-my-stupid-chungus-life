import math
import random
class ChungiController():
    def __init__(self,Console,Next,me):
        self.myWeight={}
        self.myGrowth={}
        self.GrowConstant=12.5
        self.Next=Next
        self.Console=Console
    def Feed(self,food,Feedtype):
        if Feedtype==0:
            biggie = random.choice(list(self.myGrowth.keys()))
            self.myWeight[biggie]+=food
            self.myGrowth[biggie]+=food
            self.GrowUp(biggie)
        elif Feedtype==1:
            biggest=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[biggest]:
                    biggest=ident
            self.myWeight[biggest]+=food
            self.myGrowth[biggest]+=food
            self.GrowUp(biggest)
        elif Feedtype==2:
            smallest=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[smallest]:
                    smallest=ident
            self.myWeight[smallest]+=food
            self.myGrowth[smallest]+=food
            self.GrowUp(smallest)
        elif Feedtype==3:
            biggest=list(self.myGrowth.keys())[0]
            for ident, weight in self.myGrowth.items():
                if weight>self.myGrowth[biggest]:
                    biggest=ident
            self.myWeight[biggest]+=food
            self.myGrowth[biggest]+=food
            self.GrowUp(biggest)
        elif Feedtype==4:
            smallest=list(self.myWeight.keys())[0]
            for ident, weight in self.myGrowth.items():
                if weight>self.myGrowth[smallest]:
                    smallest=ident
            self.myWeight[smallest]+=food
            self.myGrowth[smallest]+=food
            self.GrowUp(smallest)
        self.Console.Loop()
    def GrowUp(self,target):
            if self.myGrowth[target] >= self.GrowConstant:
                self.Console.chungoid +=1
                self.Console.chungi -=1
                self.Next.myWeight.append({target:math.floor(self.myWeight.pop(target)*1.5+5)})
                self.Console.Loop()
            else:
                self.Console.Loop()
    def Butcher(self,Feedtype,tools):
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+2})
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+2)
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungi -=1
        elif Feedtype==1:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+2})
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+2)
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungi -=1
        elif Feedtype==2:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+2})
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+2)
                print(f"You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungi -=1
        self.Console.Loop()
    def Sell(self,target,market,day):
        pass
    def Lay(self,target,market):
        pass