import random
tecnique = ["Fire", "Water", "Sun", "Moon", "Strom", "Wind"]

fire =["Ichi no Kata: Shiranui",
    "Ni no kata: Nobori En Ten.",
    "San no kata: Kien Banjo.",
    "Shi no kata: Sei En no Uneri",
    "Go no kata: Enko",
    "Ku no kata: Rengoku"
]

water =[
    "Ichi no kata: Minamo giri",
    "Ni no kata: Mizu guruma",
    "San no kata: Ryūryū mai",
    "Shi no kata: Uchishio",
    "Go no kata: Kanten no jiu",
    "Roku no kata: Nejire uzu",
]

sun =[
    "Hinokami kagura",
    "Hinokami kagura : Enpu"
]

strom =[
    "Ichi no kata: Hekireki issen",
    "Ni no kata: Inadama",
    "San no kata: Shiubun seirai"
]

wind =[
    "Ichi no kata: Kazekiri",
    "Ni no kata: Fuujin",
    "San no kata: Kaze to tomo ni sare"
]

moon =[
    "Ichi no kata: Meteor moon",
    "Ni no kata: Tsukoyomi",
    "San no kata: Full moon control"
]

teknik = ""

def getBreath():
    global teknik
    teknik = random.choice(tecnique)
    print("Your Breath style is", teknik)