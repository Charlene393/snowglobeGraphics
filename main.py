import math
import cairo
import random

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_circle(ctx, x, y, radius, color):
    ctx.arc(x, y, radius, 0, 2 * math.pi)
    ctx.set_source_rgb(*color)
    ctx.fill()



def draw_realistic_tree(ctx, x, y, height):
    # Draw trunk
    trunk_width = height * 0.1
    ctx.rectangle(x - trunk_width / 2, y - height * 0.3, trunk_width, height * 0.3)
    gradient = cairo.LinearGradient(x, y, x, y - height * 0.3)
    gradient.add_color_stop_rgb(0, 0.3, 0.2, 0.1)  # Darker bottom
    gradient.add_color_stop_rgb(1, 0.4, 0.25, 0.15)  # Lighter top
    ctx.set_source(gradient)
    ctx.fill()

    # Draw branches in layers
    layers = 5
    for i in range(layers):
        layer_y = y - height * (0.3 + 0.7 * i / layers)
        layer_width = height * (0.8 - 0.1 * i / layers)

        # Create triangle shape for each layer
        ctx.move_to(x, layer_y)
        ctx.line_to(x - layer_width / 2, layer_y + height * 0.2)
        ctx.line_to(x + layer_width / 2, layer_y + height * 0.2)
        ctx.close_path()

        # Green gradient for needles
        gradient = cairo.LinearGradient(x, layer_y, x, layer_y + height * 0.2)
        gradient.add_color_stop_rgb(0, 0, 0.4, 0)  # Darker top
        gradient.add_color_stop_rgb(1, 0, 0.5, 0)  # Lighter bottom
        ctx.set_source(gradient)
        ctx.fill_preserve()

        # Add snow highlights
        ctx.set_source_rgba(1, 1, 1, 0.3)
        ctx.set_line_width(1.5)
        ctx.stroke()

        # Add decorations
        for _ in range(4):
            dec_x = x + random.uniform(-layer_width * 0.4, layer_width * 0.4)
            dec_y = layer_y + random.uniform(0, height * 0.15)
            # Draw red ornaments
            draw_circle(ctx, dec_x, dec_y, 3, (0.9, 0, 0))
            # Add highlight to ornaments
            draw_circle(ctx, dec_x - 1, dec_y - 1, 1, (1, 0.8, 0.8))


def draw_house(ctx, x, y, width, height):
    # Draw house body
    ctx.rectangle(x - width / 2, y, width, height)
    ctx.set_source_rgb(0.55, 0.27, 0.07)  # Brown color for the house body
    ctx.fill()

    # Draw roof
    ctx.move_to(x - width / 2, y)
    ctx.line_to(x, y - height / 2)
    ctx.line_to(x + width / 2, y)
    ctx.close_path()
    ctx.set_source_rgb(0.4, 0.2, 0.1)  # Darker brown for the roof
    ctx.fill()


def draw_sky(ctx):
    ctx.set_source_rgb(0.15, 0.4, 0.8)
    ctx.paint()

    for _ in range(30):
        x = random.uniform(0, WIDTH)
        y = random.uniform(0, HEIGHT)
        size = random.uniform(1, 3)
        draw_circle(ctx, x, y, size, (1, 1, 1))


def draw_snow_globe(ctx, x, y, radius):
    ctx.arc(x, y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(x, y, radius * 0.1, x, y, radius)
    gradient.add_color_stop_rgba(0, 0.9, 0.95, 1, 0.2)
    gradient.add_color_stop_rgba(1, 0.3, 0.5, 0.9, 0.3)
    ctx.set_source(gradient)
    ctx.fill_preserve()

    ctx.set_source_rgba(1, 1, 1, 0.5)
    ctx.set_line_width(3)
    ctx.stroke()

    ctx.arc(x - radius * 0.6, y - radius * 0.6, radius * 0.1, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

#draw a snowman
def draw_snowman(ctx, x, y):
    # Body
    draw_circle(ctx, x, y, 20, (1, 1, 1))  # Bottom circle
    draw_circle(ctx, x, y - 30, 15, (1, 1, 1))  # Middle circle
    draw_circle(ctx, x, y - 50, 10, (1, 1, 1))  # Head

    # Eyes
    draw_circle(ctx, x - 3, y - 52, 1.5, (0, 0, 0))  # Left eye
    draw_circle(ctx, x + 3, y - 52, 1.5, (0, 0, 0))  # Right eye

    # Nose
    ctx.move_to(x, y - 45)
    ctx.line_to(x + 8, y - 45)
    ctx.set_source_rgb(1, 0.5, 0)  # Orange for carrot nose
    ctx.set_line_width(2)
    ctx.stroke()

    # Buttons on the chest
    button_y_positions = [y - 30, y - 20, y - 10]  # Vertical positions for buttons
    for pos in button_y_positions:
        draw_circle(ctx, x, pos, 1.5, (0, 0, 0))  # Draw buttons

    # Arms (lines extending from the middle circle)
    ctx.set_line_width(2)
    # Left arm
    ctx.move_to(x - 15, y - 30)  # Starting point of left arm
    ctx.line_to(x - 30, y - 25)  # Ending point of left arm
    ctx.stroke()

    # Right arm
    ctx.move_to(x + 15, y - 30)  # Starting point of right arm
    ctx.line_to(x + 30, y - 25)  # Ending point of right arm
    ctx.stroke()


def draw_holly(ctx, x, y):
    for angle in [-0.3, 0.3]:
        ctx.save()
        ctx.translate(x, y)
        ctx.rotate(angle)
        ctx.scale(1, 1.5)
        ctx.arc(0, 0, 15, 0, math.pi)
        ctx.restore()
        ctx.set_source_rgb(0, 0.5, 0)
        ctx.fill()

    positions = [(x, y), (x - 7, y + 5), (x + 7, y + 5)]
    for bx, by in positions:
        draw_circle(ctx, bx, by, 4, (0.9, 0, 0))


def draw_scene():
    context.set_source_rgb(1, 1, 1)
    context.paint()

    draw_sky(context)

    globe_x, globe_y = WIDTH // 2, HEIGHT // 2 - 50
    globe_radius = 150

    context.save()
    context.arc(globe_x, globe_y, globe_radius, 0, 2 * math.pi)
    context.clip()

    context.rectangle(globe_x - globe_radius, globe_y - 5, globe_radius * 2, globe_radius * 1.5)
    context.set_source_rgb(0.941, 1.0, 1.0)
    context.fill()

    draw_realistic_tree(context, globe_x + 90, globe_y + 120, 90)

    # Draw  houses with brown color and different positions
    draw_house(context, globe_x - 60, globe_y + 80, 30, 30)
    draw_house(context, globe_x + 20, globe_y + 80, 30, 30)
    draw_house(context, globe_x +50, globe_y +60, 30, 30)
    draw_house(context, globe_x - 10, globe_y + 110, 30, 30)
    draw_house(context, globe_x + 50, globe_y + 90, 30, 30)
    draw_house(context, globe_x - 100, globe_y + 60, 40, 80)

    for _ in range(40):
        x = random.uniform(globe_x - globe_radius * 0.9, globe_x + globe_radius * 0.9)
        y = random.uniform(globe_y - globe_radius * 0.9, globe_y + globe_radius * 0.9)
        draw_circle(context, x, y, 1.5, (1, 1, 1))

    context.restore()

    draw_snow_globe(context, globe_x, globe_y, globe_radius)
    draw_snowman(context, WIDTH // 2, 300)
    #draw_snowman(context, WIDTH // 2, 250)


    context.rectangle(globe_x - globe_radius * 0.4, globe_y + globe_radius, globe_radius * 0.8, 30)
    context.set_source_rgb(0, 0, 0)
    context.fill()

    draw_holly(context, 100, HEIGHT - 100)
    draw_holly(context, WIDTH - 100, HEIGHT - 100)

    surface.write_to_png("snow_globe_with_houses.png")

# Generate the image
draw_scene()
print("Snow globe with three small brown houses added!")
