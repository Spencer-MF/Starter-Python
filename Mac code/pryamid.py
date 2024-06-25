import tkinter as tk
from colors import Color

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH = 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14    # The number of bricks in the base

def main():
    root = tk.Tk()  # Create the main window
    root.title('Pryamid')
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    side_border = (CANVAS_WIDTH - BRICK_WIDTH * BRICKS_IN_BASE) / 2
    make_pyra(canvas, side_border)
    root.mainloop()  # Start the Tkinter event loop

def make_pyra(canvas, off_set):
    top_x = off_set
    top_y = CANVAS_HEIGHT - BRICK_HEIGHT
    bricks_tall = 0

    for i in range(BRICKS_IN_BASE):
        for j in range(BRICKS_IN_BASE - bricks_tall):
            brick(canvas, top_x, top_y, j)
            top_x += BRICK_WIDTH
        bricks_tall += 1
        top_y -= BRICK_HEIGHT
        top_x = off_set + (BRICK_WIDTH / 2) * bricks_tall 

def brick(canvas, top_x, top_y, brick_num):
    color = raindow(brick_num)
    print(color)
    canvas.create_rectangle(
        top_x,
        top_y,
        top_x + BRICK_WIDTH,
        top_y + BRICK_HEIGHT,
        fill=color,
        outline='black'
    )

def raindow(num):
    num %= 7
    return Color.colors(num)


if __name__ == '__main__':
    main()