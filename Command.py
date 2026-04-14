class Commands():
    def __init__(self):
        #Commands you have
        self.UnlockedCommands=["Help","Incubate","Finances","Milk","Butcher","Market","Lay","Pass","Feed"]
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
        self.foods={"Good Food":3,"Bad Food":1,"Wheat":0.5,"Deluxe Food":5,"Corporate Food": 2, "Your Lunch":10, "Chungus Meat": 1}
        
        self.D_UnlockedCommands = {"Help":"Displays this", "Incubate":"Speed up a chungus eggs hatch time by stitting on it", "Finances":"View your inventory, chungus amounts, and a bunch of other finance stuff", "Milk":"Milk a chungoid, but try not to get kicked", "Butcher":"Kill one of your livestock, get more chungus meat the older they were", "Lay":"Try to get a chungi to lay an egg","Pass":"Just sleep I guess? Takes up a day.", "Market":"Go to the Market to buy or sell stuff", "Feed":"Feed your livestock to help them grow."}
        self.ChungusController = None
        self.ChungiController = None
        self.ChungoidController = None
        self.Egg = None
        self.tools=1
        self.IndexCommand={}
        self.GlobalIDnumber=0
        self.viables=[]
    def Help(self):
        for name, instructions in self.D_UnlockedCommands.items():
            print(f"{name}: {instructions}")
        self.Loop()
    def FeedType(self,ChungusType,food):
        print("[0] Random")
        print("[1] Most Weight.")
        print("[2] Least Weight.")
        if ChungusType!=2:
            print("[3] Closest to growing.")
            print("[4] Furthest from growing.")
        print("[C] Cancel.")
        while True:
            choice=input("How would you like to feed? ")
            if [str(i) for i in range(5)].count(choice)!=0:
                break
            elif choice.upper()=="C":
                self.Loop()
                break
            else:
                continue
        if ChungusType==str(0):
            self.ChungusController.Feed(food,choice)
        elif ChungusType==str(1):
            self.ChungiController.Feed(food,choice)
        elif ChungusType==str(2):
            self.ChungoidController.Feed(food,choice)
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
                    self.FeedType(ChungusType,self.foods[IndexFood[choice]])
                    break
                elif choice.upper()=="C":
                    self.Loop()
                    break
                else:
                    continue
        else:
            print("You do not have any food")
        
    def ChungusChooseFeed(self):
        while True:
            choice = input("Which Chungus would you like to feed? ")
            if self.viables.count(choice)!=0:
                self.FeedChoose(choice)
                break
            elif choice.upper()=="C":
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
    def Loop(self):
        self.IndexCommand={}
        self.viables=[]
        for index, action in enumerate(self.UnlockedCommands):
            print(f"[{index}] {action}.")
            self.IndexCommand.update({index:action})
        while True:
            try:
                choice=int(input("What do you want to do? "))
            except:
                continue
            if [str(i) for i in range(len(list(self.IndexCommand.keys())))]!=0:
                break
            else: 
                continue
        if self.IndexCommand[choice]=="Help":
            self.Help()
        elif self.IndexCommand[choice]=="Feed":
            self.Feed()
        elif self.IndexCommand[choice]=="Butcher":
            self.Butcher()