alien = Actor('alien')
alien.pos = 100, 200
WIDTH = 800  # Screen width
HEIGHT = 600  # Screen height

def draw():
    screen.fill((20,50,100))
    alien.draw()

def update():
    alien.left += 2

    if alien.left > WIDTH:
        alien.left = 0

