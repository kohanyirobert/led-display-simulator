import event

class KeyboardEvent(event.Event):

    def __init__(self, key_code):
        self.key_code = key_code

    def is_left_arrow(self):
        return self.key_code == 0x25

    def is_up_arrow(self):
        return self.key_code == 0x26

    def is_right_arrow(self):
        return self.key_code == 0x27

    def is_down_arrow(self):
        return self.key_code == 0x28
