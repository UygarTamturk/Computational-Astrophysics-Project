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


class Hierarchy(pg.sprite.Sprite):
    def __init__(self, rect_value, layer_id, line_id, groups):
        super().__init__(groups)

        self.group = groups

        self.simulation_settings = SimulationSettings()
        self.SCREEN = self.simulation_settings.SCREEN

        # we might not need layer_id as the length of line_id gives the id of the layer
        self.layer_id = layer_id
        self.line_id = line_id

        self.rect_value = pg.Rect(*rect_value)
        self.hierarchy_list = {1: []}

        self.max_sprites = 1

    def organize_hierarchy(self, layer=None):
        print(f" 1{self.hierarchy_list}")

        # if an index of a layer does not exist, delete it too from the self.hierarchy_list
        if layer != None and len(self.hierarchy_list) > 1:
            self.hierarchy_list[layer.layer_id].pop(layer.line_id[len(layer.line_id) - 1] - 1)
            pass

        for _layer in self.group.sprites():

            if not _layer.layer_id in self.hierarchy_list.keys():
                self.hierarchy_list[_layer.layer_id] = [_layer]
                continue

            elif _layer in self.hierarchy_list[_layer.layer_id]:
                continue
            
            self.hierarchy_list[_layer.layer_id].append(_layer)

    def pull_rect(self):
        return self.rect_value

    def check_sprites(self, others):

        # add something so if all sublayers have no active sprites, delete all 4 layers (except for the parent layer as it is either the top layer or another sublayer of another parent layer)
        # check objects from the bottom of the hierarchy, then go up in the list
        # because we are splitting sublayer classes, we should somehow turn the sublayers into layers that will have new sublayers, deleting the sublayer class might be an option

        bottom_sublayers = self.hierarchy_list[len(self.hierarchy_list)]
        for index, layer in enumerate(bottom_sublayers):

            collide_list = layer.rect_value.collidelistall(others)
            check = True

            # gotta update it so if it finds a collision, it should pass the entire checking
            if len(collide_list) == 0:
                parent_layer = layer.get_parent()
                parent_sublayers = parent_layer.get_sublayers()
                for sublayer in parent_sublayers:
                    if sublayer.rect_value.collidelistall(others):
                        print("YES IT SURVIVED!")
                        pass

                print("oh no")
                parent_layer.delete_sublayers()
                pass

            elif len(collide_list) > 0 and len(collide_list) <= self.max_sprites:
                pass

            else:
                layer.split_layer()
            
class Layer(Hierarchy, pg.sprite.Sprite):
    def __init__(self, rect_value, layer_id, line_id, parent, groups):
        super().__init__(rect_value, layer_id, line_id, groups)

        self.parent = parent
        self.sublayers = []

    def add_sublayers(self, sublayers):
        for sublayer in sublayers:
            self.sublayers.append(sublayer)

    def delete_sublayers(self):
        for sublayer in self.sublayers:
            self.organize_hierarchy(sublayer)
            del sublayer

        self.sublayers.clear()
        
    def split_layer(self):

        # fix nx, ny, nw, nh values by using width*i and height*i (with offset using original layer's x and y position)

        # dont forget to entegrate sprite inserting for sublayers
        x, y, w, h = self.rect_value
        new_sublayers = []

        

        for i in range(2):
            for j in range(2):

                
                
                sublayer_line_id = self.line_id.copy()
                sublayer_line_id.append(i*2 + j + 1)
                

                nw = w/2
                nh = h/2

                nx = x + nw*j
                ny = y + nh*i

                sublayer = Layer((nx, ny, nw, nh), self.layer_id + 1, sublayer_line_id, self, self.group)

                new_sublayers.append(sublayer)

        
        self.add_sublayers(new_sublayers)

    def get_sublayers(self):
        return self.sublayers

    def get_parent(self):
        return self.parent

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

                max_center_distance = object.size[0]/2 + other_object.size[0]/2

                if dist < max_center_distance:
                    
                    v1, v2 = object.velocity, other_object.velocity
                    m1, m2 = object.mass, other_object.mass
                    
                    unit_direction = Dpos.normalize()
                    
                    v1_c_scalar = v1.dot(unit_direction)
                    v2_c_scalar = v2.dot(unit_direction)
                     
                    f_v1_c_sc = (m1 - m2)/(m1 + m2)*v1_c_scalar + (2*m2)/(m1 + m2)*v2_c_scalar
                    f_v2_c_sc = (2*m1)/(m1 + m2)*v1_c_scalar + (m2 - m1)/(m1 + m2)*v2_c_scalar
                    
                    f_v1 = f_v1_c_sc * unit_direction
                    f_v2 = f_v2_c_sc * unit_direction

                    overlap = max_center_distance - dist + 0.1
                    object.position -= unit_direction * (overlap / 2)
                    other_object.position += unit_direction * (overlap / 2)
                    
                    object.velocity = f_v1
                    other_object.velocity = f_v2
  
    def move(self, objs, dt):
        # Energy Loss can be implemented to avoid repeated, predictable and unrealistic actions

        total_force = np.array([0, 0], dtype=np.float32)

        for obj in objs:
            if not type(obj) is int:

                other_position = obj.position
                other_velocity = obj.velocity
                other_mass = obj.mass

                # change clamping factor + fix the merging issue

                Dx, Dy = other_position.x - self.position.x, other_position.y - self.position.y
                dist = np.sqrt(Dx**2 + Dy**2)
                clamping_dist = 300
            
                force = self.G*self.mass*other_mass/(dist**2 + clamping_dist**2)


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

        self.hierarchy_group = pg.sprite.Group()
        self.celestial_object_group = pg.sprite.Group()
        self.screen_cells_group = pg.sprite.Group()


        self.slice = 1
        self.screen_cells = np.array([[pg.rect.Rect(j*self.SCREEN.width/self.slice, i*self.SCREEN.height/self.slice, self.SCREEN.width/self.slice, self.SCREEN.height/self.slice) for j in range(self.slice)] for i in range(self.slice)])

        self.layer = Layer((0, 0, self.SCREEN.width, self.SCREEN.height), 1, [1], None, self.hierarchy_group)

 
        n = 4
        self.celestial_objects = []
        for i in range(n):
            object_x = randint(100, self.SCREEN.width-100)
            object_y = randint(50, self.SCREEN.height-50)
            mass = randint(50, 300)
            color = (randint(50, 200), randint(50, 200), randint(50, 200))
            

            self.celestial_objects.append((i, object_x, object_y, mass, (255, 255, 255), self.celestial_object_group))

        for obj in self.celestial_objects:
            self.celestial_object = CelestialObject(*obj)

    def run(self):
        while self.run_simulation:
            
            self.SCREEN.fill((10, 10, 25))
            dt = self.CLOCK.tick(self.FPS) / 100.0
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run_simulation = False

            self.layer.organize_hierarchy()

            for obj in self.celestial_object_group.sprites():
                obj.move([other_obj if other_obj.id != obj.id else 0 for other_obj in self.celestial_object_group.sprites()], dt)

            self.layer.check_sprites(self.celestial_object_group.sprites())
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