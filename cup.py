
# === Klasse Cup ===
class Cup:
    def __init__(self, dice_list:list):
        self.dice_list = dice_list

    
    def counts(self):
        """Die Funktion zählt für jeden Würfel die Häufigkeit seiner Augenzahl, 
        speichert alle gewürfelten Werte und berechnet daraus die Gesamtsumme"""

        c = [0, 0, 0, 0, 0, 0, 0] #Häufigkeit
        values = [] #gewürfelte Werte
        total = 0 #Gesamtsumme

        for d in self.dice_list:
            value = d.value         
            values.append(value)   
            total += value         
            c[value] += 1          

        return c, values, total