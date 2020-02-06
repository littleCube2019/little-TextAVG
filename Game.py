import random
import character as ch
import environment as env

# varibal list ====================================
eventList = {
    "normalDay":("Go to sleep","Do nothing"),        
    "bloodMoonDay":("Attack","Run"),
}        

# varibal list ====================================

def choice(event):
    while 1:
        print("what do you want to do now?\n")
        choiceRange = set()
    

        for num,option in enumerate(eventList[event]):
            print("{}. {}".format(num+1,option))
            choiceRange |= {str(num+1)}

        choice = input()

        if choice in choiceRange:
            return choice
            
        for i in range(100):
            print()  #clean screen
        print("invalid,please choice again!")
        

def clearScreen():  # 換場景時使用
    for i in range(100):
        print("\n")


def showState(inCharacter,inEnv): # 顯示狀態
    print("Today is day {}".format(inEnv.day))
    print("Player: {} \nhp: {}".format(inCharacter.name, inCharacter.hp))

def doDamage(aAtk,bDeff):
    damage = aAtk*random.randint(1,2)-bDeff
    if damage <= 0:
        return 0
    else:
        return damage
# varibal list ====================================
gameOver = False

player = ch.character(ch.chData["mainCharacter"])

littleZombie = ch.character(ch.chData["littleZombie"])

env = env.environment()

# varibal list ====================================
while not gameOver:
    showState(player, env)

    if env.isBloodMoon(): 
        print("\nToday is BLOODMOON!!!\n")
        while player.hp > 0 and littleZombie.hp > 0:
            print("There is a little zombie in your house")
            print("little zombie HP:{}".format(littleZombie.hp))
            print("your HP:{}".format(player.hp))
                  
            ans = choice("bloodMoonDay")
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
            break     #game is over
        elif littleZombie.hp <= 0:
            print("you kill the little zombie\n")
    
    ans = choice("normalDay")
    clearScreen()
    if ans == "1":
        env.oneDayPass()
        print("One day just passed")
    else:
        print("You do nothing~")
        print()
        
    if env.day >= env.endDay:
        print("7 days to die!")
        print("game is over")
        gameOver = True

print("Game over")










 











