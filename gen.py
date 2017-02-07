import random

lists = [[["Mollusk", "crab, lobster", "squid. mudskipper", "fish - deep sea", "jellyfish, octopus", "fish - freshwater", "whale, dolphin", "shell", "eel, leech", "coral, anemone", "shark, ray"],["worm", "ant", "mosquito", "moth, butterfly", "fly, dragonfly", "lotus, mantis", "bee, wasp", "caterpillar", "beetle, scarab", "flea, mite", "spider"],["sheep, cow", "mouse, rabbit", "pig, boar", "deer, pronghorn", "ram, bull, buck", "elephant, giraffe"],["crocodile, gila", "frog, newt", "lizard, snake", "turtle"],["wild fowl, duck", "farm fowl, rooster", "seabird, penguin", "city-raven, sparrow", "tropical-parrot, heron", "bird of prey-hawk, owl"],["bat", "bear", "lupine- wild dog", "horse, zebra", "feline-wild cat", "primate"]],
[["seaweed", "fern", "desert cacti", "thick leaf-jade", "flower-domestic", "vine", "poppy", "grass-dandelion", "bamboo", "flower-wild", "carnivorous"],["asparagus", "pinecone", "berry, grapes", "ginger", "tree fruit(apple, orange)", "bean", "pumpkin, gourd", "broccoli, artichoke", "corn", "grain, wheat", "pineapple"],["moss", "ooze, jellu", "lichen", "mushroom"],["willow", "birch", "maple, oak", "banyan", "pine", "palm"]],
[["fire, vapor", "electric bolt", "ember, hot coal", "molten lava"],["icicles", "fog, vapor", "wave", "dew drops", "ripple", "frost, snow", "suds, bubbles", "tar, gum"],["malachite", "mountain, cliff face", "brick, cobblestone", "rust, oxide", "cracked clay", "stalactite, stalagmite", "glass, crystals", "powder, sand", "slate, shale", "cement, sediment", "mercury, chrome"],["moon cycles", "starfield", "crater, asteroid", "solar flare", "galaxy form", "volcano", "planets, saturn's rings", "cloud, cyclone"]],
[["car, truck, bus", "aircraft", "rail, train, trolley", "cycle", "sled, ski", "boat, ship", "spacecraft", "tank tread"],["ornament, gargoyle", "bridge, framework", "castle, domed", "ornament, pillar", "modern skyscraper", "place of worship, totem", "doorway, archway", "old village, cottage],["drill", "cups, plates", "umbrella", "bundle, bale", "hammer, axe", "brush- hair, tooth", "razor, knife", "spigot, faucet", "rope", "silverware", "lock, key"],["switch, dial, button", "turbine", "bulb, lamp", "clock, gears", "fan, propeller", "saw"],["adhesive, bandage", "shovel, pick", "capsule, tablet", "nuts, bolts", "chain", "thread, stitch", "shears, scissors", "pen, paintbrush", "spring, coil", "syringe", "tube, plumbing"],["reactor core", "telephone", "solar panel", "engine", "laser beam", "microchip", "dish antenna", "rocket"]]]

emotactlists = [["embarrassed", "anger", "timid, bashful", "giggling, smiling", "squint, wink", "bored", "stressed, fatigued", "fear", "thought, meditation", "deadpan", "insane, berserker", "insane, happy", "pining, furrowed", "laughing, hysterical", "attentive, shock", "stern, grumpy", "clenched teeth", "gape, gawk", "relief", "sneering", "paranoid, shifty", "bliss, joy", "confusion"],
["recoil, akimbo", "drenched, thirst", "blown by cyclone", "push, pull", "snoop, listen", "crouched for attack", "hang, climb", "recoil, head/torso", "float, levitate", "swinging weapon", "twisting, stretching", "kicking, punching", "squeeze, tackle", "absorb, eat", "limp, injured", "curse, swear", "run, jump", "melt, glow, fire", "stuck, trapped", "pull, push", "shoot weapon", "dying, gaunt", "fly, swim", "shed, molting", "chant, recite", "punch, kick", "crawl, emerge"]]

ln0 = len(lists[1])-1
ln1 = len(lists[2])-1
ln2 = len(lists[3])-1
ln3 = len(lists[4])-1

ln4 = len(emotactlists[1])
ln5 = len(emotactlists[2])

pick1 = random.randint(0,ln0)
pick2 = random.randint(0,ln1)
pick3 = random.randint(0,ln2)
pick4 = random.randint(0,ln3)
pickemot = random.randint(0,ln4)
pickact = random.randint(0,ln5)

print(lists[pick1])
print(lists[pick2])
print(lists[pick3])
print(lists[pick4])
print(emotactlists[pickemot])
print(emotactlists[pickact])
