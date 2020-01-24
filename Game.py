import random

def clearScreen():  # 換場景時使用
    for i in range(100):
        print("\n")
        
class character():  # 紀錄角色狀態(新增攻擊力)

     def __init__(self,name):
        self.name = name
        self.hp = 10
        self.att = 1



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


def fight(): # 戰鬥系統(新增)
    choice = 0
    damage = 0
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
        






gameOver = False

player = character("brad")

littlezombie = enemy(5,1)  # 小僵僵數值(新增)

bloodmoon = random.randint(2,6)  # 血月(新增)

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

    if env.day == bloodmoon: # 跟little zombie戰鬥(新增)
        showState(player,env)
        print("\nToday is BLOODMOON!!!\n")
        while player.hp > 0 and littlezombie.hp > 0:
            print("There is a little zombie in your house")
            print("little zombie HP:{}".format(littlezombie.hp))
            print("your HP:{}".format(player.hp))
            damage = fight()
            clearScreen()
            print("yo do {} damage\n".format(damage))
            littlezombie.hp -= damage
            if littlezombie.hp > 0:
                print("little zombie attact you")
                print("you lose 1 HP\n")
                player.hp -= 1
        if player.hp <= 0:
            print("you die\n")
            gameOver=True
        elif littlezombie.hp <= 0:
            print("you kill the little zombie\n")
            


    if env.day >= 7:
        print("7 days to die!")
        print("game is over")
        gameOver=True

print("Game over")










 











