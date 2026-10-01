import pygame as pg
import numpy as np
from random import randint

from math import sin, cos, asin, acos, tan, atan
from dataclasses import dataclass

@dataclass
class SimulationSettings:
    SCREEN = pg.display.set_mode((3100, 1400))
    CLOCK = pg.Clock()
    GRAVITATIONAL_CONSTANT: float = 6.6
    FPS: int = 60

@dataclass
class StandartObjectSettings:
    SIZE: tuple[int, int] = (32, 32)
    COLOR: tuple[int, int, int] = (255, 255, 255)

class CelestialObject(pg.sprite.Sprite):
    def __init__(self, id, x, y, mass, color, *groups):
        super().__init__(*groups)

        standart_settings = StandartObjectSettings()
        simulation_settings = SimulationSettings()

        self.id = id

        self.SCREEN = simulation_settings.SCREEN
        self.G = simulation_settings.GRAVITATIONAL_CONSTANT

        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, 0)
        self.acceleration = pg.Vector2(0, 0)
        
        self.mass = mass
        self.size = tuple(standart * mass/100 for standart in standart_settings.SIZE)
        self.color = color
        self.previous_acceleration = 0

        self.image = pg.Surface(self.size, pg.SRCALPHA)
        pg.draw.circle(self.image, self.color, (self.size[0]/2, self.size[0]/2), self.size[0]/2)
        self.rect = self.image.get_frect(center=self.position)
        

        # self.collision_rect = self.image.get_frect(center = self.size)
    
    def move(self, objs):
        object_list = np.array([0, 0, 0], dtype=np.float32)
        steps = 0

        for ind, obj in enumerate(objs):
            steps += 1


            # the issue with the dismissal of obj 3 ind 3 is due to this if function, it completely skips the entire steps == len(objs) at the end of the loop due to the last value of obj being 0
            if type(obj) is int or ind == len(objs) - 1:
                continue
            mx = obj[0]*obj[2]
            my = obj[1]*obj[2]
            m = obj[2]

            object_list += np.array([mx, my, m])


            # Apply center of mass according to the masses of the celestial objects
            print(steps, len(objs))
            if steps == len(objs):
                object_list = np.array([object_list[0]/object_list[2], object_list[1]/object_list[2], object_list[2]])

                print(object_list)


        objx, objy, objm = object_list

            
        # Dx, Dy = objx - self.position.x, objy - self.position.y
        # dist = np.sqrt(Dx**2 + Dy**2)

        
        # force = self.G*self.mass*objm/max(Dx**2 + Dy**2, 10000)
        # print(f"{self.id} object is exerting {force}")

        # force_x = force*(Dx/dist)
        # force_y = force*(Dy/dist)


        # acceleration_x = force_x/self.mass
        # acceleration_y = force_y/self.mass

        # # Stops following the cursor after a certain time period

        # self.acceleration = pg.Vector2(acceleration_x, acceleration_y)

        # print(self.acceleration)

        
        # self.velocity += self.acceleration

        # # print(f"velocity -> {self.velocity}\nacceleration -> {self.acceleration}\nforce -> {force}\ndist -> {dist}")
        # self.position += self.velocity

        # self.rect.x = self.position.x
        # self.rect.y = self.position.y



        """
        need physical time steps
        """


        



class Simulation:
    def __init__(self):

        simulation_settings = SimulationSettings()
        self.SCREEN = simulation_settings.SCREEN
        self.CLOCK = simulation_settings.CLOCK
        self.FPS = simulation_settings.FPS

        self.run_simulation = True

        self.celestial_object_group = pg.sprite.Group()

        self.celestial_objects = [
            (1, 1500, 600, 150, (255, 0, 0), self.celestial_object_group),
            (2, 2000, 450, 150, (0, 0, 255),self.celestial_object_group),
            (3, 2000, 300, 150, (0, 255, 0),self.celestial_object_group)
        ]


        for obj in self.celestial_objects:
            self.celestial_object = CelestialObject(*obj)

        for obj in self.celestial_object_group.sprites():

                obj.move([np.array([other_obj.rect.x, other_obj.rect.y, other_obj.mass]) if other_obj.id != obj.id else 0 for other_obj in self.celestial_object_group.sprites()])

    def run(self):
        while self.run_simulation:
            
            self.SCREEN.fill((10, 10, 25))

            mouse_pos = pg.mouse.get_pos()
            dt = self.CLOCK.tick(self.FPS) / 1000.0
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run_simulation = False


            self.celestial_object_group.draw(self.SCREEN)
            self.celestial_object_group.update()

            pg.display.flip()


if "__main__" == __name__:
    simulation = Simulation()
    simulation.run()


