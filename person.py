from state import State
from action import Action
from car import Car
from a_star import a_star

class Person:
    def __init__(self, x, y, states, car, grid):
        self.x = x
        self.y = y
        self.states = states
        self.current_state = states[0]
        self.car = car
        self.grid = grid
        self.inventory = {}
        self.target = None
        self.path = []
        self.parts_positions = {
            'wheels': (10, 10),
            'battery': (0, 12),
            'headlights': (5, 14),
            'gas': (14, 5),
            'spark_plugs': (17, 7)
        }

    def move_to(self, x, y):
        if self.grid.is_valid(x, y) and (x, y) not in self.grid.obstacles:
            self.x = x
            self.y = y

    def pick_up_part(self, part):
        self.inventory[part] = True

    def install_part(self, part):
        if part in self.inventory:
            self.car.install_part(part)
            del self.inventory[part]

    def next_step(self):
        if not self.path:
            if self.current_state.name == 'pick up wheels':
                self.target = self.parts_positions['wheels']
            elif self.current_state.name == 'install wheels':
                self.target = (self.car.x, self.car.y)
            elif self.current_state.name == 'pick up battery':
                self.target = self.parts_positions['battery']
            elif self.current_state.name == 'install battery':
                self.target = (self.car.x, self.car.y)
            elif self.current_state.name == 'pick up headlights':
                self.target = self.parts_positions['headlights']
            elif self.current_state.name == 'install headlights':
                self.target = (self.car.x, self.car.y)
            elif self.current_state.name == 'pick up gas':
                self.target = self.parts_positions['gas']
            elif self.current_state.name == 'install gas':
                self.target = (self.car.x, self.car.y)
            elif self.current_state.name == 'pick up spark plugs':
                self.target = self.parts_positions['spark_plugs']
            elif self.current_state.name == 'install spark plugs':
                self.target = (self.car.x, self.car.y)
            elif self.current_state.name == 'start engine':
                self.target = (self.car.x, self.car.y)

            self.path = a_star(self.grid, (self.x, self.y), self.target)
            if not self.path:
                print(f"Cannot reach target {self.target} from ({self.x}, {self.y})")
                return

        if self.path:
            next_step = self.path[0]
            self.move_to(next_step[0], next_step[1])
            self.path = self.path[1:]

            if (self.x, self.y) == self.target:
                if self.current_state.name in ['pick up wheels', 'pick up battery', 'pick up headlights', 'pick up gas', 'pick up spark plugs']:
                    part_name = self.current_state.name.replace('pick up ', '')
                    self.pick_up_part(part_name)
                    # Переход к состоянию установки детали
                    next_state_name = f'install {part_name}'
                    self.current_state = next((state for state in self.states if state.name == next_state_name), None)
                    if self.current_state is None:
                        print("Invalid state transition")
                        return
                    self.target = (self.car.x, self.car.y)
                    self.path = a_star(self.grid, (self.x, self.y), self.target)
                    if not self.path:
                        print(f"Cannot reach target {self.target} from ({self.x}, {self.y})")
                        return
                elif self.current_state.name in ['install wheels', 'install battery', 'install headlights', 'install gas', 'install spark plugs']:
                    part_name = self.current_state.name.replace('install ', '')
                    self.install_part(part_name)
                    # Переход к следующему состоянию после установки детали
                    next_state_index = self.states.index(self.current_state) + 1
                    if next_state_index < len(self.states):
                        self.current_state = self.states[next_state_index]
                    else:
                        print("Car is ready!")
                elif self.current_state.name == 'start engine':
                    self.car.parts['engine_started'] = True
                    print("Car is ready!")

    def find_path(self, x, y):
        return a_star(self.grid, (self.x, self.y), (x, y))
