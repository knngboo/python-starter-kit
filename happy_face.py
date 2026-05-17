import arcade

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Happy Face Example"

arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300
y = 280
width = 240
height = 200
start_angle = 190
end_angle = 350
line_width = 20
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, line_width)

arcade.finish_render()

arcade.run()