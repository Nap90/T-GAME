import random
import side
gchWeapon = ["Knife", "punch", "Diamond Sword", "Golden Katana", "Jutsu", "Shuriken", "Yami Sword"]
damage = 0
weapon = ""

def gachaWeapon():
    global damage
    global weapon
    damage = random.randint(1, 65)
    weapon = random.choice(gchWeapon)
    checkWeapon()
    print("You Get", weapon, "Damage Bonus", damage)
    if weapon == "Yoru":
        if damage <= 65:
            print("You Lucky But Not Lucky In same time")
    elif damage >=65:
        print("You Lucky")

    elif weapon != "Yoru":
        if damage >=20:
            print("This Good Weapon")
        elif damage < 20:
            print("This is your not lucky Day?")

def checkWeapon():
    if weapon == "Jutsu":
        if side.userSide != "Ninja":
            gachaWeapon()
        else:
            print("You Got Ninjutsu")