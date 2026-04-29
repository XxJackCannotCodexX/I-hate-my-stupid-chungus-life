import time
import random
import math
print("You own a chungi farm and you wake up and realize one of your chungi ate your farm hat.")
print("You hate your stupid chungus life.")
print("Build a factory to make your farmer hat.")
class Commands():
    def __init__(self):
        #Commands you have
        self.UnlockedCommands=["Help","Incubate","Finances","Milk","Butcher","Market","Lay","Feed"]
        #Commands used in the market
        self.MarketCommands=["Buy","Sell","Check","Help"]
        #money
        self.money = 100
        #date
        self.day = [1,1,26]
        #how many chungus you have
        self.chungus = 10
        #how many chungi you have
        self.chungi = 3
        #how many chungoid you have
        self.chungoid = 1
        #how many chungus eggs you have
        self.chungus_egg = 5
        #inventory
        self.inventory = {"Hat_Scraps":1}
        #valid food:how much effect the food has
        self.foods={"Good Food":5,"Bad Food":2,"Deluxe Food":10,"Corporate Food": 3, "Chungus Meat": 1}
        self.foodPrice={"Good Food":10, "Bad Food":3, "Deluxe Food":15, "Corporate Food":6}
        self.D_UnlockedCommands = {"Help":"Displays this", "Incubate":"Incubate your eggs to get them closer to hatching.", "Finances":"View your inventory, chungus amounts, and a bunch of other finance stuff", "Milk":"Milk a chungoid, to get buckets of milk, more milk per Chungoid.", "Butcher":"Kill one of your livestock, get more chungus meat the older they were", "Lay":"Get your Chungi to lay an egg, more eggs per Chungi", "Market":"Go to the Market to buy or sell stuff", "Feed":"Feed your livestock to help them grow."}
        self.ChungusController = None
        self.ChungiController = None
        self.ChungoidController = None
        self.Egg = None
        self.tools=1
        self.IndexCommand={}
        self.GlobalIDnumber=0
        self.viables=[]
        self.laid=5
        self.milked=5
        self.incubated=5
        self.milktool=1
        self.incubatetool=1
        self.laytool=1
        self.networth=0
        self.factory=[]
    def Help(self):
        for name, instructions in self.D_UnlockedCommands.items():
            print(f"{name}: {instructions}")
        self.Loop()
    def FeedType(self,ChungusType,food,foodname):
        print("[0] Random")
        print("[1] Most Weight.")
        print("[2] Least Weight.")
        if int(ChungusType)!=2:
            print("[3] Closest to growing.")
            print("[4] Furthest from growing.")
        print("[C] Cancel.")
        while True:
            choice=input("How would you like to feed? ")
            if [str(i) for i in range(5)].count(choice)!=0:
                if int(ChungusType)!=2:
                    break
                elif [str(i) for i in range(3)].count(choice)!=0:
                    break
                else:
                    continue
            elif choice.upper()=="C":
                self.Loop()
                break
            else:
                continue
        if self.inventory[foodname]==1:
            self.inventory.pop(foodname)
        else:
            self.inventory[foodname]-=1
        if ChungusType==str(0):
            self.ChungusController.Feed(food,int(choice))
        elif ChungusType==str(1):
            self.ChungiController.Feed(food,int(choice))
        elif ChungusType==str(2):
            self.ChungoidController.Feed(food,int(choice))
    def FeedChoose(self,ChungusType):
        if [list(self.foods.keys()).count(i)==0 for i in list(self.inventory.keys())].count(False)!=0:
            myFoods=[]
            for i in list(self.inventory.keys()):
                if list(self.foods.keys()).count(i)!=0:
                    myFoods.append(i)
            IndexFood={}
            for index, food in enumerate(myFoods):
                print(f"[{index}] {food}. You have {self.inventory[food]}")
                IndexFood.update({index:food})
            print(f"[C] Cancel.")
            while True:
                choice=input("What food would you like to feed? ")
                if choice.upper()=="C":
                    self.Loop()
                    break
                try:
                    choice=int(choice)
                except:
                    continue
                if list(IndexFood.keys()).count(int(choice))!=0:
                    self.FeedType(ChungusType,self.foods[IndexFood[choice]],IndexFood[choice])
                    break
                elif isinstance(choice,str):
                    if choice.upper()=="C":
                        self.Loop()
                        break
                    else:
                        continue
        else:
            print("You do not have any food")
            self.Loop()
        
    def ChungusChooseFeed(self):
        while True:
            choice = input("Which Chungus would you like to feed? ")
            if self.viables.count(choice)!=0:
                self.FeedChoose(choice)
                break
            elif isinstance(choice, str):
                if choice.upper()=="C":
                    self.Loop()
                    break
                else:
                    continue
    def Feed(self):
        if self.chungus>0:
            print(f"[0] Chungus. You have {self.chungus}")
            self.viables.append("0")
        if self.chungi>0:
            print(f"[1] Chungi. You have {self.chungi}")
            self.viables.append("1")
        if self.chungoid>0:
            print(f"[2] Chungoid. You have {self.chungoid}")
            self.viables.append("2")
        print(f"[C] Cancel.")
        self.ChungusChooseFeed()
    def Butcher(self):
        if self.chungus>0:
            print(f"[0] Chungus. You have {self.chungus}")
            self.viables.append("0")
        if self.chungi>0:
            print(f"[1] Chungi. You have {self.chungi}")
            self.viables.append("1")
        if self.chungoid>0:
            print(f"[2] Chungoid. You have {self.chungoid}")
            self.viables.append("2")
        print(f"[C] Cancel.")
        self.ChungusChooseButcher()
    def ChungusChooseButcher(self):
        while True:
            choice = input("Which Chungus would you like to butcher? ")
            if self.viables.count(choice)!=0:
                self.ButcherType(choice)
                break
            elif choice.upper()=="C":
                self.Loop()
                break
            else:
                continue
    def ButcherType(self, ChungusType):
        print("[0] Random")
        print("[1] Most Weight.")
        print("[2] Least Weight.")
        print("[C] Cancel.")
        while True:
            choice=input("How would you like to butcher? ")
            if [str(i) for i in range(3)].count(choice)!=0:
                break
            elif choice.upper()=="C":
                self.Loop()
                break
            else:
                continue
        if ChungusType==str(0):
            self.ChungusController.Butcher(int(choice), self.tools)
        elif ChungusType==str(1):
            self.ChungiController.Butcher(int(choice), self.tools)
        elif ChungusType==str(2):
            self.ChungoidController.Butcher(int(choice), self.tools)
    def Milk(self):
        if self.chungoid!=0:
            if self.milked>2:
                print(f"You managed to get {math.floor((self.chungoid*0.2)+1)} buckets of milk.")
                if list(self.inventory.keys()).count("Chungus Milk")!=0:
                    self.inventory["Chungus Milk"] +=math.floor(((self.chungoid*0.2)+1)*self.milktool)
                    self.milked=0
                else:
                    self.inventory.update({"Chungus Milk":math.floor(((self.chungoid*0.2)+1)*self.milktool)})
                    self.milked=0
            else:
                print("You don't feel like milking a Chungoid for now.")
        else:
            print("How do you expect to get milk without any Chungoids?")
        self.Loop()
    def Lay(self):
        if self.chungi!=0:
            if self.laid>2:
                self.laid=0
                self.Egg.NewEgg()
            else:
                print("You don't feel getting a Chungi to lay and egg for now.")
        else:
            print("How do you expect to get eggs without any Chungi?")
        self.Loop()
    def Incubate(self):
        if self.chungus_egg!=0:
            if self.incubated>2:
                self.incubated=0
                self.Egg.Incubate()
            else:
                print("You don't feel incubating any more eggs for now.")
        else:
            print("How do you expect to incubate without any eggs")
        self.Loop()
    def Finance(self):
        print(f"Eggs: {self.chungus_egg}")
        print(f"Chungus: {self.chungus}")
        print(f"Chungi {self.chungi}")
        print(f"Chungoid: {self.chungoid}")
        print("Inventory:")
        for key, item in self.inventory.items():
            print(f"    {key}:{item}")
        print(f"Money: {self.money}")
        self.networth=self.money
        if list(self.inventory.keys()).count("Chungus Meat")!=0:
            self.networth+=(self.inventory["Chungus Meat"]*5)
        if list(self.inventory.keys()).count("Chungus Milk")!=0:
            self.networth+=(self.inventory["Chungus Milk"]*10)
        print(f"Net Worth(all sellable items liquidated): {self.networth}")
        self.Loop()
    def MarketEnter(self):
        while True:
            print("[0] Sell")
            print("[1] Buy")
            print("[C] Cancel.")
            choice=input("Which would like to do? ")
            if choice.upper()=="C":
                self.Loop()
                break
            elif choice=="0":
                self.MarketSell()
            elif choice=="1":
                self.MarketBuy()
    def MarketBuy(self):
        while True:
            print("[0] Buy tools")
            print("[1] Buy food")
            print("[C] Cancel.")
            choice=input("Which would like to do? ")
            if choice.upper()=="C":
                self.Loop()
                break
            elif choice=="0":
                self.MarketBuyStuff()
            elif choice=="1":
                self.MarketBuyFood()
    def MarketSell(self):
        viables=[]
        sellables=["Chungus Meat", "Chungus Milk"]
        for name, amount in self.inventory.items():
            if sellables.count(name) and amount != 0:
                print(f"[{len(viables)}] {name}") 
                viables.append(name)
        print("[C] Cancel.")
        if len(viables)!=0:
            while True:
                choice = input("Which would you like to sell? ")
                if [str(i) for i in range(len(viables))].count(choice)!=0:
                    if viables[int(choice)]=="Chungus Meat":
                        self.money+=(self.inventory["Chungus Meat"]*5)
                        self.inventory["Chungus Meat"]=0
                        print(f"You now have {self.money} dollars.")
                        self.incubated+=1
                        self.milked+=1
                        self.laid+=1
                        self.Loop()
                        break
                    elif viables[int(choice)]=="Chungus Milk":
                        self.money+=(self.inventory["Chungus Milk"]*10)
                        self.inventory["Chungus Milk"]=0
                        print(f"You now have {self.money} dollars.")
                        self.incubated+=1
                        self.milked+=1
                        self.laid+=1
                        self.Loop()
                        break
                else:
                    try:
                        if choice.upper()=="C":
                            self.Loop()
                            break
                        else:
                            continue
                    except:
                        continue
        else:
            print("You have nothing to sell.")
            self.Loop()
    def MarketBuyFood(self):
        for food, price in self.foodPrice.items():
            print(f"[{list(self.foodPrice.keys()).index(food)}] {food}. Cost: {price} dollars")
        print("[C] Cancel")
        while True:
            choice=input(f"You have {self.money} dollars. What would you like to buy? ")
            if [str(i) for i in range(len(self.foodPrice))].count(choice)!=0:
                self.MarketBuyFoodAmount(list(self.foodPrice.keys())[int(choice)])
                break
            else:
                try:
                    if choice.upper()=="C":
                        self.Loop()
                        break
                    else:
                        continue
                except:
                    continue
    def MarketBuyFoodAmount(self, bought):
        choiceAmount={"0":1,"1":3,"2":5,"3":10}
        print(f"[0] 1 unit of {bought}. Cost: {self.foodPrice[bought]} dollars")
        print(f"[1] 3 units of {bought}. Cost: {self.foodPrice[bought]*3} dollars")
        print(f"[2] 5 units of {bought}. Cost: {self.foodPrice[bought]*5} dollars")
        print(f"[3] 10 units of {bought}. Cost: {self.foodPrice[bought]*10} dollars")
        while True:
            choice = input("How much would you like to buy? ")
            if [str(i) for i in range(len(self.foodPrice))].count(choice)!=0:
                if self.money>=self.foodPrice[bought]*choiceAmount[choice]:
                    self.money-=self.foodPrice[bought]*choiceAmount[choice]
                    if list(self.inventory.keys()).count(bought)!=0:
                        self.inventory[bought] += choiceAmount[choice]
                        self.Loop()
                        self.incubated+=1
                        self.milked+=1
                        self.laid+=1
                        break
                    else:
                        self.inventory.update({bought:choiceAmount[choice]})
                        self.Loop()
                        self.incubated+=1
                        self.milked+=1
                        self.laid+=1
                        break
                else:
                    print("You don't have enough money.")
                    self.Loop()
                    break
            else:
                try:
                    if choice.upper()=="C":
                        self.Loop()
                        break
                    else:
                        continue
                except:
                    continue
    def MarketBuyStuff(self):
        viables={}
        def canBuy(name,power):
            if power==1:
                viables.update({"OK "+name:100})
                print(f"[{len(viables)-1}] OK {name}. Cost: {viables['OK '+name]} dollars")
                viables.update({"Good "+name:250})
                print(f"[{len(viables)-1}] Good {name}. Cost: {viables['Good '+name]} dollars")
                viables.update({"Best "+name:500})
                print(f"[{len(viables)-1}] Best {name}. Cost: {viables['Best '+name]} dollars")
            if power==1.5:
                viables.update({"Good "+name:250})
                print(f"[{len(viables)-1}] Good {name}. Cost: {viables['Good '+name]} dollars")
                viables.update({"Best "+name:500})
                print(f"[{len(viables)-1}] Best {name}. Cost: {viables['Best '+name]} dollars")
            if power==2:
                viables.update({"Best "+name:500})
                print(f"[{len(viables)-1}] Best {name}. Cost: {viables['Best '+name]} dollars")
        canBuy("butcher tools",self.tools)
        canBuy("incubater",self.incubatetool)
        canBuy("egg basket",self.laytool)
        canBuy("milker",self.milktool)
        if self.factory.count(1)==0:
            viables.update({f"Land for hat factory":500})
        if self.factory.count(2)==0:
            viables.update({f"Workers for hat factory":1000})
        if self.factory.count(3)==0:
            viables.update({f"Materials to build hat factory":1500})
        if self.factory.count(1)==0:    
            print(f"[{list(viables.keys()).index('Land for hat factory')}] Land for hat factory. Cost: 500")
        if self.factory.count(2)==0:
            print(f"[{list(viables.keys()).index('Workers for hat factory')}] Workers for hat factory. Cost: 1000")
        if self.factory.count(3)==0:
            print(f"[{list(viables.keys()).index('Materials to build hat factory')}] Materials to build hat factory. Cost: 1500")
        indexviable={}
        for index, name in enumerate(viables.keys()):
            indexviable.update({index:name})
        print("[C] Cancel.")
        while True:
            choice=input(f"You have {self.money} dollars. What would you like to buy? ")
            if [str(i) for i in range(len(viables))].count(choice)!=0:
                bought=(indexviable[int(choice)]).split()
                cost=viables[indexviable[int(choice)]]
                if self.money>=cost:
                    if bought.count("OK")!=0 or bought.count("Land")!=0:
                        if bought.count("butcher")!=0:
                            self.tools=1.5
                        elif bought.count("incubater")!=0:
                            self.incubatetool=1.5
                        elif bought.count("egg")!=0:
                            self.laytool=1.5
                        elif bought.count("milker")!=0:
                            self.milktool=1.5
                        elif bought.count("factory")!=0:
                            self.factory.append(1)
                    elif bought.count("Good")!=0 or bought.count("Workers")!=0:
                        if bought.count("butcher")!=0:
                            self.tools=2
                        elif bought.count("incubater")!=0:
                            self.incubatetool=2
                        elif bought.count("egg")!=0:
                            self.laytool=2
                        elif bought.count("milker")!=0:
                            self.milktool=2
                        elif bought.count("factory")!=0:
                            self.factory.append(2)
                    if bought.count("Best")!=0 or bought.count("Materials")!=0:
                        if bought.count("butcher")!=0:
                            self.tools=2.5
                        elif bought.count("incubater")!=0:
                            self.incubatetool=2.5
                        elif bought.count("egg")!=0:
                            self.laytool=2.5
                        elif bought.count("milker")!=0:
                            self.milktool=2.5
                        elif bought.count("factory")!=0:
                            self.factory.append(3)        
                    self.incubated+=1
                    self.milked+=1
                    self.laid+=1
                    self.money-=cost
                    print(f"You bought {indexviable[int(choice)]} for {cost} dollars. You now have {self.money} dollars.")
                    self.Loop()
                    break
                else:
                    print("You don't have enough money.")
                    continue
            else:
                try:
                    if choice.upper()=="C":
                        self.Loop()
                        break
                    else:
                        continue
                except:
                    continue
    def Loop(self):
        time.sleep(0.5)
        if len(self.factory)!=3:
            self.IndexCommand={}
            self.viables=[]
            for index, action in enumerate(self.UnlockedCommands):
                print(f"[{index}] {action}.")
                self.IndexCommand.update({index:action})
            while True:
                choice=input("What do you want to do? ")
                if [str(i) for i in range(len(self.UnlockedCommands))].count(choice)!=0:
                    break
                else: 
                    continue
            choice=int(choice)
            if self.IndexCommand[choice]=="Help":
                self.Help()
            elif self.IndexCommand[choice]=="Feed":
                self.Feed()
            elif self.IndexCommand[choice]=="Butcher":
                self.Butcher()
            elif self.IndexCommand[choice]=="Milk":
                self.Milk()
            elif self.IndexCommand[choice]=="Lay":
                self.Lay()
            elif self.IndexCommand[choice]=="Incubate":
                self.Incubate()
            elif self.IndexCommand[choice]=="Finances":
                self.Finance()
            elif self.IndexCommand[choice]=="Market":
                self.MarketEnter()
        else:
            print("As you began building your factory, you get a letter that you do not have proper the permits.")
            print("You hate your stupid chungus life.")
            print("Stage 2 coming soon.")
class ChungusController():
    def __init__(self,Console,Next,me):
        self.myWeight={}
        self.myGrowth={}
        self.GrowConstant=7.5
        self.Next=Next
        self.Console=Console
    def Feed(self,food,Feedtype):
        self.Console.incubated+=1
        self.Console.milked+=1
        self.Console.laid+=1
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
            self.GrowUp(target)
        elif Feedtype==1:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
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
        print(f"You fed one of your Chungus. It now weighs {self.myWeight[target]} pounds.")
        self.Console.Loop()
    def GrowUp(self,target):
            if self.myGrowth[target] >= self.GrowConstant:
                print("One of your chungus grew into a chungi.")
                self.Console.chungi +=1
                self.Console.chungus -=1
                self.myGrowth.pop(target)
                self.Next.myGrowth.update({target:0})
                self.Next.myWeight.update({target:math.floor(self.myWeight.pop(target)*1.5+5)})
    def Butcher(self,Feedtype,tools):
        self.Console.incubated+=1
        self.Console.milked+=1
        self.Console.laid+=1
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
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
        print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
        self.Console.Loop()
class ChungiController():
    def __init__(self,Console,Next,me):
        self.myWeight={}
        self.myGrowth={}
        self.GrowConstant=12.5
        self.Next=Next
        self.Console=Console
    def Feed(self,food,Feedtype):
        self.Console.incubated+=1
        self.Console.milked+=1
        self.Console.laid+=1
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
            self.GrowUp(target)
        elif Feedtype==1:
            target=list(self.myWeight.keys())[0]
            for ident, weight in self.myWeight.items():
                if weight>self.myWeight[target]:
                    target=ident
            self.myWeight[target]+=food
            self.myGrowth[target]+=food
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
        print(f"You fed one of your Chungi. It now weighs {self.myWeight[target]} pounds.")
        self.Console.Loop()
    def GrowUp(self,target):
            if self.myGrowth[target] >= self.GrowConstant:
                print("One of your chungi grew into a chungoid.")
                self.Console.chungoid +=1
                self.Console.chungi -=1
                self.myGrowth.pop(target)
                self.Next.myWeight.update({target:math.floor(self.myWeight.pop(target)*1.5+5)})
                self.Console.Loop()
            else:
                self.Console.Loop()
    def Butcher(self,Feedtype,tools):
        self.Console.incubated+=1
        self.Console.milked+=1
        self.Console.laid+=1
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+2})
                print(f"You now have {str(self.Console.inventory['Chungus Meat'])} Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+2)
                print("You now have " + str(self.Console.inventory['Chungus Meat']) + " Chungus Meat")
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
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+2)
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
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
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+2)
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungi -=1
        self.Console.Loop()
class ChungoidController():
    def __init__(self,Console,me):
        self.myWeight={}
        self.myGrowth={}
        self.Console=Console
    def Butcher(self,Feedtype,tools):
        self.Console.incubated+=1
        self.Console.milked+=1
        self.Console.laid+=1
        if Feedtype==0:
            target = random.choice(list(self.myGrowth.keys()))
            if list(self.Console.inventory.keys()).count("Chungus Meat") == 0:
                self.Console.inventory.update({"Chungus Meat": (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools))+5})
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+5)
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
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
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+5)
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
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
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            else:
                self.Console.inventory["Chungus Meat"] = self.Console.inventory["Chungus Meat"] + (math.ceil(1+(math.floor(self.myWeight[target]/10))*tools)+5)
                print("You now have " + str(self.Console.inventory["Chungus Meat"]) + " Chungus Meat")
            self.myGrowth.pop(target)
            self.myWeight.pop(target)
            self.Console.chungoid -=1
        self.Console.Loop()
    def Feed(self,food,Feedtype):
        self.Console.incubated+=1
        self.Console.milked+=1
        self.Console.laid+=1
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
        print(f"You fed one of your Chungoid. It now weighs {self.myWeight[target]} pounds.")
        self.Console.Loop()
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
            self.Console.chungus_egg+=1
            self.Console.GlobalIDnumber+=1
            print(f"You managed to get your Chungi to lay an egg.")
    def Incubate(self):
        print(f"You incubated your {self.Console.chungus_egg} eggs.")
        self.destroy=[]
        for key in self.myGrowth.keys():
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
you = Commands()
MainChungoidController = ChungoidController(you,you.chungoid)
MainChungiController = ChungiController(you,MainChungoidController,you.chungi)
MainChungusController = ChungusController(you,MainChungiController,you.chungus)
MainEggController = EggController(you,MainChungusController,you.chungus_egg)
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
you.Loop()