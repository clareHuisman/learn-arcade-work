import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Walls"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

NUMBER_OF_PLANTS = 30

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.plant_list = None

        # Set up the player
        self.player_sprite = None

        # Sound from kenney.nl
        self.sound = arcade.load_sound("select_004.ogg")
        self.score = 0
        self.plants_remaining = 0

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """
        # All images from kenney.nl
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.plant_list = arcade.SpriteList()
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("wormGreen.png", .4)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Sets up section one
        for y in range(100, 1450, 100):
            for x in range(0, 1025, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(4) > 0:
                    wall = arcade.Sprite("bush.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for y in range(150, 1450, 100):
            for x in range(100, 1025, 64):
                # Randomly places plants in between walls
                if random.randrange(18) == 0:
                    plant = arcade.Sprite("plantPurple.png", SPRITE_SCALING)
                    plant.center_x = x
                    plant.center_y = y
                    self.plant_list.append(plant)
                    self.plants_remaining += 1

        # -- Sets up section two
        for x in range(1225, 2000, 130):
            for y in range(0, 1990, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(7) > 0:
                    wall = arcade.Sprite("cactus.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for x in range(1290, 2000, 130):
            for y in range(40, 1450, 64):
                # Randomly places plants between walls
                if random.randrange(14) == 0:
                    plant = arcade.Sprite("plantPurple.png", SPRITE_SCALING)
                    plant.center_x = x
                    plant.center_y = y
                    self.plant_list.append(plant)
                    self.plants_remaining += 1

        # Sets up section three
        for y in range(0, 700, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2200
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(780, 1450, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2200
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(100, 1450, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2330
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 900, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2460
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(1000, 1450, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2460
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 400, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2590
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(550, 1450, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2590
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 1350, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2720
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 700, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2850
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(780, 1450, 64):
            wall = arcade.Sprite("rock.png", SPRITE_SCALING)
            wall.angle = 270
            wall.center_x = 2850
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(64, 1450, 100):
            for x in range(2245, 2900, 130):
                # Randomly places plants in between walls
                if random.randrange(8) == 0:
                    plant = arcade.Sprite("plantPurple.png", SPRITE_SCALING)
                    plant.center_x = x
                    plant.center_y = y
                    self.plant_list.append(plant)
                    self.plants_remaining += 1

        # Sets up outer walls and walls between sections
        for y in range(0, 1450, 64):
            wall = arcade.Sprite("sandCenter.png", SPRITE_SCALING)
            wall.center_x = 1075
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 1450, 64):
            wall = arcade.Sprite("water.png", SPRITE_SCALING)
            wall.center_x = 2020
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(0, 3000, 64):
            wall = arcade.Sprite("sandCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1500
            self.wall_list.append(wall)

        for y in range(0, 1500, 64):
            wall = arcade.Sprite("sandCenter.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(0, 3000, 64):
            wall = arcade.Sprite("sandCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(0, 1500, 64):
            wall = arcade.Sprite("sandCenter.png", SPRITE_SCALING)
            wall.center_x = 3000
            wall.center_y = y
            self.wall_list.append(wall)

        # Sets up signs to help player get to next section
        wall = arcade.Sprite("signRight.png", SPRITE_SCALING)
        wall.center_x = 1075
        wall.center_y = 1400
        self.wall_list.append(wall)
        wall = arcade.Sprite("signRight.png", SPRITE_SCALING)
        wall.center_x = 2020
        wall.center_y = 1400
        self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.SANDY_BROWN)

        # Set the viewport boundaries
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.plant_list.draw()

        # Draw the score and remaining plants to find
        output = f"Score: {self.score}"
        arcade.draw_text(output, self.view_left, self.view_bottom + 25, arcade.color.WHITE, 14)

        remaining = f"Plants Remaining: {self.plants_remaining}"
        arcade.draw_text(remaining, self.view_left, self.view_bottom + 10, arcade.color.WHITE, 14)

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

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # Checks for collisions with sprites
        plant_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.plant_list)

        # If a plant was hit, removes it from the list
        for plant in plant_hit_list:
            plant.remove_from_sprite_lists()
            arcade.play_sound(self.sound)
            self.score += 1
            self.plants_remaining -= 1


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
