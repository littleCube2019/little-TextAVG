import random
class environment():  # 紀錄環境狀態
    
    def __init__(self):
        self.day = 1
        self.endDay = 7
        self.bloodMoonDay = random.randint(2,self.endDay-1)
    def oneDayPass(self):
        self.day += 1

    def isBloodMoon(self):
        return self.day == self.bloodMoonDay 
