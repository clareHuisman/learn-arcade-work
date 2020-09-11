import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """Draws grass"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.csscolor.GREEN)


def draw_hills():
    arcade.draw_ellipse_filled(500, 150, 300, 200, arcade.csscolor.DARK_GREEN, 170)
    arcade.draw_ellipse_outline(500, 150, 300, 200, arcade.csscolor.DARK_OLIVE_GREEN, 5, 170)
    arcade.draw_ellipse_filled(750, 100, 600, 300, arcade.csscolor.DARK_GREEN)
    arcade.draw_ellipse_outline(750, 100, 600, 300, arcade.csscolor.DARK_OLIVE_GREEN, 5)
    arcade.draw_ellipse_filled(300, 100, 400, 200, arcade.csscolor.DARK_GREEN)
    arcade.draw_ellipse_outline(300, 100, 400, 200, arcade.csscolor.DARK_OLIVE_GREEN, 5)
    arcade.draw_ellipse_filled(0, 100, 800, 350, arcade.csscolor.DARK_GREEN)
    arcade.draw_ellipse_outline(0, 100, 800, 350, arcade.csscolor.DARK_OLIVE_GREEN, 5)

def draw_tree():
    """Draws a tree"""
    arcade.draw_polygon_filled(((650, 80), (750, 120), (760, 475), (800, 475), (800, 80)), arcade.csscolor.SANDY_BROWN)
    arcade.draw_polygon_filled(((760, 280), (720, 320), (700, 360), (710, 380),
                                (723, 340), (760, 330)), arcade.csscolor.SANDY_BROWN)
    arcade.draw_ellipse_filled(705, 370, 50, 30, arcade.csscolor.FOREST_GREEN)
    arcade.draw_ellipse_filled(705, 370, 50, 30, arcade.csscolor.FOREST_GREEN, 60)
    arcade.draw_ellipse_filled(780, 475, 100, 170, arcade.csscolor.FOREST_GREEN, 120)
    arcade.draw_ellipse_filled(780, 475, 100, 250, arcade.csscolor.FOREST_GREEN, 90)
    arcade.draw_ellipse_filled(780, 475, 100, 170, arcade.csscolor.FOREST_GREEN)


def draw_partial_flower(x, y):
    """draws a flower without all the petals"""
    arcade.draw_line(x, y, x, y - 50, arcade.csscolor.LIME_GREEN, 6)
    arcade.draw_ellipse_filled(x + 25, y, 50, 30, arcade.csscolor.LIGHT_SKY_BLUE)
    arcade.draw_ellipse_filled(x + 23, y + 15, 50, 30, arcade.csscolor.LIGHT_SKY_BLUE, 120)
    arcade.draw_ellipse_filled(x, y + 25, 50, 30, arcade.csscolor.LIGHT_SKY_BLUE, 90)
    arcade.draw_ellipse_filled(x - 23, y - 20, 50, 30, arcade.csscolor.LIGHT_SKY_BLUE, 135)
    arcade.draw_circle_filled(x, y, 10, arcade.csscolor.SALMON)


def draw_full_flower(x, y):
    """draws a flower with all the petals"""
    arcade.draw_line(x, y, x, y - 100, arcade.csscolor.LIME_GREEN, 8)
    arcade.draw_ellipse_filled(x + 25, y, 50, 25, arcade.csscolor.CORNSILK)
    arcade.draw_ellipse_filled(x + 23, y + 20, 50, 25, arcade.csscolor.CORNSILK, 135)
    arcade.draw_ellipse_filled(x, y + 25, 50, 25, arcade.csscolor.CORNSILK, 90)
    arcade.draw_ellipse_filled(x - 23, y - 20, 50, 25, arcade.csscolor.CORNSILK, 135)
    arcade.draw_ellipse_filled(x, y - 25, 50, 25, arcade.csscolor.CORNSILK, 90)
    arcade.draw_ellipse_filled(x + 23, y - 20, 50, 25, arcade.csscolor.CORNSILK, 45)
    arcade.draw_ellipse_filled(x - 23, y + 20, 50, 25, arcade.csscolor.CORNSILK, 45)
    arcade.draw_ellipse_filled(x - 25, y, 50, 25, arcade.csscolor.CORNSILK)
    arcade.draw_circle_filled(x, y, 15, arcade.csscolor.CORNFLOWER_BLUE)


def draw_daisy(x, y):
    """Draws a flower that looks like a daisy"""
    arcade.draw_line(x, y, x, y - 40, arcade.csscolor.LIME_GREEN, 4)
    arcade.draw_ellipse_filled(x + 4, y - 35, 20, 5, arcade.csscolor.LIME_GREEN, 120)
    arcade.draw_ellipse_filled(x - 4, y - 35, 20, 5, arcade.csscolor.LIME_GREEN, 60)
    arcade.draw_ellipse_filled(x, y, 50, 20, arcade.csscolor.WHITE, 90)
    arcade.draw_ellipse_filled(x, y, 50, 20, arcade.csscolor.WHITE, 150)
    arcade.draw_ellipse_filled(x, y, 50, 20, arcade.csscolor.WHITE, 30)
    arcade.draw_circle_filled(x, y, 8, arcade.csscolor.YELLOW)


def draw_tulip(x, y):
    """Draws a flower that resembles a tulip"""
    arcade.draw_line(x, y, x, y - 50, arcade.csscolor.LIME_GREEN, 3)
    arcade.draw_ellipse_filled(x + 10, y - 40, 20, 5, arcade.csscolor.LIME_GREEN, 150)
    arcade.draw_ellipse_filled(x, y, 40, 20, arcade.csscolor.ORCHID, 90)
    arcade.draw_ellipse_filled(x - 10, y - 5, 40, 20, arcade.csscolor.ORCHID, 30)
    arcade.draw_ellipse_filled(x + 10, y - 5, 40, 20, arcade.csscolor.ORCHID, 150)


def draw_vertical_bee(x, y):
    """Draws a bee vertically"""
    arcade.draw_ellipse_filled(x, y, 20, 10, arcade.csscolor.YELLOW, 90)
    arcade.draw_line(x - 5, y, x + 5, y, arcade.csscolor.BLACK)
    arcade.draw_line(x - 5, y - 5, x + 5, y - 5, arcade.csscolor.BLACK)
    arcade.draw_line(x - 5, y + 5, x + 5, y + 5, arcade.csscolor.BLACK)
    arcade.draw_line(x - 4, y - 7, x + 4, y - 7, arcade.csscolor.BLACK)
    arcade.draw_line(x - 3, y - 9, x + 3, y - 9, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(x + 5, y, 12, 5, arcade.csscolor.ANTIQUE_WHITE, 180)
    arcade.draw_ellipse_filled(x - 5, y, 12, 5, arcade.csscolor.ANTIQUE_WHITE)
    arcade.draw_line(x + 2, y + 9, x + 4, y + 12, arcade.csscolor.BLACK)
    arcade.draw_line(x - 2, y + 9, x - 4, y + 12, arcade.csscolor.BLACK)


def draw_horizontal_bee(x, y):
    """Draws a bee horizontal"""
    arcade.draw_ellipse_filled(x, y, 20, 10, arcade.csscolor.YELLOW)
    arcade.draw_line(x, y - 5, x, y + 5, arcade.csscolor.BLACK)
    arcade.draw_line(x + 5, y + 5, x + 5, y - 5, arcade.csscolor.BLACK)
    arcade.draw_line(x - 5, y + 5, x - 5, y - 5, arcade.csscolor.BLACK)
    arcade.draw_line(x - 7, y + 4, x - 7, y - 4, arcade.csscolor.BLACK)
    arcade.draw_line(x - 9, y + 3, x - 9, y - 3, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(x, y + 5, 12, 5, arcade.csscolor.ANTIQUE_WHITE, 90)
    arcade.draw_ellipse_filled(x, y - 5, 12, 5, arcade.csscolor.ANTIQUE_WHITE, 90)
    arcade.draw_line(x + 9, y + 2, x + 12, y + 4, arcade.csscolor.BLACK)
    arcade.draw_line(x + 9, y - 2, x + 12, y - 4, arcade.csscolor.BLACK)


def draw_cloud(x, y):
    """Draws a cloud"""
    arcade.draw_ellipse_filled(x, y, 80, 50, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_ellipse_filled(x + 40, y, 80, 50, arcade.csscolor.FLORAL_WHITE)
    arcade.draw_ellipse_filled(x + 20, y + 25, 80, 50, arcade.csscolor.FLORAL_WHITE)


def draw_bird(x, y, z):
    """Draws a bird"""
    arcade.draw_parabola_outline(x + z, y, x, z * .5, arcade.csscolor.BLACK, 4)
    arcade.draw_parabola_outline(x, y, x - z, z * .5, arcade.csscolor.BLACK, 4)

def main():
    """Draws entire picture"""
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.csscolor.DODGER_BLUE)
    arcade.start_render()

    draw_hills()
    draw_grass()
    draw_tree()

    draw_cloud(100, 400)
    draw_cloud(150, 425)
    draw_cloud(580, 380)
    draw_cloud(300, 590)
    draw_cloud(340, 320)
    draw_cloud(380, 460)
    draw_cloud(420, 490)
    draw_cloud(75, 425)

    draw_bird(300, 400, 20)
    draw_bird(280, 380, 20)
    draw_bird(320, 480, 30)
    draw_bird(100, 520, 30)
    draw_bird(580, 460, 20)

    draw_partial_flower(760, 50)
    draw_partial_flower(170, 70)
    draw_partial_flower(450, 10)

    draw_full_flower(400, 50)
    draw_full_flower(625, 96)
    draw_full_flower(286, 100)
    draw_full_flower(50, 80)

    draw_daisy(500, 100)
    draw_daisy(200, 25)
    draw_daisy(320, 37)
    draw_daisy(700, 70)
    draw_daisy(560, 125)

    draw_tulip(550, 50)
    draw_tulip(120, 75)
    draw_tulip(670, 100)
    draw_tulip(25, 60)

    draw_vertical_bee(100, 120)
    draw_vertical_bee(573, 50)
    draw_vertical_bee(238, 140)
    draw_vertical_bee(698, 76)

    draw_horizontal_bee(400, 100)
    draw_horizontal_bee(608, 23)
    draw_horizontal_bee(154, 78)
    draw_horizontal_bee(752, 63)

    arcade.finish_render()

    arcade.run()


main()
