def showDamage(dmg):
    if dmg > 20:
        print("Crital Hit", dmg)
    elif dmg < 20:
        print("Damage", dmg)