class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []

    def add_obstacle(self, x, y):
        self.obstacles.append((x, y))

    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles
