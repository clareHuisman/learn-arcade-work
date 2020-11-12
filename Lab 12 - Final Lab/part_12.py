import arcade
import os

SPRITE_SCALING = 0.1
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Sprite Rooms Example"

MOVEMENT_SPEED = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None

        self.lock_list = None
        self.dragon_list = None
        self.sword_list = None
        self.key_list = None
        self.trophy_list = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.lock_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26:
                # http://www.i2clipart.com/clipart-custom-color-round-square-button-c82a
                wall = arcade.Sprite("blue wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            # Skip making a block 4 and 5 blocks up on the right side
            if y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5 and y != SPRITE_SIZE * 6:
                wall = arcade.Sprite("blue wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create castle
    for x in range(80, 200, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)
    for x in range(415, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)
    for x in range(92, 185, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 355
        room.wall_list.append(wall)
    for x in range(427, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 355
        room.wall_list.append(wall)
    for x in range(92, 185, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 330
        room.wall_list.append(wall)
    for x in range(427, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 330
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 305
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 280
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 255
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 230
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 230
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 205
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 205
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)

    lock = arcade.Sprite("lockBlue.png", 0.2)
    lock.center_y = 210
    lock.center_x = 297
    room.lock_list.append(lock)

    # Load the background image for this level.
    # https://www.iconsdb.com/gray-icons/rectangle-icon.html
    room.background = arcade.load_texture("background.png")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.dragon_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if (x != SPRITE_SIZE * 12 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 14) or y != 0:
                # https://www.iconsdb.com/custom-color/square-icon.html
                wall = arcade.Sprite("actual_red_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5 and y != SPRITE_SIZE * 6) or x != 0:
                wall = arcade.Sprite("actual_red_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # https://icon-library.com/icon/dragon-png-icon-17.html
    dragon = arcade.Sprite("dragon.png", SPRITE_SCALING * 5)
    dragon.left = 200
    dragon.bottom = 200
    room.dragon_list.append(dragon)
    room.background = arcade.load_texture("background.png")

    return room


def setup_room_3():
    """
    Create and return room 3.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if (x != SPRITE_SIZE * 12 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 14) or y == 0:
                # https: // www.iconsdb.com / yellow - icons / square - icon.html
                wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            if (y != SPRITE_SIZE * 2 and y != SPRITE_SIZE * 3 and y != SPRITE_SIZE * 4) or x != 0:
                wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Creates maze
    for x in range(23, 525, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 315
        room.wall_list.append(wall)
    for x in range(63, 300, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 265
        room.wall_list.append(wall)
    for x in range(360, 580, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 265
        room.wall_list.append(wall)
    for x in range(23, 200, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 215
        room.wall_list.append(wall)
    for x in range(260, 580, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 215
        room.wall_list.append(wall)
    for x in range(53, 110, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(160, 280, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(320, 400, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(460, 580, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(23, 50, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 115
        room.wall_list.append(wall)
    for x in range(100, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 115
        room.wall_list.append(wall)
    for x in range(23, 230, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 65
        room.wall_list.append(wall)
    for x in range(280, 580, SPRITE_SIZE * 2):
        wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
        wall.left = x
        wall.bottom = 65
        room.wall_list.append(wall)

    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 260
    wall.bottom = 240
    room.wall_list.append(wall)
    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 160
    wall.bottom = 190
    room.wall_list.append(wall)
    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 100
    wall.bottom = 140
    room.wall_list.append(wall)
    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 363
    wall.bottom = 140
    room.wall_list.append(wall)
    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 304
    wall.bottom = 90
    room.wall_list.append(wall)
    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 288
    wall.bottom = 25
    room.wall_list.append(wall)
    wall = arcade.Sprite("yellow_wall.png", SPRITE_SCALING)
    wall.left = 288
    wall.bottom = 38
    room.wall_list.append(wall)
    room.background = arcade.load_texture("background.png")

    # https://www.vexels.com/png-svg/preview/209809/hand-drawn-sword-historical-weapon
    object = arcade.Sprite("sword.png", .16)
    object.left = 335
    object.bottom = 95
    room.object_list.append(object)

    return room


def setup_room_4():
    """
    Create and return room 4.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if (x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26) or y != 0:
                # https://www.iconsdb.com/custom-color/square-icon.html
                wall = arcade.Sprite("purple_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            wall = arcade.Sprite("purple_wall.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for x in range(30, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 65
        room.wall_list.append(wall)
    for x in range(60, 135, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 115
        room.wall_list.append(wall)
    for x in range(245, 375, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 115
        room.wall_list.append(wall)
    for x in range(425, 570, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 115
        room.wall_list.append(wall)
    for x in range(30, 80, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(132, 200, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(320, 470, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 165
        room.wall_list.append(wall)
    for x in range(60, 200, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 215
        room.wall_list.append(wall)
    for x in range(245, 320, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 215
        room.wall_list.append(wall)
    for x in range(520, 580, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 215
        room.wall_list.append(wall)
    for x in range(60, 110, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 265
        room.wall_list.append(wall)
    for x in range(220, 275, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 265
        room.wall_list.append(wall)
    for x in range(385, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 265
        room.wall_list.append(wall)
    for x in range(60, 110, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 315
        room.wall_list.append(wall)
    for x in range(158, 230, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 315
        room.wall_list.append(wall)
    for x in range(315, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("purple_wall.png", .08)
        wall.left = x
        wall.bottom = 315
        room.wall_list.append(wall)
    room.background = arcade.load_texture("background.png")
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 190
    wall.bottom = 90
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 190
    wall.bottom = 115
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 310
    wall.bottom = 90
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 132
    wall.bottom = 140
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 245
    wall.bottom = 140
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 245
    wall.bottom = 165
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 365
    wall.bottom = 140
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 83
    wall.bottom = 190
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 180
    wall.bottom = 190
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 320
    wall.bottom = 190
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 463
    wall.bottom = 190
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 463
    wall.bottom = 215
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 463
    wall.bottom = 240
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 520
    wall.bottom = 190
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 520
    wall.bottom = 165
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 385
    wall.bottom = 240
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 385
    wall.bottom = 215
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 60
    wall.bottom = 240
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 245
    wall.bottom = 240
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 158
    wall.bottom = 240
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 315
    wall.bottom = 290
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 315
    wall.bottom = 265
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 108
    wall.bottom = 290
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 158
    wall.bottom = 290
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 390
    wall.bottom = 345
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 255
    wall.bottom = 345
    room.wall_list.append(wall)
    wall = arcade.Sprite("purple_wall.png", .08)
    wall.left = 255
    wall.bottom = 320
    room.wall_list.append(wall)

    object = arcade.Sprite("keyGreen.png", .2)
    object.left = 60
    object.bottom = 195
    room.object_list.append(object)

    return room


def setup_room_5():
    """
    Create and return room 5.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.lock_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if (x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26) or y == 0:
                # https://www.iconsdb.com/custom-color/square-icon.html
                wall = arcade.Sprite("red_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5 and y != SPRITE_SIZE * 6) or x == 0:
                wall = arcade.Sprite("red_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create castle
    for x in range(80, 200, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)
    for x in range(415, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)
    for x in range(92, 185, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 355
        room.wall_list.append(wall)
    for x in range(427, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 355
        room.wall_list.append(wall)
    for x in range(92, 185, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 330
        room.wall_list.append(wall)
    for x in range(427, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 330
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 305
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 280
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 255
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 230
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 230
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 205
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 205
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)

    lock = arcade.Sprite("lockRed.png", 0.2)
    lock.center_y = 210
    lock.center_x = 297
    room.lock_list.append(lock)

    room.background = arcade.load_texture("background.png")

    return room


def setup_room_6():
    """
    Create and return room 6.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26:
                # https://www.iconsdb.com/white-icons/square-icon.html
                wall = arcade.Sprite("white_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            if y != SPRITE_SIZE * 2 and y != SPRITE_SIZE * 3 and y != SPRITE_SIZE * 4:
                wall = arcade.Sprite("white_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("background.png")

    return room


def setup_room_7():
    """
    Create and return room 7.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.dragon_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            # https://www.iconsdb.com/black-icons/square-icon.html
            wall = arcade.Sprite("black_wall.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            if (y != SPRITE_SIZE * 2 and y != SPRITE_SIZE * 3 and y != SPRITE_SIZE * 4) or x == 0:
                wall = arcade.Sprite("black_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    object = arcade.Sprite("keyRed.png", .2)
    object.left = 50
    object.bottom = 50
    room.object_list.append(object)
    dragon = arcade.Sprite("dragon.png", SPRITE_SCALING * 5)
    dragon.left = 200
    dragon.bottom = 200
    room.dragon_list.append(dragon)
    room.background = arcade.load_texture("background.png")

    return room


def setup_room_8():
    """
    Create and return room 8.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.dragon_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if (x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26) or y != 0:
                # https://www.iconsdb.com/custom-color/square-icon.html
                wall = arcade.Sprite("actual_red_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            wall = arcade.Sprite("actual_red_wall.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    object = arcade.Sprite("keyRed.png", .2)
    object.left = 350
    object.bottom = 350
    room.object_list.append(object)
    dragon = arcade.Sprite("dragon.png", SPRITE_SCALING * 5)
    dragon.left = 200
    dragon.bottom = 200
    room.dragon_list.append(dragon)
    room.background = arcade.load_texture("background.png")

    return room


def setup_room_9():
    """
    Create and return room 9.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.lock_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26:
                # https://www.iconsdb.com/green-icons/square-rounded-icon.html
                wall = arcade.Sprite("green wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            wall = arcade.Sprite("green wall.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create castle
    for x in range(80, 200, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 30
        room.wall_list.append(wall)
    for x in range(415, 520, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 30
        room.wall_list.append(wall)
    for x in range(92, 185, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 55
        room.wall_list.append(wall)
    for x in range(427, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 55
        room.wall_list.append(wall)
    for x in range(92, 185, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 80
        room.wall_list.append(wall)
    for x in range(427, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 80
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 105
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 130
        room.wall_list.append(wall)
    for x in range(92, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 130
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 155
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 155
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)
    for x in range(92, 250, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 205
        room.wall_list.append(wall)
    for x in range(357, 505, SPRITE_SIZE * 2):
        wall = arcade.Sprite("brickGrey.png", 0.2)
        wall.center_x = x
        wall.center_y = 205
        room.wall_list.append(wall)

    lock = arcade.Sprite("lockGreen.png", .2)
    lock.center_y = 180
    lock.center_x = 297
    lock.angle = 180
    room.lock_list.append(lock)
    room.background = arcade.load_texture("background.png")

    return room


def setup_room_10():
    """
    Create and return room 10.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.object_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE * 2):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 2):
            if (x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 24 and x != SPRITE_SIZE * 26) or y == 0:
                # https://www.walpaperlist.com/2020/01/rainbow-wallpaper-png.html
                wall = arcade.Sprite("rainbow_wall.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE * 2):
        # Loop for each box going across
        for y in range(SPRITE_SIZE * 2, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE * 2):
            wall = arcade.Sprite("rainbow_wall.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # https://findicons.com/icon/456447/trophy
    object = arcade.Sprite("trophy.png", .2)
    object.left = 275
    object.bottom = 190
    room.object_list.append(object)
    room.background = arcade.load_texture("background.png")

    return room


class Player(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.carry = None


class Dragon(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

    def follow_sprite(self, player_sprite):
        if self.center_y < player_sprite.center_y:
            self.center_y += min(MOVEMENT_SPEED - 3, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(MOVEMENT_SPEED - 3, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(MOVEMENT_SPEED - 3, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(MOVEMENT_SPEED - 3, self.center_x - player_sprite.center_x)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0
        self.object_list = None
        self.dragon_list = None

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        # http://www.i2clipart.com/colorwheel-24-football-flower-12-color-f5ce
        self.player_sprite = Player("player.png", 0.08)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.object_list = arcade.SpriteList()
        self.dragon_list = arcade.SpriteList()

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        room = setup_room_4()
        self.rooms.append(room)

        room = setup_room_5()
        self.rooms.append(room)

        room = setup_room_6()
        self.rooms.append(room)

        room = setup_room_7()
        self.rooms.append(room)

        room = setup_room_8()
        self.rooms.append(room)

        room = setup_room_9()
        self.rooms.append(room)

        room = setup_room_10()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        dragon = Dragon("dragon.png", SPRITE_SCALING * 2)
        dragon.center_x = 100
        dragon.center_y = 300

        self.dragon_list.append(dragon)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        if self.rooms[self.current_room].lock_list:
            self.rooms[self.current_room].lock_list.draw()

        if self.rooms[self.current_room].dragon_list:
            self.dragon_list.draw()

        if self.rooms[self.current_room].object_list:
            self.rooms[self.current_room].object_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()

        if self.player_sprite.carry:
            self.player_sprite.carry.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            if self.player_sprite.carry:
                self.rooms[self.current_room].object_list.append(self.player_sprite.carry)
                self.player_sprite.carry = None

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()
        if self.player_sprite.carry:
            self.player_sprite.carry.center_x = self.player_sprite.center_x + 30
            self.player_sprite.carry.center_y = self.player_sprite.center_y
        if self.rooms[self.current_room].object_list:
            object_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].object_list)

            for object in object_hit_list:
                self.player_sprite.carry = object
                self.rooms[self.current_room].object_list.remove(object)

        for dragon in self.dragon_list:
            dragon.follow_sprite(self.player_sprite)
            #dragon_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.dragon_list)

            #if dragon_hit_list:
                #end game

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH

        elif self.player_sprite.center_y < 0 and self.current_room == 1:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 2:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0

        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 0:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 3:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT

        elif self.player_sprite.center_x < 0 and self.current_room == 0:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 4:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0

        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 4:
            self.current_room = 7
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 7:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT

        elif self.player_sprite.center_x < 0 and self.current_room == 2:
            self.current_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 5:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0

        elif self.player_sprite.center_x < 0 and self.current_room == 5:
            self.current_room = 6
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 6:
            self.current_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0

        elif self.player_sprite.center_y < 0 and self.current_room == 5:
            self.current_room = 8
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 8:
            self.current_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0

        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 5:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 0:
            self.current_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT

        elif self.player_sprite.center_y < 0 and self.current_room == 8:
            self.current_room = 9
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 9:
            self.current_room = 8
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

