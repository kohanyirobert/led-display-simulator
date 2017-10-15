import script
import color


class BlinkScript(script.Script):

    def __init__(self):
        super().__init__()

    def update(self, width, height, grid, event):
        if grid[0][0] == color.BLACK:
            grid[0][0] = color.WHITE
        else:
            grid[0][0] = color.BLACK
