import math
import numpy as np
from formulas import *


class NeedTimeOrHeight(Exception):
    ...


class Weight:
    def __init__(self, weight, position=[0, 0], velocity=[0, 0], acceleration=0):
        self.m = weight
        self.p = np.array(position)
        self.direction = np.array(velocity)/math.sqrt(velocity[0]**2+velocity[1]**2)
        self.v = velocity
        self.a = acceleration
        self.momentum = Formula.Momentum(self.m, self.v)
        self.kinetic_energy = Formula.KineticEnergy(self.m, self.v)
        self.gravitational_potential_energy = Formula.GravitationalPotentialEnergy(
            self.m, self.p)
        self.work = Formula.Work(self.m, self.a)
        self.force = Formula.Force(self.m, self.a)

    def _update(self):
        self.m = self.m
        self.p = np.array(self.p)
        self.v = self.v
        self.a = self.a
        self.momentum = Formula.Momentum(self.m, self.v)
        self.kinetic_energy = Formula.KineticEnergy(self.m, self.v)
        self.gravitational_potential_energy = Formula.GravitationalPotentialEnergy(
            self.m, self.p)
        self.work = Formula.Work(self.m, self.a)
        self.force = Formula.Force(self.m, self.a)


    def free_fall(self, update_value=False, **kwargs):
        if "time" not in kwargs and "height" not in kwargs:
            raise NeedTimeOrHeight(
                "You need to specify either time or height") from None
        v = 9.8*kwargs["time"] if "time" in kwargs else math.sqrt(2*9.8*kwargs["height"]) if "height" in kwargs else 0
        if update_value:
            self.v=v
            self._update()
        return v

    def __str__(self):
        return f"""Object(
    weight="{str(self.m)}"
    position="{str(self.p)}"
    velocity="{str(self.v)}"
    acceleration="{str(self.a)}"
    momentum="{str(self.momentum)}"
    kinetic_energy="{str(self.kinetic_energy)}"
    gravitational_potential_energy="{str(self.gravitational_potential_energy)}"
    work="{str(self.work)}" 
    force="{str(self.force)}
)"""
