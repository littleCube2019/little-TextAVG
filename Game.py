import random

def clearScreen():  # 換場景時使用
    for i in range(100):
        print("\n")
        
class character():  # 紀錄角色狀態(新增攻擊力)

     def __init__(self,name,hp,atk,deff):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.deff = deff



class environment():  # 紀錄環境狀態
    
    def __init__(self):
        self.day = 1
    
    def oneDayPass(self):
        self.day += 1



def showState(inCharacter,inEnv): # 顯示狀態
    print("Today is day {}".format(inEnv.day))
    print("Player: {} \nhp: {}".format(inCharacter.name, inCharacter.hp))
    

def chooseAction(): # 選擇行動
    choice = 0
    if not bloodMoon:
        choice = normalDay()
    elif bloodMoon:
        choice = bloodDay()
    return choice
    

def normalDay():
    choice = 0
    while 1:
            print("what do you want to do now?\n")
            print("1 Go to sleep")
            print("2 Do nothing")
            choice = input()
            if choice == "1" or choice == "2":
                return choice
            else:
                clearScreen()
                print("invalid,please choice again!")

def bloodDay():
    choice = 0
    while 1:
            print("What do you want to do now?\n")
            print("1 Attact")
            print("2 Run")
            choice = input()
            if choice == "1" or choice == "2":
                return choice
            else:
                clearScreen()
                print("invalid,please choice again!")


def doDamage(aAtk,bDeff):
    damage = aAtk*random.randint(1,2)-bDeff
    if damage <= 0:
        return 0
    else:
        return damage



DAY = 7

gameOver = False

player = character("brad",100,10,1)

littleZombie = character("littleZombie",50,5,0)  # 小僵僵數值(新增)

bloodMoonDay = random.randint(2,DAY)  # 血月(新增)

env = environment()

bloodMoon = False


while not gameOver:
    
    
    if env.day == bloodMoonDay:
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
            ans = chooseAction()
            if ans == "1":
                clearScreen()
                damage = doDamage(player.atk,littleZombie.deff)
                print("yo do {} damage\n".format(damage))
            elif ans == "2":
                clearScreen()
                damage = 0
                print("YOU SCREAM AND RUN!!!\n")
            littleZombie.hp -= damage
            if littleZombie.hp > 0:
                print("little zombie attact you")
                damage = doDamage(littleZombie.atk,player.deff)
                print("you lose {} HP\n".format(damage))
                player.hp -= damage
        if player.hp <= 0:
            print("you die\n")
            gameOver=True
        elif littleZombie.hp <= 0:
            print("you kill the little zombie\n")
            env.oneDayPass()
        
            


    if env.day >= 7:
        print("7 days to die!")
        print("game is over")
        gameOver = True

print("Game over")










 











