import os
from planet import *

os.environ['SDL_AUDIODRIVER'] = 'dsp'


def main():
    run = True
    clock = pygame.time.Clock()
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30, "sun")
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24, "earth")
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.490 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23, "mars")
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.400 * Planet.AU, 0, 8, AUBURN, 4.0 * 10 ** 23, "mercury")
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 10, WHITE, 4.8685 * 10 ** 24, "venus")
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    # Відтворення звуку
    pygame.mixer.music.play(-1)

    while run:
        clock.tick(60)
        WIN.blit(Planet.TEXTURES["space"], (0, 0))  # Використовуємо зображення космосу як тло

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    # Зупинка звуку
    pygame.mixer.music.stop()

    pygame.quit()
    logging.info('Simulation completed')


if __name__ == '__main__':
    print("""
     ____  _  _      _     _     ____  _____  _  ____  _        ____  _____   ____  _     ____  _      _____ _____  ____ 
    / ___\/ \/ \__/|/ \ /\/ \   /  _ \/__ __\/ \/  _ \/ \  /|  /  _ \/    /  /  __\/ \   /  _ \/ \  /|/  __//__ __\/ ___\
    |    \| || |\/||| | ||| |   | / \|  / \  | || / \|| |\ ||  | / \||  __\  |  \/|| |   | / \|| |\ |||  \    / \  |    \
    \___ || || |  ||| \_/|| |_/\| |-||  | |  | || \_/|| | \||  | \_/|| |     |  __/| |_/\| |-||| | \|||  /_   | |  \___ |
    \____/\_/\_/  \|\____/\____/\_/ \|  \_/  \_/\____/\_/  \|  \____/\_/     \_/   \____/\_/ \|\_/  \|\____\  \_/  \____/
    """)
    main()
