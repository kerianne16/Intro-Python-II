from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
        "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, fallingkeri
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Items in rooms
ham = Item('ham', 'Looks good!')
sword = Item('sword', 'Stick \'um with the pointy end.')
dog = Item('dog', 'lets be friends')

room['foyer'].items = [dog]
room['overlook'].items = [sword]
room['narrow'].items = [ham]

#Inventory

inventory = []

def tryDirection(d, currentRoom):
    attrib = d +'_to'

    if hasattr(currentRoom, attrib):
        return getattr(currentRoom, attrib)

    else: 
        print('You can\'t go there')
    
    return currentRoom
#
# Main
#
movement = ["n", "s", "e", "w"]

getStarted = input("Welcome to my house of Rooms! \n What is your name? ")
print(f'Nice to meet you, {getStarted}.')



# Make a new player object that is currently in the 'outside' room.
player = Player(getStarted, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

done = False

while not done:

    print("\n{}\n{}".format(player.currentRoom.name, player.currentRoom.description))
    print("You look around and see: {} ".format(player.currentRoom.items))
    if len(player.currentRoom.items) > 0:
            keep_it = input('Do you want to keep the {}? (y/n)'.format(player.currentRoom.items))
            if keep_it.strip().casefold() == 'y':
                    inventory.append(player.currentRoom.items)
                    player.currentRoom.items = []
                    print(inventory)
                    continue


    s= input(" What direction should we go now? \nCommand> ").strip().lower().split()

    if s[0] == "q" or s[0] == "Q":
        done = True

    elif s[0] == 'h':
        print("HELP MENU:\n i:inventory \n d: drop from inventory \n q: quit \n\n DIRECTIONS: \n n:north \n s:south \n e:east \n w:west ")
    
    elif s[0] == 'i' or s[0] == 'I':
            index = 0
            for i in inventory:
                    index += 1
                    print(f'{index}.{i}')
            if len(inventory) == 0:
                    print('There is nothing in your inventory')
    
    elif s[0] == 'd' or s[0]=='D':
            index = 0
            for i in inventory:
                    index += 1
                    print(f'{index}.{i}')
            remove = input('what should we remove from your inventory? (choose the number): ' )
            inventory.remove(inventory[int(remove)-1]) 
    
    elif s[0] in movement:
        player.currentRoom = tryDirection(s[0], player.currentRoom)    
    else:
        print("unknown command {}".format(' '.join(s)))