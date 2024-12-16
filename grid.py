class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []

    def is_valid(self, x, y, obstacles=None):
        if obstacles is None:
            obstacles = self.obstacles
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in obstacles
