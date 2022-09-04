import random, attackStyle, clan
elemen = ""
def getElement():
    global elemen 
    elemen = random.choice(attackStyle.ninjaJutsu)
    print("Your element", elemen)