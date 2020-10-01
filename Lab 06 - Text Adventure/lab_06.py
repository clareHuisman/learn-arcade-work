class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    """Creates list of rooms on castle property"""
    room = Room("You are in the library. There is a strange trapdoor in the ceiling.\n"
                "There is a passage to the north and east.", 3, 1, None, None)
    room_list.append(room)

    room = Room("You are in the study. There is a passage to the north, east, and west.", 4, 2, None, 0)
    room_list.append(room)

    room = Room("You are in the ballroom. Maybe you should try dancing.\n"
                "There is a passage to the north and west.", 5, None, None, 1)
    room_list.append(room)

    room = Room("You are in a bedroom with a window overlooking the lake outside.\n"
                "There is a passage to the north, south, and east.", 6, 4, 0, None)
    room_list.append(room)

    room = Room("You are in the bathroom. There is a passage to the south, east, and west.", None, 5, 1, 3)
    room_list.append(room)

    room = Room("You are in a bedroom. The bed is unkept and the room is a mess. Who sleeps here?\n"
                "There is a passage to the north, south, and west.", 7, None, 2, 4)
    room_list.append(room)

    room = Room("You are in the kitchen. There are some homemade muffins on the counter.\n"
                "There is a passage to the south.", None, None, 3, None)
    room_list.append(room)

    room = Room("You are in the dining room. The table is set for three. Is someone else here?\n"
                "There is a passage to the south and west.", None, None, 5, 8)
    room_list.append(room)

    room = Room("You are in the courtyard. The flowers look lovely here, and you can see the lake.\n"
                "There is a door to the east, stables to the north, and a guest house to the west.", 9, 7, None, 13)
    room_list.append(room)

    room = Room("You are in the stables. You can hear a horse, but can't see it.\n"
                "There is a passage to the north, south, east, and west.", 11, 10, 8, 12)
    room_list.append(room)

    room = Room("You are in one of the stalls. You can hear a horse, but can't see it.\n"
                "There is a passage to the west.", None, None, None, 9)
    room_list.append(room)

    room = Room("You are in one of the stalls. There is a beautiful black stallion here!\n"
                "There is a passage to the south.", None, None, 9, None)
    room_list.append(room)

    room = Room("You are in one of the stalls. You can hear a horse, but can't see it.\n"
                "There is a door to the east and west.", None, 9, None, 8)
    room_list.append(room)

    room = Room("You are in the guest house. There are fresh cut flowers in a vase on the table.\n"
                "There is a passage to the north, south, and west.", 14, None, 8, 16)
    room_list.append(room)

    room = Room("You are in the guest bedroom. The view to the lake is even better here.\n"
                "There is a passage to the south and west.", None, None, 13, 15)
    room_list.append(room)

    room = Room("You are in the guest bathroom. There is a passage to the east.", None, 14, None, None)
    room_list.append(room)

    room = Room("You are in a study. Why would the guests have their own study?\n"
                "There is a passage to the east and west.", None, 13, None, 8)
    room_list.append(room)

    current_room = 0
    done = False
    print("You have entered an abandoned castle in the woods.")

    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("Where would you like to go? ")
        if user_choice.lower() == "n" or user_choice.lower() == "north":
            """Moves user one room to the north if it exists"""
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        elif user_choice.lower() == "s" or user_choice.lower() == "south":
            """Moves user one room to the south if it exists"""
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        elif user_choice.lower() == "e" or user_choice.lower() == "east":
            """Moves user one room to the east if it exists"""
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        elif user_choice.lower() == "w" or user_choice.lower() == "west":
            """Moves user one room to the west if it exists"""
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        elif user_choice.lower() == "d" or user_choice.lower() == "dance":
            """Tells the user that they can't dance"""
            print()
            print("You don't have time for that right now.")

        elif user_choice.lower() == "u" or user_choice.lower() == "up":
            """Tells the user they can't go up"""
            print()
            print("You aren't tall enough to reach that.")

        elif user_choice.lower() == "r" or user_choice.lower() == "ride":
            """Tells the user they can't ride the horse"""
            print()
            print("You don't know how to ride a horse!")

        elif user_choice.lower() == "q" or user_choice.lower() == "quit":
            """Quits the game"""
            print()
            print("You quit!")
            done = True

        else:
            """Tells the user that what they said is not part of the game """
            print()
            print("I don't understand what you mean.")


main()
