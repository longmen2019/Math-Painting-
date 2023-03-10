from venv.canvas import Canvas
from venv.shapes import Rectangle, Square

# Get canvas with and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])
while True:
    shape_type = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How  much green? "))
        blue = int(input("How much blue"))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)
    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the side length the square: "))
        # sqr_height = int(input("Enter the height of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How  much green? "))
        blue = int(input("How much blue"))
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    # Break the loop if user entered 'quit'
    if shape_type == 'quit':
        break

# canvas = Canvas(height=20, width=30, color=(255, 255, 255))
# r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
# r1.draw(canvas)
# s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
# s1.draw(canvas)
canvas.make('canvas.png')
