import random

anima = ["sealife", "insect", "mammal_a", "reptile", "bird", "mammal_b"]
sealife = ["Mollusk", "crab, lobster", "squid. mudskipper", "fish - deep sea", "jellyfish, octopus", "fish - freshwater", "whale, dolphin", "shell", "eel, leech", "coral, anemone", "shark, ray"]
insect = ["worm", "ant", "mosquito", "moth, butterfly", "fly, dragonfly", "lotus, mantis", "bee, wasp", "caterpillar", "beetle, scarab", "flea, mite", "spider"]
mammal_a = ["sheep, cow", "mouse, rabbit", "pig, boar", "deer, pronghorn", "ram, bull, buck", "elephant, giraffe"]
reptile = ["crocodile, gila", "frog, newt", "lizard, snake", "turtle"]
bird = ["wild fowl, duck", "farm fowl, rooster", "seabird, penguin", "city-raven, sparrow", "tropical-parrot, heron", "bird of prey-hawk, owl"]
mammal_b = ["bat", "bear", "lupine- wild dog", "horse, zebra", "feline-wild cat", "primate"]

veggie = ["plant", "fruitveg", "fungi", "tree"]
plant = ["seaweed", "fern", "desert cacti", "thick leaf-jade", "flower-domestic", "vine", "poppy", "grass-dandelion", "bamboo", "flower-wild", "carnivorous"]
fruitveg = ["asparagus", "pinecone", "berry, grapes", "ginger", "tree fruit(apple, orange)", "bean", "pumpkin, gourd", "broccoli, artichoke", "corn", "grain, wheat", "pineapple"]
fungi = ["moss", "ooze, jellu", "lichen", "mushroom"]
tree = ["willow", "birch", "maple, oak", "banyan", "pine", "palm"]

element = ["fire", "liquid", "earth", "astral"]
fire = ["fire, vapor", "electric bolt", "ember, hot coal", "molten lava"]
liquid = ["icicles", "fog, vapor", "wave", "dew drops", "ripple", "frost, snow", "suds, bubbles", "tar, gum"]
earth = ["malachite", "mountain, cliff face", "brick, cobblestone", "rust, oxide", "cracked clay", "stalactite, stalagmite", "glass, crystals", "powder, sand", "slate, shale", "cement, sediment", "mercury, chrome"]
astral = ["moon cycles", "starfield", "crater, asteroid", "solar flare", "galaxy form", "volcano", "planets, saturn's rings", "cloud, cyclone"]

techne = ["transportation", "architecture", "tool_a", "machine_a", "tool_b", "machine_b"]
transportation = ["car, truck, bus", "aircraft", "rail, train, trolley", "cycle", "sled, ski", "boat, ship", "spacecraft", "tank tread"]
architecture = ["ornament, gargoyle", "bridge, framework", "castle, domed", "ornament, pillar", "modern skyscraper", "place of worship, totem", "doorway, archway", "old village, cottage"]
tool_a = ["drill", "cups, plates", "umbrella", "bundle, bale", "hammer, axe", "brush- hair, tooth", "razor, knife", "spigot, faucet", "rope", "silverware", "lock, key"]
machine_a = ["switch, dial, button", "turbine", "bulb, lamp", "clock, gears", "fan, propeller", "saw"]
tool_b = ["adhesive, bandage", "shovel, pick", "capsule, tablet", "nuts, bolts", "chain", "thread, stitch", "shears, scissors", "pen, paintbrush", "spring, coil", "syringe", "tube, plumbing"]
machine_b = ["reactor core", "telephone", "solar panel", "engine", "laser beam", "microchip", "dish antenna", "rocket"]

emotactlists = [["embarrassed", "anger", "timid, bashful", "giggling, smiling", "squint, wink", "bored", "stressed, fatigued", "fear", "thought, meditation", "deadpan", "insane, berserker", "insane, happy", "pining, furrowed", "laughing, hysterical", "attentive, shock", "stern, grumpy", "clenched teeth", "gape, gawk", "relief", "sneering", "paranoid, shifty", "bliss, joy", "confusion"],
["recoil, akimbo", "drenched, thirst", "blown by cyclone", "push, pull", "snoop, listen", "crouched for attack", "hang, climb", "recoil, head/torso", "float, levitate", "swinging weapon", "twisting, stretching", "kicking, punching", "squeeze, tackle", "absorb, eat", "limp, injured", "curse, swear", "run, jump", "melt", "glow", "fire", "stuck, trapped", "pull, push", "shoot weapon", "dying, gaunt", "fly, swim", "shed, molting", "chant, recite", "punch, kick", "crawl, emerge"]]

ln0 = len(anima)-1
ln1 = len(veggie)-1
ln2 = len(element)-1
ln3 = len(techne)-1

lnsealife = len(sealife)-1

ln4 = len(emotactlists[0])-1
ln5 = len(emotactlists[1])-1

pick0 = random.randint(0,ln0)
pick1 = random.randint(0,ln1)
pick2 = random.randint(0,ln2)
pick3 = random.randint(0,ln3)
pickemot = random.randint(0,ln4)
pickact = random.randint(0,ln5)

def listpicker(listpick):
    if listpick == "sealife":
        ln = len(sealife)-1
        pick = random.randint(0, ln)
        print(sealife[pick])
    elif listpick == "insect":
        ln = len(insect)-1
        pick = random.randint(0, ln)
        print(insect[pick])
    elif listpick == "mammal_a":
        ln = len(mammal_a)-1
        pick = random.randint(0, ln)
        print(mammal_a[pick])
    elif listpick == "reptile":
        ln = len(reptile)-1
        pick = random.randint(0, ln)
        print(reptile[pick])
    elif listpick == "bird":
        ln = len(bird)-1
        pick = random.randint(0, ln)
        print(bird[pick])
    elif listpick == "mammal_b":
        ln = len(mammal_b)-1
        pick = random.randint(0, ln)
        print(mammal_b[pick])
    elif listpick == "plant":
        ln = len(plant)-1
        pick = random.randint(0, ln)
        print(plant[pick])
    elif listpick == "fruitveg":
        ln = len(fruitveg)-1
        pick = random.randint(0, ln)
        print(fruitveg[pick])
    elif listpick == "fungi":
        ln = len(fungi)-1
        pick = random.randint(0, ln)
        print(fungi[pick])
    elif listpick == "tree":
        ln = len(tree)-1
        pick = random.randint(0, ln)
        print(tree[pick])
    elif listpick == "fire":
        ln = len(fire)-1
        pick = random.randint(0, ln)
        print(fire[pick])
    elif listpick == "liquid":
        ln = len(liquid)-1
        pick = random.randint(0, ln)
        print(liquid[pick])
    elif listpick == "earth":
        ln = len(earth)-1
        pick = random.randint(0, ln)
        print(earth[pick])
    elif listpick == "astral":
        ln = len(astral)-1
        pick = random.randint(0, ln)
        print(astral[pick])
    elif listpick == "transportation":
        ln = len(transportation)-1
        pick = random.randint(0, ln)
        print(transportation[pick])
    elif listpick == "architecture":
        ln = len(architecture)-1
        pick = random.randint(0, ln)
        print(architecture[pick])
    elif listpick == "tool_a":
        ln = len(tool_a)-1
        pick = random.randint(0, ln)
        print(tool_a[pick])
    elif listpick == "machine_a":
        ln = len(machine_a)-1
        pick = random.randint(0, ln)
        print(machine_a[pick])
    elif listpick == "tool_b":
        ln = len(tool_b)-1
        pick = random.randint(0, ln)
        print(tool_b[pick])
    elif listpick == "machine_b":
        ln = len(machine_b)-1
        pick = random.randint(0, ln)
        print(machine_b[pick])
    print(" ")

print("""

Fantasy Genesis
""")
print(anima[pick0] + ": ")
listpick = anima[pick0]
listpicker(listpick)
print(veggie[pick1] + ": ")
listpick = veggie[pick1]
listpicker(listpick)
print(element[pick2] + ": ")
listpick = element[pick2]
listpicker(listpick)
print(techne[pick3] + ": ")
listpick = techne[pick3]
listpicker(listpick)
print("emotion: ", emotactlists[0][pickemot])
print("action: ", emotactlists[1][pickact])
print(" ")
