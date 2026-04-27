class Dice: 
    def __init__(self, value:int, in_cup:bool, size:int, position:dict, color:str):
        self.value = value
        self.in_cup = in_cup
        self.size = size
        self.position = position
        self.color = color

    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, value):
        self.value = value

    def roll_dice():
        pass

    def show():
        pass