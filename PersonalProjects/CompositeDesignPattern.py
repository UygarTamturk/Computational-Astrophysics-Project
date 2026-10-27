import numpy



class Hierarchy:
    def __init__(self):
        pass


class Layer(Hierarchy):
    def __init__(self, index):
        super().__init__()
        self.rect_value = [0, 0, 1540, 800]

        self.layer_index = index
        self.sublayers = [0]