chData = {
    "littleZombie":{
        "name":"littleZombie",
        "hp":50,
        "atk":5,
        "deff":0,
    },

    "mainCharacter":{
        "name":"Tofu",  #default    
        "hp":100,
        "atk":10,
        "deff":1,
    },
}


class character():  # 紀錄角色狀態(新增攻擊力)

    def __init__(self,data):
        self.name = data["name"]
        self.hp = data["hp"]
        self.atk = data["atk"]
        self.deff = data["deff"]

    def changeName(self,name):
        self.name = name
