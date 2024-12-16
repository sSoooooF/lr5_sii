import pygame
import sys
class Visualization:
    def __init__(self, grid, person, car):
        self.grid = grid
        self.person = person
        self.car = car
        self.cell_size = 30
        self.screen_width = grid.width * self.cell_size
        self.screen_height = grid.height * self.cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Car Assembly Simulation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.parts_positions = {
            'wheels': (10, 10),
            'battery': (0, 12),
            'headlights': (5, 14),
            'gas': (14, 5),
            'spark_plugs': (17, 7)
        }

    def draw_grid(self):
        self.screen.fill((255, 255, 255))
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                pygame.draw.rect(self.screen, (200, 200, 200), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), 1)

    def draw_obstacles(self):
        for obstacle in self.grid.obstacles:
            pygame.draw.rect(self.screen, (0, 0, 0), (obstacle[0] * self.cell_size, obstacle[1] * self.cell_size, self.cell_size, self.cell_size))

    def draw_car(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (self.car.x * self.cell_size, self.car.y * self.cell_size, self.car.width * self.cell_size, self.car.height * self.cell_size))

    def draw_person(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.person.x * self.cell_size + self.cell_size // 2 - 5, self.person.y * self.cell_size + self.cell_size // 2 - 5, 10, 10))

    def draw_parts(self):
        # Визуализация деталей
        for part, position in self.parts_positions.items():
            if part == 'wheels':
                color = (0, 0, 255)
                size = 20
            elif part == 'battery':
                color = (255, 255, 0)
                size = 30
            elif part == 'headlights':
                color = (0, 255, 255)
                size = 40
            elif part == 'gas':
                color = (128, 0, 128)
                size = 50
            elif part == 'spark_plugs':
                color = (128, 128, 0)
                size = 60

            pygame.draw.rect(self.screen, color, (position[0] * self.cell_size + self.cell_size // 2 - size // 2, position[1] * self.cell_size + self.cell_size // 2 - size // 2, size, size))

        # Подписи для деталей
        wheels_text = self.font.render("Wheels", True, (0, 0, 0))
        battery_text = self.font.render("Battery", True, (0, 0, 0))
        headlights_text = self.font.render("Headlights", True, (0, 0, 0))
        gas_text = self.font.render("Gas", True, (0, 0, 0))
        spark_plugs_text = self.font.render("Spark Plugs", True, (0, 0, 0))

        self.screen.blit(wheels_text, (self.parts_positions['wheels'][0] * self.cell_size, self.parts_positions['wheels'][1] * self.cell_size + self.cell_size))
        self.screen.blit(battery_text, (self.parts_positions['battery'][0] * self.cell_size, self.parts_positions['battery'][1] * self.cell_size + self.cell_size))
        self.screen.blit(headlights_text, (self.parts_positions['headlights'][0] * self.cell_size, self.parts_positions['headlights'][1] * self.cell_size + self.cell_size))
        self.screen.blit(gas_text, (self.parts_positions['gas'][0] * self.cell_size, self.parts_positions['gas'][1] * self.cell_size + self.cell_size))
        self.screen.blit(spark_plugs_text, (self.parts_positions['spark_plugs'][0] * self.cell_size, self.parts_positions['spark_plugs'][1] * self.cell_size + self.cell_size))

    def draw_state(self):
        state_text = self.font.render(f"Current State: {self.person.current_state.name}", True, (0, 0, 0))
        self.screen.blit(state_text, (10, 10))

    def update(self):
        self.draw_grid()
        self.draw_obstacles()
        self.draw_car()
        self.draw_person()
        self.draw_parts()
        self.draw_state()
        pygame.display.flip()
        self.clock.tick(60)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.person.next_step()
                        if self.car.is_ready():
                            print("Car is ready!")
                            running = False
            self.update()
        pygame.quit()
        sys.exit()
