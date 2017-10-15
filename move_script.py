import script
import color
import keyboard_event

class MoveScript(script.Script):

    def __init__(self):
        super().__init__()
        self.last_x = 0
        self.last_y = 0

    def update(self, width, height, grid, event):
        x, y = self.last_x, self.last_y

        if event:
            if isinstance(event, keyboard_event.KeyboardEvent):
                if event.is_left_arrow():
                    if x - 1 >= 0:
                        x -= 1
                elif event.is_up_arrow():
                    if y - 1 >= 0:
                        y -= 1
                elif event.is_right_arrow():
                    if x + 1 < width:
                        x += 1
                if event.is_down_arrow():
                    if y + 1 < height:
                        y += 1

        moved = x != self.last_x or y != self.last_y
        if moved:
            grid[self.last_x][self.last_y] = color.BLACK
            self.last_x, self.last_y = x, y

        grid[x][y] = color.WHITE
