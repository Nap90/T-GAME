import side
import random
clan = ""
pClan =["Uciha", "Hyuga", "Senju", "Uzumaki"]

def getClan():
    global pClan
    global clan

    usrClan = random.choice(pClan)
    clan = usrClan
    print("Your clan is:", clan)

eye = "Normal eye"
ability = 0
eyeAbility = 0

def getEye():
    global ability
    global eye
    if clan == "Uciha":
        if ability == 5:
            eye = "Sharingan"
    elif clan == "Hyuga":
        if ability == 5:
            eye = "Byakugan"

def updateEye():
    global ability
    global eye

    if clan == "Uciha":
        if eyeAbility >= 5:
            eye = "Mangekyo sharingan"
        if eyeAbility >= 10:
            eye = "Rinnegan"
    if clan == "Hyuga":
        if eyeAbility >=5:
            eye = "Jougan"

