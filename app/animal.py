class Animal:

    def __init__(self, name):
        self.name = name

    def introduce_yourself(self):
        return f'{self.speak()} I\'m {self.name}'
