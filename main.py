from state import State
from action import Action
from car import Car
from person import Person
from grid import Grid
from obstacle import Obstacle
from visualization import Visualization
def main():
    # Initialize grid
    grid = Grid(20, 20)

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

    # Initialize visualization
    visualization = Visualization(grid, person, car)
    visualization.run()

if __name__ == "__main__":
    main()
