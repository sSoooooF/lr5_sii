from state import State
from action import Action
from car import Car
from person import Person
from grid import Grid
from obstacle import Obstacle
from visualization import Visualization
import random
from a_star import a_star

def main():
    # Initialize grid
    grid = Grid(20, 20)

    # Generate random parts positions
    parts_positions = {}
    for part in ['wheels', 'battery', 'headlights', 'gas', 'spark_plugs']:
        while True:
            x = random.randint(0, grid.width - 1)
            y = random.randint(0, grid.height - 1)
            if (x, y) not in parts_positions.values() and (x, y) != (15, 15):  # Avoid car position
                parts_positions[part] = (x, y)
                break

    # Add obstacles randomly, avoiding parts positions and ensuring paths
    obstacles = set()
    for _ in range(50):  # Number of obstacles
        while True:
            x = random.randint(0, grid.width - 1)
            y = random.randint(0, grid.height - 1)
            if (x, y) not in parts_positions.values() and (x, y) != (15, 15) and (x, y) not in obstacles:
                obstacles.add((x, y))
                break

    # Ensure there are paths to each part
    for part, position in parts_positions.items():
        path = a_star(grid, (0, 0), position, obstacles)
        if not path:
            print(f"No path to {part} at {position}, regenerating obstacles")
            obstacles = set()
            for _ in range(50):  # Number of obstacles
                while True:
                    x = random.randint(0, grid.width - 1)
                    y = random.randint(0, grid.height - 1)
                    if (x, y) not in parts_positions.values() and (x, y) != (15, 15) and (x, y) not in obstacles:
                        obstacles.add((x, y))
                        break
            # Recheck paths
            for part, position in parts_positions.items():
                path = a_star(grid, (0, 0), position, obstacles)
                if not path:
                    print(f"Still no path to {part} at {position}, exiting")
                    return

    grid.obstacles = list(obstacles)

    # Initialize car
    car = Car(15, 15, 2, 4)

    # Initialize states
    states = [
        State('pick up wheels', lambda: True, lambda: car.parts['wheels']),
        State('install wheels', lambda: 'wheels' in car.parts, lambda: car.parts['wheels']),
        State('pick up battery', lambda: car.parts['wheels'], lambda: car.parts['battery']),
        State('install battery', lambda: 'battery' in car.parts, lambda: car.parts['battery']),
        State('pick up headlights', lambda: car.parts['battery'], lambda: car.parts['headlights']),
        State('install headlights', lambda: 'headlights' in car.parts, lambda: car.parts['headlights']),
        State('pick up gas', lambda: car.parts['headlights'], lambda: car.parts['gas']),
        State('install gas', lambda: 'gas' in car.parts, lambda: car.parts['gas']),
        State('pick up spark plugs', lambda: car.parts['gas'], lambda: car.parts['spark_plugs']),
        State('install spark plugs', lambda: 'spark_plugs' in car.parts, lambda: car.parts['spark_plugs']),
        State('start engine', lambda: car.parts['spark_plugs'], lambda: car.parts['engine_started'])
    ]

    # Initialize person
    person = Person(0, 0, states, car, grid)
    person.parts_positions = parts_positions

    # Initialize visualization
    visualization = Visualization(grid, person, car)
    visualization.run()

if __name__ == "__main__":
    main()
