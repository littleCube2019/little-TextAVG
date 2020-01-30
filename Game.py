import random

def clearScreen():  # 換場景時使用
    for i in range(100):
        print("\n")
        
class character():  # 紀錄角色狀態(新增攻擊力)

     def __init__(self,name,hp,att):
        self.name = name
        self.hp = hp
        self.att = att



class environment():  # 紀錄環境狀態
    
    def __init__(self):
        self.day = 1
    
    def oneDayPass(self):
        self.day += 1



class enemy(): # 紀錄敵人參數(新增)

    def __init__(self,hp,att):
        self.hp=hp
        self.att=att

def showState(inCharacter,inEnv): # 顯示狀態
    print("Today is day {}".format(inEnv.day))
    print("Player: {} \nhp: {}".format(inCharacter.name, inCharacter.hp))
    

def chooseAction(): # 選擇行動
    choice = 0
    damage = 0
    if bloodMoon==False:
        while 1:
            print("\n")
            print("1 Go to sleep")
            print("2 Do nothing")
            choice=input("what do you want to do now?\n")
            if choice == "1" or choice == "2":
                return choice
            else:
                clearScreen()
                print("invalid,please choice again!")
    elif bloodMoon==True:
        while 1:
            print("\n")
            print("1 Attact")
            print("2 Run")
            choice=input("What do you want to do now?\n")
            if choice == "1":
                damage = random.randint(1,2)
                return damage
            elif choice == "2":
                damage = 0
                return damage
            else :
                clearScreen()
                print("invalid,please choice again!")







day = 7

gameOver = False

player = character("brad",10,1)

littleZombie = character("littleZombie",5,1)  # 小僵僵數值(新增)

bloodMoonDay = random.randint(2,day)  # 血月(新增)

env = environment()

bloodMoon = False

while not gameOver:
    
    

    
    if env.day==bloodMoonDay:
        bloodMoon = True
    elif env.day!=bloodMoonDay:
        bloodMoon = False
    if not bloodMoon:
        showState(player, env)
        ans = chooseAction()
        clearScreen()
        if ans == "1":
            env.oneDayPass()
            print("One day just passed")
        else:
            print("You do nothing~")
        print()

    if bloodMoon: # 跟little zombie戰鬥(新增)
        showState(player, env)
        print("\nToday is BLOODMOON!!!\n")
        while player.hp > 0 and littleZombie.hp > 0:
            print("There is a little zombie in your house")
            print("little zombie HP:{}".format(littleZombie.hp))
            print("your HP:{}".format(player.hp))
            damage = chooseAction()
            clearScreen()
            print("yo do {} damage\n".format(damage))
            littleZombie.hp -= damage
            if littleZombie.hp > 0:
                print("little zombie attact you")
                print("you lose 1 HP\n")
                player.hp -= 1
        if player.hp <= 0:
            print("you die\n")
            gameOver=True
        elif littleZombie.hp <= 0:
            print("you kill the little zombie\n")
            env.oneDayPass()
        
            


    if env.day >= 7:
        print("7 days to die!")
        print("game is over")
        gameOver=True

print("Game over")










 











