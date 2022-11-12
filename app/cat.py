class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Meow'

    def introduce_yourself(self):
        return f'{self.speak()} I\'m {self.name}'
