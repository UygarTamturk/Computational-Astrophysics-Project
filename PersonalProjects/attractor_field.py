import pygame as pg
import numpy as np
from dataclasses import dataclass

@dataclass
class SimulationSettings:
    SCREEN = pg.display.set_mode((2500, 1200))
    CLOCK = pg.Clock()
    FPS: int = 60

class Arrow(pg.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        simulation_settings = SimulationSettings()
        self.SCREEN = simulation_settings.SCREEN

        self.position = pg.Vector2(x, y)
        self.magnitude = 10

        self.original_image = pg.Surface((16, 16), pg.SRCALPHA)

        self.image = self.original_image.copy()
        self.rect = self.image.get_frect(center = (x, y))

    def change_color(self, distance):
        color = (255, 255, 255)

        reduce_color = (0, round(distance/2), 10 * round(distance/2))
        
        color = tuple(max(0, val - sub) for val, sub in zip(color, reduce_color))
        self.original_image.fill(color)

    def rotation_towards_object(self, objx, objy):
        

        Dx, Dy = self.position.x - objx, self.position.y - objy
        theta = np.atan2(Dy, Dx)
        angle = -np.degrees(theta)
        
        distance = np.sqrt(Dx**2 + Dy**2)

        self.image = pg.transform.rotozoom(self.original_image, angle, max(0, 1 - distance/1250))
        self.rect = self.image.get_frect(center = (self.position.x, self.position.y))
        self.change_color(distance)

class Object(pg.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        simulation_settings = SimulationSettings()
        self.SCREEN = simulation_settings.SCREEN

        self.position = pg.Vector2(x, y)
        self.direction = pg.Vector2(-1, 1)

        self.image = pg.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_frect(center = (x, y))

    def move(self):
        self.position += 10*self.direction
        if self.position.x >= self.SCREEN.width + self.image.size[0] or self.position.x <= -self.image.size[0]:
            self.position.x = self.position.x - self.SCREEN.width*self.direction.x

        if self.position.y >= self.SCREEN.height + self.image.size[1] or self.position.y <= -self.image.size[1]:
            self.position.y = self.position.y - self.SCREEN.height*self.direction.y

        print(self.position)
        self.rect = self.image.get_frect(center = (self.position.x, self.position.y))

    def positional_value(self):
        return (self.position.x, self.position.y)

class Simulation:
    def __init__(self):
        simulation_settings = SimulationSettings()
        self.SCREEN = simulation_settings.SCREEN
        self.CLOCK = simulation_settings.CLOCK
        self.FPS = simulation_settings.FPS
        self.run = True

        self.arrow_group = pg.sprite.Group()
        self.object_group = pg.sprite.Group()

        self.object_ = Object(self.SCREEN.width/2, self.SCREEN.height/2, self.object_group)

        width, height = self.SCREEN.width, self.SCREEN.height
        gap = 25
        for i in range(round(height/gap)):
            for j in range(round(width/gap)):
                arrow = Arrow(gap*j, gap*i, self.arrow_group)



    def run_simulation(self):
        while self.run:
            mouse_pos = pg.mouse.get_pos()
            self.SCREEN.fill((10, 10, 25))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

            self.object_.move()
            for arrow in self.arrow_group.sprites():
                arrow.rotation_towards_object(mouse_pos[0], mouse_pos[1]) #*self.object_.positional_value()

            self.arrow_group.draw(self.SCREEN)
            self.arrow_group.update()

            # self.object_group.draw(self.SCREEN)
            # self.object_group.update()

            self.CLOCK.tick(self.FPS)
            pg.display.flip()



if "__main__" == __name__:
    simulation = Simulation()
    simulation.run_simulation()