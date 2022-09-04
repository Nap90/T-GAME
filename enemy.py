import side
import random

villainEnemy = ["Knight", "King", "Bounty Hunter", "DragonSlayer", "DevilKing", "Demon slayer"]

knightEnemy = [
    "Skeleton", "Dragon", "Treasure Hunter", "DragonSlayer", "Devil King"
]

ninjaEnemy = [
    "Fugutive", "Swordman", "Daimyo BodyGuard", "Dragon", "DragonSlayer"
]

dragonSlayerEnemy = [
    "Dragon", "Knight", "Main Villain", "Ninja", "Guild Member",
    "Master Guild", "Kurozawa Descendants"
]

demonSlayerEnemy =[
    "Upper Moon", "Down moon", "Normal demon", "Muzan", "DragonSlayer"
]

travelerEnemy =[
    "Fatui", "Fatui harbinger", "DragonSlayer", "Slime", "Devil"
]

def getEnemy():
    global lawan
    if side.userSide == "Demon":
        lawan = random.choice(villainEnemy)
        print("Your Enemy Is:" + lawan)
    if side.userSide == "Knight":
        enemyK = random.choice(knightEnemy)
        print("Your Enemy Is:" + enemyK)
    if side.userSide == "Ninja":
        lawan = random.choice(ninjaEnemy)
        print("Your Enemy Is", lawan)
    if side.userSide == "Demon Slayer":
        lawan = random.choice(demonSlayerEnemy)
        print("Your enemy  is", lawan)
    if side.userSide == "DragonSlayer":
        lawan = random.choice(dragonSlayerEnemy)
        print("You enemy is", lawan)
        if lawan == "Dragon":
            print("This time i will stop you")
    if side.userSide == "Traveler":
        lawan = random.choice(travelerEnemy)
        print("Your enemy is", lawan)