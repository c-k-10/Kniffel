class Cup:
    def __init__(self, dice_list:list):
        self.dice_list = dice_list

    def roll_dices():
        pass

    def reset():
        pass 

    
    def counts(self):
        c = [0] * 7
        for d in self.dice_list:
            c[d.value] += 1
    
        values = [d.value for d in self.dice_list]
        total = sum(values)

        return c, values, total