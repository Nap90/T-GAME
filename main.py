#This script inspired By: Naruto, Fairy Tail, Kimetsu no yaiba, genshin impact

from distutils.dep_util import newer
from distutils.log import error
import time
import random
import os
import json
from datetime import date, datetime

#module
import clan
import enemy
import attackStyle as art
import side
import damage as atk
import gacha
import breathing
import ninjutsu
import fmt_money
import vision

#data
database = './database/accounts.json'
history = './database/history.json'
inventory = './database/inventory.json'

side.userSide = "Citizen"

#main stat
money = 100
weaponName = "knife"
playerHP = 100
enemyHP = 100
dmgBonus = 0
playerDamage = random.randint(1, 25)
enemyDamage = random.randint(1, 25)
clan.clan = ""
need_save = 1

#function

def addInvntory(weapon, damage):
    item = {}
    with open(inventory, "r") as f:
        cache = json.load(f)
        id = len(cache)
    item["weapon"] = weapon
    item["damage"] = str(damage)
    item["id"] = str(id)
    cache.append(item)
    with open (inventory, "w") as f:
        json.dump(cache, f, indent=4)
    
def selectWeapon():
    global weaponName, dmgBonus
    with open (inventory, "r") as f:
        cache = json.load(f)
        i = 0
        lenght = len(cache)
        for query in cache:
            print(query.items())
        wp = input(f"Input weapon id:")
        i=0
        for query in cache:
            if i == int(wp):
                weaponName = query["weapon"]
                dmgBonus = int(query["damage"])
                runGame()
            else:
                i=i+1


def gachaHistory(get, dm):
    recent = {}
    jam = datetime.now()

    current_time = jam.strftime("%D-%H:%M:%S")
    w = current_time
    with open(history, "r") as f:
        cache = json.load(f)
        id = len(cache) +1
    recent["id"] = str(id)
    recent["type"] = "Gacha"
    recent["weapon"] = get
    recent["damage"] = str(dm)
    recent["date"] = w

    cache.append(recent)
    with open(history, "w") as f:
        json.dump(cache, f, indent=4)

def addHistory(hasil):
    recent = {}
    jam = datetime.now()

    current_time = jam.strftime("%D-%H:%M:%S")
    w = current_time
    with open(history, "r") as f:
        cache = json.load(f)
        id = len(cache) +1
    recent["id"] = str(id)
    recent["type"] = "Fight"
    recent["enemy"] = enemy.lawan
    recent["result"] = str(hasil)
    recent["date"] = w

    cache.append(recent)
    with open(history, "w") as f:
        json.dump(cache, f, indent=4)

def showHistory():
    clear()
    with open(history, "r") as f:
        cache = json.load(f)
        print(cache, "\n")
    h = input("Back to main menu? (y)")
    if h == "y":
        runGame()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")

def foundEnemy():
    global enemyHP
    global playerHP
    if enemyHP < 0:
        enemyHP = 0
    if playerHP < 0:
        playerHP = 0

    print("Player Health", playerHP, "enemy Health", enemyHP)
    print("")
    time.sleep(1)
    print("Select your choice")
    print("1.Attack\t\t2.Run")
    choice = input("")
    if choice == "1":
        attackEnemy(1)
    elif choice == "2":
        attackEnemy(2)


def attackEnemy(choised):
    clear()

    global playerHP
    global enemyHP
    global money
    global dmgBonus
    global playerDamage
    global enemyDamage
    playerDamage = random.randint(1, 25)
    enemyDamage = random.randint(1, 25)
    if choised == 1:
        if side.userSide == "Traveler":
            if vision.vision == "Anemo":
                print(name + ": Tornado")
            if vision.vision == "Electro":
                print(name + ": Strom Make")
            if vision.vision == "Pyro":
                print(name + ": Get burn")
            if vision.vision == "Hydro":
                print(name + ": Get drowned")
            if vision.vision == "Dendro":
                print(name + ": Create Your Way")
            if vision.vision == "Geo":
                print(name + ": I will have order")
            if vision.vision == "Cryo":
                print(name + ": Freeze")
        if side.userSide == "Ninja":
            if weaponName == "Jutsu":
                if ninjutsu.elemen == "Fuuton":
                    ninpo = random.choice(art.fuuton)
                    print(name + ":", ninpo)
                elif ninjutsu.elemen == "Suiton":
                    ninpo = random.choice(art.suiton)
                    print(name + ":", ninpo)
                elif ninjutsu.elemen == "Doton":
                    ninpo = random.choice(art.doton)
                    print(name + ":", ninpo)
                elif ninjutsu.elemen == "Katon":
                    ninpo = random.choice(art.katon)
                    print(name + ":", ninpo)
                elif ninjutsu.elemen == "Mokuton":
                    ninpo = random.choice(art.mokuton)
                    print(name + ":", ninpo)
            if weaponName == "Taijutsu":
                ninpo = random.choice(art.taijutsu)
                print(name + ":", ninpo)

        elif side.userSide == "DragonSlayer":
            dragonArt = random.choice(art.dragonSlayerATTACK)
            print("You Attack Enemy Use", dragonArt)

        elif side.userSide == "Demon Slayer":
            if breathing.teknik == "Fire":
                att = random.choice(breathing.fire)
                print(name + ":", att)

            elif breathing.teknik == "Water":
                att = random.choice(breathing.water)
                print(name + ":", att)

            elif breathing.teknik == "Sun":
                att = random.choice(breathing.sun)
                print(name + ":", att)
            
            elif breathing.teknik == "Moon":
                att = random.choice(breathing.moon)
                print(name + ":", att)

            elif breathing.teknik == "Strom":
                att = random.choice(breathing.strom)
                print(name + ":", att)

            elif breathing.teknik == "Wind":
                att = random.choice(breathing.wind)
                print(name + ":", att)

        else:
            if side.userSide != "Traveler":
                print("You attack enemy use", weaponName)
            else:
                pass

        time.sleep(1)
        totalDamage = playerDamage + dmgBonus
        print("You hit the enemy")
        time.sleep(1)
        atk.showDamage(totalDamage)
        enemyHP -= totalDamage

        if enemyHP <= 0:
            print("you win")
            addHistory("Win")
            if clan.clan == "Uciha" or clan.clan == "Hyuga":
                clan.ability +=1
                clan.getEye()
                if clan.eye != "Normal eye":
                    clan.eyeAbility +=1
                    clan.updateEye()
            
            time.sleep(1)
            print("Dracon +35")
            if money >= 10000:
                print("+0 dracon")
                time.sleep(1)
                runGame
            else:
                money += 35
                runGame()

        time.sleep(2)
        clear()
        print("Enemy Turn")
        time.sleep(2)
        if clan.eye != "Normal eye":
            if clan.eye == "Sharingan":
                print("You  dodge Use sharingan")
                clan.eyeAbility +=1
                clan.updateEye()
                time.sleep(1)
                foundEnemy()
            elif clan.eye == "Mangekyo sharingan":
                print("You  dodge Use Mangekyō sharingan")
                time.sleep(1)
                print("You attack use Amaterasu (Eye power)")
                clan.eyeAbility +=1
                clan.updateEye()
                enemyHP -= 15
                time.sleep(1)
                print("Enemy get attack use", clan.eye)
                time.sleep(1)
                foundEnemy()
            elif clan.eye == "Rinnegan":
                print("You  dodge Use Rinnegan")
                clan.eyeAbility +=1
                clan.updateEye()
                time.sleep(1)
                print("You attack use Rikudo no Jutsu")
                enemyHP -= 100
                time.sleep(1)
                print("Enemy get attack use", clan.eye)
                time.sleep(1)
                foundEnemy()
            elif clan.eye == "Byakugan" or clan.eye == "Jougan":
                print("You dodge use Byakugan")
                time.sleep(1)
                clan.eyeAbility +=1
                foundEnemy()
        atk.showDamage(enemyDamage)
        playerHP -= enemyDamage

        if playerHP <= 0:
            print("You Lose")
            addHistory("Lose")
            time.sleep(3)
            exit()
        foundEnemy()

        if playerHP <= 0:
            print("you lose")
            addHistory("Lose")
            time.sleep(1)
            print("Dracon -20")
            money -= 20
            time.sleep(1)
            exit()
        foundEnemy()
    if choised == 2:
        print("You run from enemy")
        addHistory("Run")
        time.sleep(2)
        print("Dracon -5")
        money -= 5
        time.sleep(2)
        runGame()


def showShopMenu():

    clear()

    if side.userSide == "Knight":
        print("WELCOME TO ISEKAI STORE")
    elif side.userSide == "Demon":
        print("WELCOME TO BLACK MARKET")
    elif side.userSide == "Ninja":
        print("WELCOME TO NINJA SHOP")
    elif side.userSide == "DragonSlayer":
        print("No shop accepts you")
        time.sleep(1)
        print(name + ": Why people hate me?")
        time.sleep(1)
        print(name + ": Because i am dragon slayer?")
        time.sleep(3)
        runGame()

    if side.userSide == "Ninja":
        print("Shuriken(25$)\nKunai(15$)\nJutsu(35$)")
        ninjaSelect = input("Input Weapon Name:")
        if ninjaSelect == "":
            showShopMenu()
        else:
            buyNinjaWeapon(ninjaSelect)

    elif side.userSide != "Ninja":
        print("Excalibur (50$)\nDiamond Katana(15$)\nDurendal(25$)\nYoru(100)")
        select = input("Input Weapon Name:")
        if select == "":
            showShopMenu()
        else:
            buyWeapon(select)


def buyNinjaWeapon(wp):
    clear()
    global weaponName
    global dmgBonus
    global money
    if wp == "Shuriken":
        if money < 25:
            print("You need 25 Dracon For Buy", wp)
            time.sleep(1)
            runGame()
        else:
            dmgBonus = 0
            money -= 25
            weaponName = "Shuriken"
            dmgBonus = 15
            addInvntory(weaponName, dmgBonus)
            runGame()
    if wp == "Kunai":
        if money < 15:
            print("You need 15 Dracon For Buy", wp)
            time.sleep(1)
            runGame()
        else:
            dmgBonus = 0
            money -= 15
            weaponName = "Kunai"
            dmgBonus = 10
            addInvntory(weaponName, dmgBonus)
            runGame()
    if wp == "Jutsu":
        if money < 35:
            print("You need 35 Dracon For Buy", wp)
            time.sleep(1)
            runGame()
        else:
            dmgBonus = 0
            money -= 35
            weaponName = "Jutsu"
            dmgBonus = 25
            addInvntory(weaponName, dmgBonus)
            ninjutsu.getElement()
            time.sleep(1)
            runGame()


def buyWeapon(wp):
    clear()
    global weaponName
    global dmgBonus
    global money
    if wp == "Excalibur":
        if money < 50:
            print("You Need 50 Dracon For buy", wp)
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "Excalibur"
            dmgBonus += 35
            money -= 50
            addInvntory(weaponName, dmgBonus)
            runGame()
    if wp == "Diamond Katana":
        if money < 15:
            print("You Need 15 Dracon For buy", wp)
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "Diamond Katana"
            dmgBonus += 15
            money -= 50
            addInvntory(weaponName, dmgBonus)
            runGame()
    if wp == "Durendal":
        if money < 25:
            print("You Need 25 Dracon For buy", wp)
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "Durendal"
            dmgBonus += 25
            money -= 25
            addInvntory(weaponName, dmgBonus)
            runGame()
    if wp == "Yoru":
        if money < 100:
            print("You Need 100 Dracon For Buy", wp)
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "Yoru"
            dmgBonus += 65
            money -= 100
            addInvntory(weaponName, dmgBonus)
            runGame()

def hospitalMenu():
    global money
    global playerHP
    if money < 5:
        print("tou need 5 Dracon")
        time.sleep(2)
        print("")
        runGame()
    else:
        playerHP = 100
        print("done +100Hp")
        money -= 5
        time.sleep(2)
        print("")
        runGame()

def insertData():
    with open(database, "r") as f:
        cache = json.load(f)
    cache["name"] = name
    cache["dracon"] = str(money)
    cache["damage"] = str(dmgBonus)
    cache["weapon"] = weaponName
    cache["side"] = side.userSide
    cache["clan"] = clan.clan
    cache["ninpo"] = ninjutsu.elemen
    cache["vision"] = vision.vision
    cache["eye"] = clan.eye
    cache["ability"] = str(clan.ability)
    cache["eyeAbility"] = str(clan.eyeAbility)
    cache["breath"] = breathing.teknik
    cache["health"] = str(playerHP)

    with open (database, "w") as f:
        json.dump(cache, f, indent=4)
        print(cache.items(), "Has saved to database")

def loadData():
    global money, dmgBonus, weaponName, playerHP, need_save

    with open (database, "r") as f:
        cache = json.load(f)
        if cache["name"] == "":
            need_save = 1
            pass
        elif cache["name"] != "":
            if name == cache["name"]:
                money = int(cache["dracon"])
                dmgBonus = int(cache["damage"],)
                weaponName = cache["weapon"]
                side.userSide = cache["side"]
                clan.clan = cache["clan"]
                ninjutsu.elemen = cache["ninpo"]
                vision.vision = cache["vision"]
                clan.eye = cache["eye"]
                clan.ability = int(cache["ability"])
                clan.eyeAbility = int(cache["eyeAbility"])
                breathing.teknik = cache["breath"]
                playerHP = int(cache["health"])
                need_save = 0
            else:
                exit()
    print("Data 100 loaded")


def runGame():
    global enemyHP
    global playerHP
    global weaponName
    global dmgBonus
    global money
    clear()
    if side.userSide == "DragonSlayer":
        weaponName = "DragonArt"
        dmgBonus = 35
    if side.userSide == "Ninja":
        print("Hello", clan.clan, name)
    if side.userSide != "Ninja":
        print("Hello", name)
    print("This Is Your Stats:")
    if side.userSide == "Traveler":
        print("Health:", playerHP, "Dracon:", fmt_money.FormatMoney(money), "\tvision:", vision.vision,
          "\tHealthPoin:", playerHP, "\nDamageBonus:", dmgBonus, "Role:",
          side.userSide)
    elif side.userSide != "Traveler":
        print("Health:", playerHP, "Dracon:", fmt_money.FormatMoney(money), "\tWeapon:", weaponName,
            "\tHealthPoin:", playerHP, "\nDamageBonus:", dmgBonus, "Role:",
            side.userSide)
    if clan.clan == "Uciha" or clan.clan == "Hyuga":
        print("Eye:", clan.eye, "\tAbility:", clan.ability, "\tEye Ability:", clan.eyeAbility)
    if side.userSide == "Demon Slayer":
        print("Breathing Style:", breathing.teknik)
    if side.userSide == "Ninja":
        print("Element:", ninjutsu.elemen)
    print("1.Search Enemy\n2.Hospital\n3.Shop\n4.Gacha\n5.Show history\n6.Inventory\n7.Exit")
    select = input("")
    if select == "1":
        enemy.getEnemy()
        time.sleep(2)
        enemyHP = 100
        foundEnemy()
    elif select == "3":
        showShopMenu()
    elif select == "2":
        hospitalMenu()
    elif select == "6":
        selectWeapon()
    elif select == "4":
        if money >= 15:
            gacha.gachaWeapon()
            money -= 15
            time.sleep(3)
            dmgBonus = gacha.damage
            weaponName = "%s" % gacha.weapon
            gachaHistory(weaponName, dmgBonus)
            addInvntory(weaponName, dmgBonus)
            runGame()
        else:
            print("You need 15 Dracon For gacha")
            time.sleep(1)
            runGame()
    elif select == "5":
        showHistory()
    elif select == "7":
        insertData()
        exit()


#run all script
clear()
name = input("Pleasee input your name:")
loadData()

if need_save == 1:
    clear()
    print("Select You Role:")
    print("1.Knight\n2.Demon\n3.Ninja\n4.DragonSlayer\n5.Demon Slayer\n6.Traveler")
    role = input("")

    if role == "1":
        side.userSide = "Knight"

    elif role == "2":
        side.userSide = "Demon"

    elif role == "3":
        side.userSide = "Ninja"
        weaponName = "Taijutsu"
        clan.getClan()
        if clan.clan == "Senju":
            ninjutsu.elemen = "Mokuton"
            weaponName = "Jutsu"
            dmgBonus = 25
        time.sleep(1)

    elif role == "4":
        side.userSide = "DragonSlayer"

    elif role == "5":
        side.userSide = "Demon Slayer"
        weaponName = "Nichirin Sword"
        breathing.getBreath()
        dmgBonus = 35

    elif role == "6":
        side.userSide = "Traveler"
        vision.getVision()
        dmgBonus = 35

runGame()