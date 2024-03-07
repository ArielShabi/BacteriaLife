class Bacteria:
    def __init__(self, id, name, speed):
        self.id = id
        self.name = name
        self.speed = speed

    def __str__(self):
        return self.name
