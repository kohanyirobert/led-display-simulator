import color

class Display():

    def __init__(self, script, width, height):
        self.script = script
        self.width = width
        self.height = height
        self.grid = []
        for _ in range(self.width):
            row = []
            for _ in range(self.height):
                row.append(color.BLACK)
            self.grid.append(row)

    def run(self):
        while True:
            self.script.update(self.width, self.height,
                               self.grid, self.get_event())
            self.refresh()

    def refresh(self):
        pass

    def get_event(self):
        pass
