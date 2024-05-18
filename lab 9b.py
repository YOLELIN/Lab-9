import random

class Agent:
    def __init__(self, world):
        self.world = world
        self.location = None

    def move(self):
        empty_locations = self.world.find_empty_locations()
        if empty_locations:
            new_location = random.choice(empty_locations)
            self.world.grid[self.location[0]][self.location[1]] = None
            self.world.grid[new_location[0]][new_location[1]] = self
            self.location = new_location

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(self) for _ in range(num_agents)]
        self.place_agents()

    def find_empty_locations(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if self.grid[x][y] is None]

    def place_agents(self):
        empty_locations = self.find_empty_locations()
        for agent in self.agents:
            location = random.choice(empty_locations)
            self.grid[location[0]][location[1]] = agent
            agent.location = location
            empty_locations.remove(location)

    def run(self, iterations):
        for _ in range(iterations):
            for agent in self.agents:
                agent.move()


world_size = 10
num_agents = 20 
iterations = 10 
world = World(world_size, num_agents)
world.run()