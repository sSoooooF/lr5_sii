class Action:
    def __init__(self, name, state_transition):
        self.name = name
        self.state_transition = state_transition

    def __str__(self):
        return self.name
