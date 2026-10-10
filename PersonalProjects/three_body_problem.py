import pygame as pg
import numpy as np

import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt

import pandas as pd

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

def visualise_data(object_, time):

    # having two DataFrames just to store object index and object data seperately is inefficient. Reduce it to one DataFrame

    # object_id (integer), object_data (DataFrame form)
    object_ = object_.to_numpy()
    object_id = object_[:, 0]
    object_data = object_[:, 1]


    figure, ax = plt.subplots()

    print(object)

    for ind in range(len(object_)):
        ax.plot(time, object_data[ind][0].y, marker="o", label=f"{object_id[ind]}")

    ax.set_xlabel("time")
    ax.set_ylabel("x position")
    ax.set_title("observation")
    ax.legend()

    canvas = agg.FigureCanvasAgg(figure)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()

    size = canvas.get_width_height()
    surf = pg.image.frombuffer(raw_data, size, "RGBA")

    plt.close(figure)

    return surf

    

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

        self.own_data = [self.position, self.velocity, self.acceleration]
        self.index = ["position", "velocity", "acceleration"]
        

        # self.collision_rect = self.image.get_frect(center = self.size)
    
    def move(self, objs, dt):

        # Energy Loss can be implemented to avoid repeated, predictable and unrealistic actions

        total_force = np.array([0, 0], dtype=np.float32)
        
        ## Center of Mass Method ->Does not obey to Newton's Third Law of Motion
        # object_list = np.array([0, 0, 0], dtype=np.float32)
        steps = 0

        for ind, obj in enumerate(objs):
            steps += 1

            
            if not type(obj) is int:
                Dx, Dy = obj[0] - self.position.x, obj[1] - self.position.y
                dist = np.sqrt(max(Dx**2 + Dy**2, 10000))
            
                force = self.G*self.mass*obj[2]/(dist**2)
                # print(f"{self.id} object is exerting {force}")

                force_x = force*(Dx/dist)
                force_y = force*(Dy/dist)

                total_force += np.array([force_x, force_y])

            



            ## Center of Mass Method -> Does not obey to Newton's Third Law of Motion
            # if not type(obj) is int:
            #     mx = obj[0]*obj[2]
            #     my = obj[1]*obj[2]
            #     m = obj[2]

            #     object_list += np.array([mx, my, m])
            # if steps == len(objs):
            #     object_list = np.array([object_list[0]/object_list[2], object_list[1]/object_list[2], object_list[2]])

            #     print(object_list)
        

        acceleration_x = total_force[0]/self.mass
        acceleration_y = total_force[1]/self.mass

        self.acceleration = pg.Vector2(acceleration_x, acceleration_y)     
        self.velocity += self.acceleration

        # print(f"velocity -> {self.velocity}\nacceleration -> {self.acceleration}\nforce -> {force}\ndist -> {dist}")
        self.position += self.velocity * dt

        self.rect = self.image.get_frect(center=self.position)

        for ind in range(len(self.own_data)):
            # print(self.own_data[item])
            self.own_data[ind] = getattr(self, self.index[ind])



        """
        need physical time steps
        """

    def return_data(self):
        return self.own_data
        



class Simulation:
    def __init__(self):

        simulation_settings = SimulationSettings()
        self.SCREEN = simulation_settings.SCREEN
        self.CLOCK = simulation_settings.CLOCK
        self.FPS = simulation_settings.FPS
        
        self.time_taken = 0
        self.run_simulation = True

        self.celestial_object_group = pg.sprite.Group()

        self.celestial_objects = [
            (1, 1500, 600, 150, (255, 0, 0), self.celestial_object_group),
            (2, 2000, 450, 150, (0, 0, 255),self.celestial_object_group),
            (3, 2000, 300, 150, (0, 255, 0),self.celestial_object_group),
        ]


        for obj in self.celestial_objects:
            self.celestial_object = CelestialObject(*obj)


    def run(self):
        while self.run_simulation:
            
            self.SCREEN.fill((10, 10, 25))

            mouse_pos = pg.mouse.get_pos()
            dt = self.CLOCK.tick(self.FPS) / 1000.0
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run_simulation = False

            total_data = pd.DataFrame({})
            for obj in self.celestial_object_group.sprites():
                obj.move([np.array([other_obj.rect.x, other_obj.rect.y, other_obj.mass]) if other_obj.id != obj.id else 0 for other_obj in self.celestial_object_group.sprites()], dt)
                new_data = [{"object_id": obj.id, "object_data": obj.return_data()}]
                total_data = pd.concat([total_data, pd.DataFrame(new_data)], ignore_index=True)

            surf = visualise_data(total_data, self.time_taken)
            
            self.time_taken += dt

            self.celestial_object_group.draw(self.SCREEN)
            self.celestial_object_group.update()

            self.SCREEN.blit(surf, (50, 50))

            pg.display.flip()
            plt.show()


if "__main__" == __name__:

    simulation = Simulation()
    simulation.run()