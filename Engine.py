import pymunk
import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a Space which contains the simulation
space = pymunk.Space()
space.gravity = 0, -981  # Set gravity (you can adjust this value)

# Create a dictionary to store object properties
objects = {}

def create_ball(position, mass=10, radius=20):
    body = pymunk.Body()
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    space.add(body, shape)
    return body

def create_plank(position, mass=20, width=100, height=10):
    body = pymunk.Body()
    body.position = position
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.mass = mass
    space.add(body, shape)
    return body

# Create initial objects
objects["ball"] = create_ball((100, 100))
objects["plank"] = create_plank((400, 200))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Step the simulation one step forward
    space.step(0.02)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the objects
    for obj_name, body in objects.items():
        if isinstance(body.shapes[0], pymunk.Circle):
            x, y = body.position
            radius = body.shapes[0].radius
            pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), int(radius))
        elif isinstance(body.shapes[0], pymunk.Poly):
            points = body.shapes[0].get_vertices()
            pygame.draw.polygon(screen, (0, 0, 0), points)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate

# Clean up
pygame.quit()
