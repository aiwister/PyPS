import numpy as np
from formulas import *
from weight import Weight

class Circuler(Weight):
    def __init__(self):
        super().__init__(1,[0,0],[0,0],[0,0])
        self.acceleration_direction=np.array([0,0])
    
    def circuler_motion(self, angular_velocity:int, radius:int, update_value:bool=False):
        ...

    def __str__(self):
        return f"""Object(
    weight = "{str(self.m)}"
    position = "{str(self.p)}"
    velocity = "{str(self.v.tolist())}"
    acceleration = "{str(self.a)}"
    momentum = "{str(self.momentum)}"
    kinetic_energy = "{str(self.kinetic_energy)}"
    potential_energy = "{str(self.potential_energy)}"
    work = "{str(self.work)}"
    force = "{str(self.force)}"
)"""




