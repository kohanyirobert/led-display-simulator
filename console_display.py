import atexit
import display
import color
import keyboard_event
import asciimatics.screen
import asciimatics.event


class ConsoleDisplay(display.Display):

    def __init__(self, script, width, height):
        super().__init__(script, width, height)
        self.screen = asciimatics.screen.Screen.open()
        atexit.register(lambda: self.screen.close(True))

    def refresh(self):
        for i in range(self.width):
            for j in range(self.height):
                char = '#'
                if self.grid[i][j] == color.BLACK:
                    char = ' '
                self.screen.print_at(char, i, j)
        self.screen.refresh()

    def get_event(self):
        event = self.screen.get_event()
        if event:
            if isinstance(event, asciimatics.event.KeyboardEvent):
                if event.key_code == asciimatics.screen.Screen.KEY_LEFT:
                    return keyboard_event.KeyboardEvent(0x25)
                elif event.key_code == asciimatics.screen.Screen.KEY_UP:
                    return keyboard_event.KeyboardEvent(0x26)
                elif event.key_code == asciimatics.screen.Screen.KEY_RIGHT:
                    return keyboard_event.KeyboardEvent(0x27)
                elif event.key_code == asciimatics.screen.Screen.KEY_DOWN:
                    return keyboard_event.KeyboardEvent(0x28)
            elif isinstance(event, asciimatics.event.MouseEvent):
                pass
        return None
