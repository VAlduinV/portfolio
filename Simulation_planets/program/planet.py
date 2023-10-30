import pygame
import logging
import math
from constants import *

pygame.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

font_path = "fonts/Beking-Font.ttf"
font = pygame.font.Font(font_path, 16)

# Ініціалізація звуку
sound_path = "music/ObservingTheStar.ogg"
pygame.mixer.music.load(sound_path)

logging.basicConfig(filename='../planets_simulation.log', level=logging.INFO, encoding='utf-8')


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day
    ORBIT_SAVE_INTERVAL = 10  # Зберігайте точку орбіти кожні 10 оновлень (збільшуйте або зменшуйте за необхідності)
    MAX_ORBIT_POINTS = 100

    # Загрузіть текстури і збережіть їх у словнику для ефективного використання
    TEXTURES = {
        "earth": pygame.transform.scale(pygame.image.load("images/earth.png").convert_alpha(), (50, 50)),
        "mars": pygame.transform.scale(pygame.image.load("images/mars.png").convert_alpha(), (30, 30)),
        "mercury": pygame.transform.scale(pygame.image.load("images/mercury.png").convert_alpha(), (15, 15)),
        "venus": pygame.transform.scale(pygame.image.load("images/venus.png").convert_alpha(), (20, 20)),
        "sun": pygame.transform.scale(pygame.image.load("images/sun.png").convert_alpha(), (150, 150)),
        "space": pygame.image.load("images/space.png").convert_alpha(),
        # Додайте інші текстури планет, які ви використовуєте
    }

    def __init__(self, x, y, radius, color, mass, texture_key):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_x_vel = self.x_vel
        self.prev_y_vel = self.y_vel

        # Використовуємо текстури зі словника замість завантаження зображення з диску кожного разу
        self.texture = self.TEXTURES[texture_key]

        logging.info(
            f'Planet created: x={x}, y={y}, radius={radius}, color={color}, mass={mass}, texture={texture_key}')

    def draw(self, win):
        x = int(self.x * self.SCALE + WIDTH / 2)
        y = int(self.y * self.SCALE + HEIGHT / 2)

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x_orbit, y_orbit = point
                x_orbit = x_orbit * self.SCALE + WIDTH / 2
                y_orbit = y_orbit * self.SCALE + HEIGHT / 2
                updated_points.append((x_orbit, y_orbit))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = font.render(f"{round(self.distance_to_sun / 1000, 1)}km", True, "GREEN")
            # win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))
            # Розмістити надпис нижче планети (відступ в 5 пікселів від нижньої межі планети)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y + self.radius + 5))

        # draw the planet texture
        texture_rect = self.texture.get_rect(center=(x, y))
        win.blit(self.texture, texture_rect)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        if self.prev_x != self.x or self.prev_y != self.y or self.prev_x_vel != self.x_vel or self.prev_y_vel != self.y_vel:
            total_fx = total_fy = 0
            for planet in planets:
                if self == planet:
                    continue

                fx, fy = self.attraction(planet)
                total_fx += fx
                total_fy += fy

            self.x_vel += total_fx / self.mass * self.TIMESTEP
            self.y_vel += total_fy / self.mass * self.TIMESTEP

            self.prev_x = self.x
            self.prev_y = self.y
            self.prev_x_vel = self.x_vel
            self.prev_y_vel = self.y_vel

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        # Додайте поточну позицію планети до списку орбіт
        self.orbit.append((self.x, self.y))

        # Додайте поточну позицію планети до списку орбіт кожні ORBIT_SAVE_INTERVAL оновлень
        if pygame.time.get_ticks() % (self.ORBIT_SAVE_INTERVAL * self.TIMESTEP * 1000) == 0:
            self.orbit.append((self.x, self.y))

        # Видаліть найстаріші точки орбіти, якщо їх кількість перевищує MAX_ORBIT_POINTS
        if len(self.orbit) > self.MAX_ORBIT_POINTS:
            self.orbit.pop(0)

        logging.info(f'Planet position updated: x={self.x}, y={self.y}, x_vel={self.x_vel}, y_vel={self.y_vel}')