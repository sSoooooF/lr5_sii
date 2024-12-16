class State:
    def __init__(self, name, preconditions, postconditions):
        self.name = name
        self.preconditions = preconditions
        self.postconditions = postconditions

    def __str__(self):
        return self.name
