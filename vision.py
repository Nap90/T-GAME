import random
vision = ""
pVision =["Anemo", "Electro", "Pyro", "Hydro", "Dendro", "Geo", "Cryo"]

def getVision():
    global vision
    global pVision

    myVision = random.choice(pVision)
    vision = myVision

    print("Your vision is", vision)