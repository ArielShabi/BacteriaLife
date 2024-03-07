class Board:
    def __init__(self, width, height, bacterias):
        self.width = width
        self.height = height
        self.bacteria = bacterias

    def add_bacteria(self, bacteria):
        self.bacteria.append(bacteria)

    def remove_bacteria(self, bacteria_id):
        self.bacteria = [b for b in self.bacteria if b.id != bacteria_id]
