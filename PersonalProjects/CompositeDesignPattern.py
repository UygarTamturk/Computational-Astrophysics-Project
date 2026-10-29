import numpy
import pygame as pg



class Hierarchy:
    def __init__(self, rect_value):

        self.rect_value = pg.Rect(*rect_value)

    def pull_rect(self):
        return self.rect_value

    def check_sprites(self, others):
        pass

class Sublayer(Hierarchy):
    def __init__(self, rect_value):
        super().__init__(rect_value)

        self.sprites = []    

class Layer(Hierarchy):
    def __init__(self, rect_value):
        super().__init__(rect_value)
        self.sublayers = []

    def add_sublayer(self, sublayers):
        for sublayer in sublayers:
            self.sublayers.append(sublayer)

    def remove_sublayer(self, sublayers):
        for sublayer in sublayers:
            if not sublayer in self.sublayers:
                continue

            self.sublayers.remove(sublayer)

    def split_layer(self):

        # dont forget to entegrate sprite inserting for sublayers
        x, y, w, h = self.rect_value
        new_sublayers = []

        for i in range(2):
            for j in range(2):
                nx = x/(j + 1)
                ny = y/(i + 1)
                nw = w/(j + 1)
                nh = h/(i + 1)

                sublayer = Sublayer((nx, ny, nw, nh))

                new_sublayers.append(sublayer)

        
        self.add_sublayer(new_sublayers)

    def get_sublayers(self):
        return self.sublayers




sprite_group = pg.sprite.Group()




sprites = [4, 2, 1, 4, 6]

# position calculated from topright to avoid division by zero
layer1 = Layer(pg.Rect(1540, 800, 1540, 800))
layer1.split_layer()
layer_1_sublayers = layer1.get_sublayers()

for sublayer in layer_1_sublayers:
    print(sublayer.pull_rect())
