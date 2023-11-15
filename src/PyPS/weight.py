import math
from typing import List
import numpy as np
from formulas import *


class NeedTimeOrHeight(Exception):
    ...


class Weight:
    def __init__(self, weight:int, position:list=[0, 0], velocity:list=[0, 0], acceleration:list=[0,0]):
        self.m = weight
        self.p = np.array(position)
        self.direction = np.array(velocity)/math.sqrt(velocity[0]**2+velocity[1]**2)
        self.v = np.array(velocity)
        self.velocity=math.sqrt(velocity[0]**2+velocity[1]**2)
        self.a = np.array(acceleration)
        self.momentum = Formula.Momentum(self.m, self.v)
        self.kinetic_energy = Formula.KineticEnergy(self.m, self.v)
        self.potential_energy = Formula.PotentialEnergy(
            self.m, self.p)
        self.work = Formula.Work(self.m, self.a)
        self.force = Formula.Force(self.m, self.a)

    def _vtovel(self, v:list):
        return math.sqrt(v[0]**2+v[1]**2)

    def _update(self):
        self.m = self.m
        self.p = np.array(self.p)
        self.v = self.v
        self.a = self.a
        self.momentum = Formula.Momentum(self.m, self.v)
        self.kinetic_energy = Formula.KineticEnergy(self.m, self.velocity)
        self.potential_energy = Formula.PotentialEnergy(
            self.m, self.p[1])
        self.work = Formula.Work(self.m, self.a)
        self.force = Formula.Force(self.m, self.a)


    def fall(self, speed:list=[0,0], update_value:bool=False, **kwargs):
        if "time" not in kwargs and "height" not in kwargs:
            raise NeedTimeOrHeight(
                "You need to specify either time or height") from None
        v = [0,9.8*kwargs["time"] if "time" in kwargs else math.sqrt(2*9.8*kwargs["height"]) if "height" in kwargs else 0]
        v+=np.array(speed)
        if update_value:
            self.v=v
            self.velocity=self._vtovel(v)
            self.a=[0,9.8]
            self._update()
        return v
    
    

    def __str__(self):
        return f"""Object(
    weight = "{str(self.m)}"
    position = "{str(self.p)}"
    velocity = "{str(self.v.tolist())}"
    acceleration = "{str(self.a)}"
    momentum = "{str(self.momentum.tolist())}"
    kinetic_energy = "{str(self.kinetic_energy)}"
    potential_energy = "{str(self.potential_energy)}"
    work = "{str(self.work)}" 
    force = "{str(self.force)}"
)"""
