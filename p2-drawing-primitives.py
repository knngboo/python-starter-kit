import arcade

# set width, height, title, and make resizeable
arcade.open_window(600, 600, "Drawing with Primatives!", resizable=True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for x in range(0, 601, 120):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)
for y in range(0, 601, 200):
    arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 2)

font0 = 9
font1 = 3
font2 = 10

arcade.draw_text("draw_point", 3, 405, arcade.color.BLACK, 9)
arcade.draw_point(60, 495, arcade.color.RED, 10)
arcade.draw_text("draw_points", 123, 405, arcade.color.BLACK, 9)
point_list = ((165, 495),
              (165, 480),
              (165, 465),
              (195, 495),
              (195, 480),
              (195, 465))
arcade.draw_points(point_list, arcade.color.ZAFFRE, 10)


arcade.draw_text("draw_line", 243, 405, arcade.color.BLACK, 9)
arcade.draw_line(270, 495, 300, 450, arcade.color.WOOD_BROWN, 3)
arcade.draw_text("draw_lines", 363, 405, arcade.color.BLACK, 9)
point_list = ((390, 450),
              (450, 450),
              (390, 480),
              (450, 480),
              (390, 510),
              (450, 510))
arcade.draw_lines(point_list, arcade.color.BLUE, 3)

arcade.draw_text("draw_line_strip", 483, 405, arcade.color.BLACK, 9)
point_list = ((510, 450),
              (570, 450),
              (510, 480),
              (570, 480),
              (510, 510),
              (570, 510))
arcade.draw_line_strip(point_list, arcade.color.TROPICAL_RAIN_FOREST, 3)

arcade.draw_text("draw_polygon_outline",3, 207, arcade.color.BLACK, 9)
point_list = ((30, 240),
              (45, 240),
              (60, 255),
              (60, 285),
              (45, 300),
              (30, 300))
arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)
arcade.draw_text("draw_polygon_filled", 123, 207, arcade.color.BLACK, 9)
point_list = ((150, 240),
              (165, 240),
              (180, 255),
              (180, 285),
              (165, 300),
              (150, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

arcade.draw_text("circle_outline", 243, 207, arcade.color.BLACK, 9)
arcade.draw_circle_outline(300, 285, 18, arcade.color.GREEN, 3)
arcade.draw_text("circle_filled", 363, 207, arcade.color.BLACK, 9)
arcade.draw_circle_filled(420, 285, 18, arcade.color.GREEN)

arcade.draw_text("ellipse_outline", 483, 207, arcade.color.BLACK, 9)
arcade.draw_ellipse_outline(540, 273, 15, 36, arcade.color.AMBER, 3)
arcade.draw_ellipse_outline(540, 336, 15, 36, arcade.color.BLACK_BEAN, 3, 45)
arcade.draw_text("ellipse_filled", 483, 207, arcade.color.BLACK, 9)
arcade.draw_ellipse_filled(60, 81, 15, 36, arcade.color.AMBER)
arcade.draw_ellipse_filled(60, 144, 15, 36, arcade.color.BLACK_BEAN, 45)

arcade.draw_text("arc_outline/filled", 123, 3, arcade.color.BLACK, 9)
arcade.draw_arc_outline(150, 81, 15, 36, arcade.color.BRIGHT_MAROON, 90, 360)
arcade.draw_arc_filled(150, 144, 15, 36, arcade.color.BOTTLE_GREEN, 90, 360, 45)

arcade.draw_text("rect_outline", 243, 3, arcade.color.BLACK, 9)
arcade.draw_rect_outline(arcade.rect.XYWH(295, 100, 45, 65), arcade.color.BRITISH_RACING_GREEN)
arcade.draw_rect_outline(arcade.rect.XYWH(295, 160, 20, 45), arcade.color.BRITISH_RACING_GREEN, 3, 45)
arcade.draw_text("rect_filled", 363, 3, arcade.color.BLACK,9)
arcade.draw_rect_filled(arcade.rect.XYWH(420, 100, 45, 65), arcade.color.BLUSH)
arcade.draw_rect_filled(arcade.rect.XYWH(420, 160, 20, 40), arcade.color.BLUSH, 45)

arcade.draw_text("bitmap", 483, 3, arcade.color.BLACK, 9)
texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png")
scale = .6
arcade.draw_texture_rect(texture, arcade.XYWH(540, 120, texture.width, texture.height).scale(scale))
arcade.draw_texture_rect(texture, arcade.XYWH(540, 60, texture.width, texture.height).scale(scale), angle=-90)

arcade.finish_render()

arcade.run()
