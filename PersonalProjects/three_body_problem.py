import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from random import randint
from math import sin, cos, asin, acos, tan, atan
from dataclasses import dataclass

@dataclass
class SimulationSettings:
    SCREEN = pg.display.set_mode((3100, 1400))
    CLOCK = pg.Clock()
    GRAVITATIONAL_CONSTANT: float = 7
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
        self.force = pg.Vector2(0, 0) # for debugging purposes
        
        self.mass = mass
        self.size = tuple(standart * mass/100 for standart in standart_settings.SIZE)
        self.color = color
        self.previous_acceleration = 0

        self.image = pg.Surface((self.size[0], self.size[1]), pg.SRCALPHA)
        pg.draw.circle(self.image, self.color, (self.size[0]/2, self.size[0]/2), self.size[0]/2)
        self.rect = self.image.get_frect(center=self.position)

    def collision_check(objs, dt):
        for index, object in enumerate(objs):
            collide_list = object.rect.collidelistall(objs)
            for collided_object in collide_list:
                if collided_object <= index:
                    continue

                other_object = objs[collided_object]

                pos1, pos2 = object.position, other_object.position
                Dpos = pos2 - pos1
                dist = Dpos.length()
                print(dist, object.size[0]/2 + other_object.size[0]/2)

                max_center_distance = object.size[0]/2 + other_object.size[0]/2

                if dist > max_center_distance + 5 or dist < max_center_distance - 5:
                    
                    v1, v2 = object.velocity, other_object.velocity
                    m1, m2 = object.mass, other_object.mass
                    
                    unit_direction = Dpos.normalize()
                    
                    v1_c_scalar = v1.dot(unit_direction)
                    v2_c_scalar = v2.dot(unit_direction)
                     
                    f_v1_c_sc = (m1 - m2)/(m1 + m2)*v1_c_scalar + (2*m2)/(m1 + m2)*v2_c_scalar
                    f_v2_c_sc = (2*m1)/(m1 + m2)*v1_c_scalar + (m2 - m1)/(m1 + m2)*v2_c_scalar
                    
                    f_v1 = f_v1_c_sc * unit_direction
                    f_v2 = f_v2_c_sc * unit_direction
                    
                    object.velocity = f_v1
                    other_object.velocity = f_v2


                # marked_objects.iloc[index]["total_velocity"] += f_v1 *     
                # marked_objects.iloc[collided_object]["total_velocity"] += f_v2 * dt

        # print(marked_objects)

        # for index, object in enumerate(marked_objects["object"]):
        #     object.velocity = marked_objects.iloc[index]["total_velocity"]



        # v1f = (m1 - m2)/(m1 + m2)*v1i + (2*m2)/(m1 + m2)*v2i
        # v2f = (2*m1)/(m1 + m2)*v1i + (m2 - m1)/(m1 + m2)*v2i

        # x object - y object -> calculate two final velocities and two momentums
        # f_velocity = pg.Vector2((self_obj.mass - obj.mass)/(self_obj.mass + obj.mass)*self_obj + (2*other_mass)/(self.mass + other_mass)*other_velocity)
        # print(f_velocity)
        # f_momentum = f_velocity * self.mass



    
    def move(self, objs, dt):
        # Energy Loss can be implemented to avoid repeated, predictable and unrealistic actions

        total_force = np.array([0, 0], dtype=np.float32)

        for obj in objs:
            if not type(obj) is int:

                other_position = obj.position
                other_velocity = obj.velocity
                other_mass = obj.mass

                Dx, Dy = other_position.x - self.position.x, other_position.y - self.position.y
                dist = np.sqrt(max(Dx**2 + Dy**2, 10000))
            
                force = self.G*self.mass*other_mass/(dist**2)


                force_x = force*(Dx/dist)
                force_y = force*(Dy/dist)

                self.force = pg.Vector2(force_x, force_y)

                total_force += np.array([force_x, force_y])
        

        acceleration_x = total_force[0]/self.mass
        acceleration_y = total_force[1]/self.mass

        self.acceleration = pg.Vector2(acceleration_x, acceleration_y)     
        self.velocity += self.acceleration

        # print(f"velocity -> {self.velocity}\nacceleration -> {self.acceleration}\nforce -> {force}\ndist -> {dist}")
        self.position += self.velocity * dt

        self.rect = self.image.get_frect(center=self.position)

        """
        need physical time steps
        """




class Simulation:
    def __init__(self):

        simulation_settings = SimulationSettings()
        self.SCREEN = simulation_settings.SCREEN
        self.CLOCK = simulation_settings.CLOCK
        self.FPS = simulation_settings.FPS
        
        self.time_taken = 0
        self.run_simulation = True

        self.celestial_object_group = pg.sprite.Group()


        self.slice = 5
        self.screen_cells = np.array([[pg.rect.Rect(j*self.SCREEN.width/self.slice, i*self.SCREEN.height/self.slice, self.SCREEN.width/self.slice, self.SCREEN.height/self.slice) for j in range(self.slice)] for i in range(self.slice)])
        

 
        n = 3

        self.celestial_objects = []
        for i in range(n):
            object_x = randint(100, self.SCREEN.width-100)
            object_y = randint(50, self.SCREEN.height-50)
            mass = randint(200, 300)
            color = (randint(50, 200), randint(50, 200), randint(50, 200))
            

            self.celestial_objects.append((i, object_x, object_y, mass, color, self.celestial_object_group))

        for obj in self.celestial_objects:
            self.celestial_object = CelestialObject(*obj)


    def run(self):
        while self.run_simulation:
            
            self.SCREEN.fill((10, 10, 25))
            dt = self.CLOCK.tick(self.FPS) / 100.0
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run_simulation = False

            for obj in self.celestial_object_group.sprites():
                obj.move([other_obj if other_obj.id != obj.id else 0 for other_obj in self.celestial_object_group.sprites()], dt)

            for c in self.screen_cells:
                for r in c:
                    r = pg.Rect(r[:])
                    objs = r.collideobjectsall(self.celestial_object_group.sprites())
                    if len(objs) == 0:
                        continue

                    CelestialObject.collision_check(objs, dt)




            self.time_taken += dt

            self.celestial_object_group.draw(self.SCREEN)
            self.celestial_object_group.update()

            pg.display.flip()
            plt.show()


if "__main__" == __name__:

    simulation = Simulation()
    simulation.run()