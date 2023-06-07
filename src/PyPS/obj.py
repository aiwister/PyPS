import math
import numpy as np
from formulas import *

class Weight:
    def __init__(self,weight,position=[0,0],velocity=[0,0],acceleration=0):
        self.m=weight
        self.p=np.array(position)
        self.v=np.array(velocity)/math.sqrt(velocity[0]**2+velocity[1]**2)
        self.a=acceleration
        self.momentum=Formula.Momentum(self.m,self.v)
        self.kinetic_energy=Formula.KineticEnergy(self.m,self.v)
        self.gravitational_potential_energy=Formula.GravitationalPotentialEnergy(self.m,self.p)
        self.work=Formula.Work(self.m,self.a)
        self.force=Formula.Force(self.m,self.a)
    
    def __str__(self):
        return "Object(\n  weight="+str(self.m)+"\n  position="+str(self.p)+"\n  velocity="+str(self.v)+"\n  acceleration="+str(self.a)+"\n  momentum="+str(self.momentum)+"\n  kinetic_energy="+str(self.kinetic_energy)+"\n  gravitational_potential_energy="+str(self.gravitational_potential_energy)+"\n  work="+str(self.work)+"\n  force="+str(self.force)+"\n)"
    
