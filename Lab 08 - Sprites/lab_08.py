import random
import math
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_PIE = 0.3
SPRITE_SCALING_BAT = 0.2
PIE_COUNT = 50
BAT_COUNT = 35

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


class Bat(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Creates the bat movement
        self.center_y -= 1

        # Checks if we went off the screen and resets to the top
        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Pie(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.02
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        # Creates pie motion
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y

        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player_list = None
        self.pie_list = None
        self.bat_list = None

        # Loads sounds for pie and bat collisions
        # Both sounds found at kenney.nl
        self.good_sound = arcade.load_sound("confirmation_004.ogg")
        self.bad_sound = arcade.load_sound("error_004.ogg")

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)

    def setup(self):
        """Sets up game and initializes variables"""

        # Creates sprite lists
        self.player_list = arcade.SpriteList()
        self.pie_list = arcade.SpriteList()
        self.bat_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Character from myiconfinder.com
        self.player_sprite = arcade.Sprite("ghost.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Creates pies
        for i in range(PIE_COUNT):
            # Pie image from shareicon.net
            pie = Pie("pumpkin_pie.png", SPRITE_SCALING_PIE)

            pie.circle_center_x = random.randrange(SCREEN_WIDTH)
            pie.circle_center_y = random.randrange(SCREEN_HEIGHT)

            pie.circle_radius = random.randrange(10, 200)

            pie.circle_angle = random.random() * 2 * math.pi

            self.pie_list.append(pie)

        # Creates bats
        for i in range(BAT_COUNT):
            # Bat image from vexels.com
            bat = Bat("bat.png", SPRITE_SCALING_BAT)

            bat.center_x = random.randrange(SCREEN_WIDTH)
            bat.center_y = random.randrange(SCREEN_HEIGHT)
            bat.change_x = random.randrange(-3, 4)
            bat.change_y = random.randrange(-3, 4)

            self.bat_list.append(bat)

    def on_draw(self):
        """Draws everything"""
        arcade.start_render()
        self.pie_list.draw()
        self.bat_list.draw()
        self.player_list.draw()

        # Creates score on screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # Checks if game is over, prints Game Over if there are no pies left
        if len(self.pie_list) == 0:
            end = f"GAME OVER"
            arcade.draw_text(end, 400, 400, arcade.color.WHITE, 50)
            output = f"Score: {self.score} / 50"
            arcade.draw_text(output, 400, 300, arcade.color.WHITE, 40)

    def on_mouse_motion(self, x, y, dx, dy):
        # Move the center of the player sprite to match the mouse
        if len(self.pie_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """Movement and game logic"""

        # Checks if there are pies left, if so moves all sprites
        if len(self.pie_list) > 0:
            # Calls update on all pie sprites
            self.pie_list.update()

            # Checks for collisions with pie
            pie_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.pie_list)

            # Loops through colliding sprites and removes them
            for pie in pie_hit_list:
                pie.remove_from_sprite_lists()
                arcade.play_sound(self.good_sound)
                self.score += 1

            # Calls update on all bat sprites
            self.bat_list.update()

            # Checks for collisions with bat
            bat_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bat_list)

            # Loops through colliding sprites and removes them
            for bat in bat_hit_list:
                bat.remove_from_sprite_lists()
                arcade.play_sound(self.bad_sound)
                self.score -= 1


def main():
    """Main method"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
