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




def draw_sky(ctx):
    # Rich blue background
    ctx.set_source_rgb(0.15, 0.4, 0.8)
    ctx.paint()

    # Add stars
    for _ in range(30):
        x = random.uniform(0, WIDTH)
        y = random.uniform(0, HEIGHT)
        size = random.uniform(1, 3)
        draw_circle(ctx, x, y, size, (1, 1, 1))

    # Feature star
    ctx.save()
    ctx.translate(WIDTH - 100, 80)
    for i in range(8):
        ctx.move_to(0, 0)
        ctx.line_to(0, 15)
        ctx.rotate(math.pi / 4)
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(2)
    ctx.stroke()
    ctx.restore()


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

    # Highlights
    ctx.arc(x - radius * 0.6, y - radius * 0.6, radius * 0.1, 0, 2 * math.pi)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()


def draw_snowman(ctx, x, y):
    # Body
    draw_circle(ctx, x, y + 30, 25, (1, 1, 1))
    draw_circle(ctx, x, y, 20, (1, 1, 1))
    draw_circle(ctx, x, y - 30, 15, (1, 1, 1))

    # Hat
    ctx.rectangle(x - 12, y - 55, 24, 15)
    ctx.rectangle(x - 15, y - 42, 30, 5)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()

    # Face
    draw_circle(ctx, x - 5, y - 33, 2, (0, 0, 0))
    draw_circle(ctx, x + 5, y - 33, 2, (0, 0, 0))

    # Arms
    ctx.set_source_rgb(0.3, 0.2, 0.1)
    ctx.set_line_width(2)
    ctx.move_to(x - 25, y)
    ctx.line_to(x - 40, y - 15)
    ctx.move_to(x + 25, y)
    ctx.line_to(x + 40, y - 15)
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

def draw_curvy_mountain(ctx, x, y, width, height, peaks=3):
    # Set color for the mountain - dark grey
    ctx.set_source_rgb(0.3, 0.3, 0.3)

    # Start drawing from the left base of the mountain
    ctx.move_to(x - width / 2, y)

    # Loop to create each peak using Bezier curves
    for i in range(peaks):
        peak_x = x - width / 2 + (i + 0.5) * (width / peaks)  # x position for each peak
        valley_x = x - width / 2 + (i + 1) * (width / peaks)  # x position for the valley after each peak

        # Control points create the curves; adjust y control points for more smoothness
        ctx.curve_to(peak_x - width / (4 * peaks), y - height * 0.7,
                     peak_x + width / (4 * peaks), y - height * 0.7,
                     valley_x, y)

    # Complete the mountain shape down to the base
    ctx.line_to(x + width / 2, y)
    ctx.line_to(x - width / 2, y)
    ctx.close_path()
    ctx.fill()



def draw_scene():
    # Clear canvas
    context.set_source_rgb(1, 1, 1)
    context.paint()

    # Draw sky
    draw_sky(context)

    # Set up snow globe
    globe_x, globe_y = WIDTH // 2, HEIGHT // 2 - 50
    globe_radius = 150

    # Clip for snow globe contents
    context.save()
    context.arc(globe_x, globe_y, globe_radius, 0, 2 * math.pi)
    context.clip()

    # Snowy ground
    context.rectangle(globe_x - globe_radius, globe_y - 20, globe_radius * 2, globe_radius * 1.5)
    context.set_source_rgb(1, 1, 1)
    context.fill()

    # Draw mountains (moved to the back and colored dark grey)


    # Draw scene elements in the foreground
    draw_realistic_tree(context, globe_x + 90, globe_y + 120, 90)  # Right tree, moved forward

   # draw_snowman(context, globe_x, globe_y + 20)

    # Falling snow
    for _ in range(40):
        x = random.uniform(globe_x - globe_radius * 0.9, globe_x + globe_radius * 0.9)
        y = random.uniform(globe_y - globe_radius * 0.9, globe_y + globe_radius * 0.9)
        draw_circle(context, x, y, 1.5, (1, 1, 1))

    context.restore()

    # Draw snow globe
    draw_snow_globe(context, globe_x, globe_y, globe_radius)

    # Base
    context.rectangle(globe_x - globe_radius * 0.4, globe_y + globe_radius, globe_radius * 0.8, 30)
    context.set_source_rgb(0, 0, 0)
    context.fill()

    # Holly decorations
    draw_holly(context, 100, HEIGHT - 100)
    draw_holly(context, WIDTH - 100, HEIGHT - 100)

    # Save the image
    surface.write_to_png("snow_globe_realistic_tree.png")

# Generate the updated image
draw_scene()
print("Snow globe with mountain moved to the back and dark grey color applied!")
