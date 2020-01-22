def clearScreen():  # 換場景時使用
    for i in range(100):
        print("\n")
        
class character():  # 紀錄角色狀態

     def __init__(self,name):
        self.name = name
        self.hp = 10



class environment():  # 紀錄環境狀態
    
    def __init__(self):
        self.day = 1
    
    def oneDayPass(self):
        self.day +=1


def showState(inCharacter,inEnv): # 顯示狀態
    print("Today is day {}".format(inEnv.day))
    print("Player: {} \nhp: {}".format(inCharacter.name, inCharacter.hp))
    

def chooseAction(): # 選擇行動
    choice = 0
    while 1:
        print("\n")
        print("1 Go to sleep")
        print("2 Do nothing")
        choice=input("what do you want to do now?")
        if choice == "1" or choice == "2":
            return choice
        else:
            clearScreen()
            print("invalid,please choice again!")






gameOver = False

player = character("brad")

env = environment()

while not gameOver:
    
    

    showState(player, env)
    ans = chooseAction()
    clearScreen()
    if ans == "1":
        env.oneDayPass()
        print("One day just passed")
    else:
        print("You do nothing~")
    print()

    
    if env.day >= 8:
        print("8 days to die!")
        print("game is over")
        gameOver=True

print("Game over")










 











