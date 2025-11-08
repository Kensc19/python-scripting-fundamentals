#!/usr/bin/env python3
from random import *
from textwrap import *

def unlockSafe(comboD1, comboN1, comboD2, comboN2, comboD3, comboN3):
    firstValid = False
    secondValid = False
    thirdValid = False

    d1 = input("Right or left? (r/l): ")
    n1 = input("Number? ")

    if d1[0].lower() == comboD1[0].lower() and int(n1) == comboN1:
        print("You hear a click.")
        firstValid = True

    d2 = input("Right or left? (r/l): ")
    n2 = input("Number? ")

    if d2[0].lower() == comboD2[0].lower() and int(n2) == comboN2:
        print("You hear a click.")
        secondValid = True

    d3 = input("Right or left? (r/l): ")
    n3 = input("Number? ")

    if d3[0].lower() == comboD3[0].lower() and int(n3) == comboN3:
        print("You hear a click.")
        thirdValid = True

    if firstValid is True and secondValid is True and thirdValid is True:
        print('You unlocked the safe!')
        den[4]['safe'] = 'The safe has a combination lock. But it is unlocked! Inside the safe is a map.'
        den[4]['map'] = 'The map is a treasure map to the hidden treasure of Kiloalto. This must be where the family went! To find the treasure!'
    else:
        print('The safe did not unlock. Please try again.')

def unlockNightstand():
    print(usableItems['key'])
    masterBedroom[4]['nightstand'] = 'The night stand is old and solid-looking. The nightstand drawer is unlocked.'
    masterBedroom[4]['drawer'] = "The drawer has some lotion, a torrid romance novel, and a paper that says 'combination' on it."
    masterBedroom[4]['combination'] = 'Hi Honey, Don\'t forget to feed the dog. I reset the safe combination to {} {} {} {} {} {}. I love you! Your cute little wife :)'.format(comboD1, comboN1, comboD2, comboN2, comboD3, comboN3)

def help():
    print()
    print("Valid Commands:")
    for command in commands:
        print(command)
    print()

def printInventory():
    print('You are holding:')
    for item in inventory.keys():
        print(item)
    print()

# Lists to initialize rooms
# Index 0 will be name
# Index 1 will be the article
# Index 2 is the description
# Index 3 will be the possible directions
# Index 4 will be objects in the room
# Index 5 will be dropped objects in the room.
porch = ['Covered Porch', 'a', 'The porch has dust on the floor but there are recent footprints. In front of you, on the north side, is an old victorian door painted violet. It has an ominous lion\'s head door knocker.', {'n': 'entry'}, {}, {}]
entry = ['Entry', 'the', "Above the foyer, a large chandelier lit with retro lightbulbs weakly illuminates the entry. Someone needs to do some dusting. The entryway faces a stairway to the second floor. \nWest of you, you see a small den. \nTo the east is a living room.", {'climb': 'secondFloor', 'e': 'livingRoom', 'w': 'den'}, {}, {}]
den = ['Den', 'a', 'The den is a cozy room with a woven carpet and a used looking love seat. There is a large desk with a drawer. Against the wall is a bookshelf. In the corner is a large safe. \nThe entry to the house is to the east.', {'e': 'entry'}, {'desk': 'The desk has some papers scattered on the top of it. The desk has a drawer.', 'papers': 'There appear to be a number of unpaid bills and the Last Will and Testiment of Gareth Brookline.', 'drawer': 'In the drawer is an number of photos of a family. The family vaguely resembles the Adaams Family.', 'bookshelf': 'The bookshelf is made of weathered oak and contains a number of leatherbound books.', 'books': 'The books are covered in dust and look just as interesting.', 'safe': 'The safe has a combination lock. It has numbers from 1-40. Guess you will have to find the combination.'}, {}]
livingRoom = ['Living Room', 'the', 'The living room is a hodpodge of centuries. The victorian sofa faces a giant flatscreen TV. On the walls are painted portraits of men and women in old fashioned dress. \nTo the west is the entry to the house. \nTo the north is a dining room.', {'w': 'entry', 'n': 'diningRoom'}, {'portraits': 'The portraits are spooky. In one portrait, a man with menacing eyes has a hand on the sword hung at his belt.', 'tv': 'It\'s a large flatscreen TV.'}, {}]
diningRoom = ['Dining Room', 'the', 'The dining room long table. Eight chairs surround the table, one in front of each place setting. The chair at the head of the table is pushed back as if the host just rose and stepped away. There is a china cabinet off to the side. \nTo the south is a living room. \nTo the west is a kitchen.', {'s': 'livingRoom', 'w': 'kitchen'}, {'candelabra': 'The candelabra looks heavy. Eight candles flicker in its gothic grasp.', 'cabinet': 'Boy, you would hate to have to be part of the moving crew that has to move this! The family\'s finest china is on display in the hutch. There is a drawer under the hutch.', 'drawer': 'In the drawer is a set of birthday candles and a strange looking key.', 'key': 'It looks like a skeleton key.', 'table': 'Besides the place settings, there is a candelabra sitting in the middle of the table.'}, {}]
kitchen = ['Kitchen', 'the', 'Unlike the rest of the house, the kitchen is truly modern. The stove may even be wifi capable and the oven is huge! The stainless steel fridge looks like it must be stocked with lots of goodies. On the front of the fridge is a sticky note. \nTo the south is a small bathroom. \nTo the west is a pantry.', {'s': 'halfBath', 'w': 'pantry', 'e': 'diningRoom'}, {'stove': 'The stove is the finest money can buy! There is a pot on the stove.', 'pot': 'Ugh, someone forgot to put this in the dishwasher.', 'oven': 'There is a batch of brownies baking in the oven.', 'brownies': 'They appear to be a combination of white and chocolate fudge.', 'fridge': 'The only thing in the fridge is an old fashioned bottle of milk. There is a note taped to the fridge.', 'milk': "Wow, you haven't seen a milk bottle like this since the last time you went to a flea market.", "note": "The sticky note says, 'Honey, throw out the milk!'"}, {}]
pantry = ['Pantry', 'the', 'The pantry would make anyone claustrophobic. The shelves are filled with cans and boxes of non-perishable goods. \nTo the east is the kitchen.', {'e': 'kitchen'}, {'shelves': 'The shelves are filled with cans and boxes of non-perishable goods.', 'cans': 'Someone likes tomato soup!', 'boxes': 'No one can eat that much instant mashed potatoes!'}, {}]
halfBath = ['Small Bathroom', 'a',  'This is the kind of half-baths architects put on the main floor to keep guests out of the living area above. There is an antique-looking sink in a mahogany vanity. \nTo the north is the kitchen.', {'n': 'kitchen'}, {'toilet': 'The toilet is immaculate. Must be a guest bathroom.', 'sink': 'The sink is mounted on a mahogany vanity.', 'vanity': 'The antique-looking vanity has a set of doors.', 'doors': 'Inside the vanity are several spare rolls of toilet paper.'}, {}]
secondFloor = ['Second Floor Hallway', 'the', 'As you crest the stairs, you enter the second floor hallway. Another place that could use some dusting!\n To the east and west the hallway continues.', {'w': 'westHall', 'e': 'eastHall', 'climb': 'entry'}, {}, {}]
westHall = ['West Hallway', 'the', 'The west hallway has the same thick pile carpet that desperately needs to be vacuumed. \nTo the north and south are bedrooms.', {'n': 'guestBed1', 's': 'guestBed2', 'e': 'secondFloor'}, {}, {}]
guestBed1 = ['Kid\'s Bedroom', 'a', 'This room looks like it belongs to a teenage girl. Posters of hunky pop starts are taped to the walls between the ancient light scones. The closet door is partially ajar. A small dresser sits against the wall opposite the queen-sized bed with its immaculate, if dusty, comforter. On the wall is a flatscreen TV. \nTo the south is the West Hallway.', {'s': 'westHall'}, {'closet': 'The closet is filled with teenage outfits including a cheerleading outfit and a prom dress.', 'dresser': 'The dresser is filled with color coordinated outfits.', 'tv': 'It\'s a decent sized flatscreen TV. Lucky kid!', 'bed': 'The bed is neatly made with a pink bedspread that needs a wash.'}, {}, {}]
guestBed2 = ['Kid\'s Bedroom', 'a', 'This room clearly belongs to a pre-teen boy if you can judge by the toys. Various action figures are posed around the room, caught in the act of battling for truth and justice. The dresser drawers have rather modern clothing spilling over the top where they were not quite pushed in all the way. The closet door is wide open. On the wall is a flatscreen TV. \nTo the north is the West Hallway.', {'n': 'westHall'}, {'dresser': 'The dresser drawers have rather modern clothing spilling over the top where they were not quite pushed in all the way.', 'closet': 'The closet has a pile of dirty laundry that would take an oxygen tank to summit.', 'tv': 'It\'s a decent sized flatscreen TV. Lucky kid!', 'bed': 'The sheets are rumpled as if the sleeper jumped out of bed and rushed out to play.'}, {}]
eastHall = ['East Hallway', 'the', 'The east hallway has the same thick pile carpet that desperately needs to be vacuumed.\nTo the north is a small bathroom that looks like its used by children. \nTo the south is a door leading to the master bedroom.', {'n': 'kidsBath', 's': 'masterBedroom', 'w': 'secondFloor'}, {}, {}]
kidsBath = ["Kid's Bathroom", 'the', 'The kids may have done a good job of cleaning themselves in this room, but the room itself needs some love. In the bathroom is a toilet, a sink, and a vanity with a drawer.\nTo the south is the East Hallway.', {'s': 'eastHall'}, {'toilet': 'The toilet could use a good cleaning.', 'sink': 'The sink is perhaps the most frightening thing you have seen yet. Is that petrified toothpaste?', 'vanity': 'As you start to open the vanity, a mountain of empty bottles starts to spill out. You quickly close it.'}, {}]
masterBedroom = ['Master Bedroom','the', 'The master bedroom has a king-size canopy bed. The comforter is made of rich damask in a medieval pattern. At the side of the bed is a nightstand. Hanging over the large dresser on the opposite side is a flatscreen TV.\nTo the northeast is the master bath. \nTo the north is the East Hallway.', {'n': 'eastHall', 'ne': 'masterBath'}, {'bed': 'The king-size bed is massive. The comforter is made of rich damask in a medieval pattern. The pillows look inviting. If only they weren\'t so dusty!', 'nightstand': 'The night stand is old, solid-looking and the drawer is locked. It looks like it needs a skeleton key to unlock it.', 'tv': 'With a TV this large, why would anyone need to get up?', 'drawer': 'The drawer is locked.'}, {}]
masterBath = ['Master Bathroom', 'the', 'The master bathroom features a double-sink mounted on a antique-style vanity that has a drawer. There is a deep claw-footed soaking tub. The proceline commode looks just as old. A closet at the back of the bathroom has a stack of bath towels that would be fluffy if they were washed. \nTo the south is the master bedroom.', {'s': 'masterBedroom'}, {'vanity': 'Who knew they made double sink vanities in the 19th century?', 'tub': 'It\'s a deep claw-footed soaking tub. Unlike everything else in the house, it\'s sparkling clean.', 'drawer': 'The drawer is filled with hairbands and empty toothpaste tubes.', 'commode': 'The toilet seat is up and the water still looks faintly blue.'}, {}]

commands = ["look at [object]", "take [object]", "climb (stairs; either up or down)", "use [object]", "n (move north)", "s (move south)", "e (move east)", "w (move west)", "ne (move northeast)", "inventory (display items in inventory", "drop [object] (remove object from inventory)", "Unlock (unlock an item)","help (display commands)", "q (quit game)"]

usableItems = {'milk': 'Yuck! Defnitely spoiled!', 'brownies': 'Yum! Delicious!', 'key': 'The key worked! The drawer is unlocked!'}

takeableItems = {'papers': ['desk', 'The top of the desk is bare.'], 'photos': ['drawer', 'The drawer is empty.'], 'candelabra': ['table', 'The table is set for four. It looks as if the family just stepped away.'], 'key': ['drawer', 'In the drawer is a set of birthday candles.'], 'brownies': ['oven', 'There is nothing in the oven.'], 'milk': ['fridge', 'There is nothing in the fridge.'], 'cans': ['shelves'], 'boxes': ['shelves'], 'combination': ['drawer', "The drawer has some lotion and a torrid romance novel."], 'map': ['safe', 'The safe is empty']}

gameWon = False
move = ''
room = 'porch'
inventory = {}
descriptionDisplayed = False
safeDirections = ["left", "right"]
comboD1 = choice(safeDirections)
comboN1 = randint(1,40)
comboD2 = choice(safeDirections)
comboN2 = randint(1,40)
comboD3 = choice(safeDirections)
comboN3 = randint(1,40)

print("Welcome to the text adventure!")
print("Your task is to find the secret treasure map")
print("which is hidden inside this spooky house!")
answer = input("Are you up to the challenge? (y/n) ")

while not (answer[0].lower() == 'y' or answer[0].lower() == 'n'):
    print("I'm sorry, I didn't understand. Please try again.")
    answer = input("Are you up to the challenge? (y/n) ")

if answer[0].lower() == 'n':
    print('It can be intimidating! Gather your courage and return.')
    move = 'q'
else:
    print('Excellent!')
    help()


while move != 'q' and gameWon is False:

    code1 = 'roomName = '+room+'[0]'
    code2 = 'roomArticle = '+room+'[1]'
    code3 = 'roomDescription = '+room+'[2]'
    code4 = 'directions = '+room+'[3]'
    code5 = 'roomObjects = '+room+'[4]'
    code6 = 'droppedObjects = '+room+'[5]'

    exec(code1)
    exec(code2)
    exec(code3)
    exec(code4)
    exec(code5)
    exec(code6)

    print(roomName)
    print('You are standing in '+roomArticle+' '+roomName.lower()+'.')

    if descriptionDisplayed is False:
        print(fill(roomDescription))
    descriptionDisplayed = True
    
    if len(droppedObjects) >= 1:
        print("On the floor you see:")
        for object in droppedObjects:
            print(object)
        print()

    move = input('What would you like to do? ')

    if len(move) > 1:
        move = move.lower().split()
    else:
        move = move.lower()

    if move[0] == 'q':
        print('Cowering in fright, you run screaming from the house.')
        print('It can be intimidating! Gather your courage and return.')
        break
    elif move[0] in directions:
        room = directions[move[0].lower()]
        descriptionDisplayed = False
    elif move[0] == 'help':
        help()
        continue
    elif move[0] == 'look':
        if len(move) == 1:
            descriptionDisplayed = False
            continue
        elif move[-1] in roomObjects:
            print(fill(roomObjects[move[-1]]))
        elif move[-1] in inventory:
            print(fill(inventory[move[-1]]))
        elif move[-1] in droppedObjects:
            print(fill(droppedObjects[move[-1]]))
        else:
            print("I'm sorry, you can't do that.")
    
    elif move[0] == 'take':
        if move[-1] in roomObjects and move[-1] in takeableItems:
            inventory[move[-1]] = roomObjects[move[-1]]
            code7 = "del "+room+"[4]['"+move[-1]+"']"
            exec(code7)
            if move[-1] == 'map':
                printInventory()
                print("As you take the map, a deep sense of pride comes over you.")
                print("You did it!")
                print()
                print("Now you will have to wait for the next version")
                print("of this game to follow the map to the lost treasure!")
                gameWon = True
                break
            elif move[-1] == 'cans' and 'boxes' in roomObjects:
                pantry[4]['shelves'] = 'The shelves contain boxes of non-perishable goods.'
            elif move[-1] == 'cans' and 'boxes' not in roomObjects:
                 pantry[4]['shelves'] = 'The shelves are empty.'
            elif move[-1] == 'boxes' and 'cans' in roomObjects:
                pantry[4]['shelves'] = 'The shelves contain cans of food.'
            elif move[-1] == 'boxes' and 'cans' not in roomObjects:
                pantry[4]['shelves'] = 'The shelves are empty.'
            else:
                code7 = room+"[4]['"+takeableItems[move[-1]][0]+"'] = '"+takeableItems[move[-1]][1]+"'"
                exec(code7)
            printInventory()
            continue
        elif move[-1] in droppedObjects:
            inventory[move[-1]] = droppedObjects/[move[-1]]
            code9 = "del "+room+"[5]['"+move[-1]+"']"
            exec(code9)
            printInventory()
        else:
            print("I'm sorry, you can't do that.")
            continue
    elif move[0] == 'inventory':
        printInventory()
        continue
    elif move[0] == 'drop':
        code8 = room+"[5]['"+move[-1]+"'] = \""+ inventory[move[-1]]+"\""
        exec(code8)
        del inventory[move[-1]]
        
    elif move[0] == 'use':
        if move[-1] in inventory and move[-1] in usableItems:
            if move[-1] == 'key':
                if room == 'masterBedroom':
                    unlockNightstand()
                else:
                    print("The key definitely unlocks something. But you can't use it until you find something locked.")
            else:
                print(usableItems[move[-1]])
        else:
            print("I'm sorry, you can't do that.")
    elif move[0] == 'unlock':
        if room == 'masterBedroom':
            if 'key' in inventory:
                unlockNightstand()
            else:
                print("It looks like you will need a key to unlock that.")
        elif room == 'den':
            unlockSafe(comboD1, comboN1, comboD2, comboN2, comboD3, comboN3)
        else:
            print("I'm sorry, there's nothing here to unlock.")
    else:
        print("I'm sorry, you can't do that.")

print('Goodbye!')