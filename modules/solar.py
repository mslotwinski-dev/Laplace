import pygame
import sys
import math

WIDTH, HEIGHT = 1200, 800


class Planet:
    AU = 149.6e9
    G = 6.67428e-11
    SCALE = 100 / AU
    TIMESTEP = 3600 * 24

    def __init__(self, x, y, r, m, color):
        self.x = x
        self.y = y
        self.r = r
        self.m = m
        self.color = color

        self.orbit = []
        self.sun = False
        self.R = 0

        self.x_vel = 0

        if self.sun == False and self.x != 0:
            self.y_vel = math.sqrt(self.G * 1.98892e30 / abs(self.x))
        else:
            self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.r)

    def gravity(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        F = self.G * self.m * other.m / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        F_x = math.cos(theta) * F
        F_y = math.sin(theta) * F

        return F_x, F_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.gravity(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += (total_fx / self.m) * self.TIMESTEP
        self.y_vel += (total_fy / self.m) * self.TIMESTEP

        if self.sun == False:
            self.x += self.x_vel * self.TIMESTEP
            self.y += self.y_vel * self.TIMESTEP
            self.orbit.append((self.x, self.y))


Sun = Planet(0, 0, 30, 1.98892e30, "#ffff00")
Sun.sun == True

Mercury = Planet(0.387 * Planet.AU, 0, 8, 3.30e23, "#bbbbbb")
Venus = Planet(0.723 * Planet.AU, 0, 14, 4.8685e24, "#cccc22")
Earth = Planet(- Planet.AU, 0, 16, 5.9742e24, "#00647d")
Mars = Planet(-1.524 * Planet.AU, 0, 12, 6.39e23, "#cc0000")

Jupiter = Planet(5.2 * Planet.AU, 0, 12, 1.89813e27, "#999944")
Saturn = Planet(-9.5 * Planet.AU, 0, 12, 5.683e26, "#eeee11")
Uranus = Planet(19.8 * Planet.AU, 0, 12, 8.681e25, "#22dddd")
Neptune = Planet(30 * Planet.AU, 0, 12, 1.024e26, "#2244dd")

Pluto = Planet(-39 * Planet.AU, 0, 12, 1.309e22, "#dddddd")


def Solar(Window):
    clock = pygame.time.Clock()

    while True:

        clock.tick(144)
        Window.fill("#222222")

        planets = [Sun, Mercury, Venus, Earth, Mars,
                   Jupiter, Saturn, Uranus, Neptune, Pluto]

        for planet in planets:
            planet.update_position(planets)
            planet.draw(Window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
