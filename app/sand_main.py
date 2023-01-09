### INIT OF THE GAME ###

class State:
    def __init__(self, will_change=False, moving=False, solid=False, liquid=False, gas=True, color="grey"):
        self.will_change = will_change
        self.moving = moving
        self.solid = solid
        self.liquid = liquid
        self.gas = gas
        self.color = color

# Create an air state for an air particle ---> this is also the default when creating a new grid, it will be full of air particles
air_state = State()

# Create a State object for the sand particle
sand_state = State(changing=True, moving=True, solid=False, liquid=False)

# Create a State object for the water particle
water_state = State(changing=True, moving=True, solid=False, liquid=True)

# Create a State object for the wood obstacle
wood_state = State(changing=False, moving=False, solid=True, liquid=False)

###############################################################################################################################

class Particle:
    def __init__(self, x, y, type, state):
        self.x = x
        self.y = y
        self.type = type
        self.state = state


# Create a grid of air-particles as the initial game state
grid_size = 5
grid = []
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        row.append(Particle(i, j, "air", air_state))
    grid.append(row)

###############################################################################################################################

class Obstacle:
    def __init__(self, x, y, type, state):
        self.x = x
        self.y = y
        self.type= type
        self.state = state
        self.blocking = True

# Create obstacle objects for wood at the bottom of the screen to test it
wood_obstacle1 = Obstacle(0, 4, "brown", wood_state)
wood_obstacle2 = Obstacle(1, 4, "brown", wood_state)
wood_obstacle3 = Obstacle(2, 4, "brown", wood_state)
wood_obstacle4 = Obstacle(3, 4, "brown", wood_state)
wood_obstacle5 = Obstacle(4, 4, "brown", wood_state)
       
###############################################################################################################################

class Environment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.particles= []
        self.obstacles = []
        self.special_surfaces = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def add_obstacle(self, x, y):
        self.obstacles.append((x, y))

    def add_special_surface(self, x, y, effect):
        self.special_surfaces.append((x, y, effect))

# init a environment instance
env = Environment(grid_size)

###############################################################################################################################

def get_neighbors(particle, env):
    neighbors = []
    # Check the 8 cells surrounding the particle and add any Particles or environment objects to the list
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x = particle.x + dx
            y = particle.y + dy
            if x < 0 or x >= env.grid_size or y < 0 or y >= env.grid_size:
                continue
            # Check if there is an environment object at (x, y)
            for obstacle in env.obstacles:
                if obstacle[0] == x and obstacle[1] == y:
                    # Add the obstacle to the list of neighbors
                    neighbors.append(((x, y), "obstacle", (dx, dy)))
                    break
            for surface in env.special_surfaces:
                if surface[0] == x and surface[1] == y:
                    # Add the special surface to the list of neighbors
                    neighbors.append(((x, y), surface[2], (dx, dy)))
                    break
            else:
                # No environment object was found, so add the particle at (x, y)
                neighbors.append((env.grid[x][y], (dx, dy)))
    return neighbors

###############################################################################################################################

def update_cell(particle, env):
    # Check the particle's neighbors to see if it should change state
    neighbors = get_neighbors(particle, env)
    if should_change_state(particle, neighbors):
        particle.state.will_change = True
    else:
        particle.state.will_change = False

    # Update the particle based on its type
    def air_update():
        # Do something for normal particles
        pass

    def sand_update():
        # Do something for gravity particles
        pass

    def fire_update():
        # Do something for fire particles
        pass
    # Define additional functions to handle other particle types

    def water_update():
        # Do something for fire particles
        pass

    def default_update():
        # Do something for unrecognized particle types
        pass

    switch = {
        "air": air_update,
        "sand": sand_update,
        "fire": fire_update,
        "water": water_update,
    }
    # Add additional cases to the switch dictionary to handle other particle types

    switch.get(particle.type, default_update)()

###############################################################################################################################

def should_change_state(particle, neighbours):
    # Return 'True' if particle should change state based on neighbours
    pass

###############################################################################################################################

for row in grid:
    for particle in row:
        update_cell(particle, env)
