class Car:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.parts = {
            'wheels': False,
            'battery': False,
            'headlights': False,
            'gas': False,
            'spark_plugs': False,
            'engine_started': False
        }

    def install_part(self, part):
        if part in self.parts:
            self.parts[part] = True

    def is_ready(self):
        return all(self.parts.values())
