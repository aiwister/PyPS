class Formula:
    def __init__(self):
        pass

    def Momentum(m, v):
        return m*v

    def KineticEnergy(m, v):
        return 0.5*m*(v*v)

    def PotentialEnergy(m, h):
        return m*9.8*h

    def Work(F, d):
        return F*d

    def Power(W, t):
        return W/t

    def Force(m, a):
        return m*a

    def Acceleration(F, m):
        return F/m

    def Velocity(d, t):
        return d/t

    def Distance(v, t):
        return v*t

    def Time(d, v):
        return d/v

    def Weight(m):
        return m*9.8

    def Density(m, v):
        return m/v

    def Pressure(F, A):
        return F/A

    def Area(l, w):
        return l*w

    def Volume(l, w, h):
        return l*w*h

    def Torque(F, d):
        return F*d

    def AngularVelocity(w, t):
        return w/t
