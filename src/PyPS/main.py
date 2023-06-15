from weight import Weight
import sympy
a=sympy.Symbol("a")
o=Weight(1,[0,0],[1,1],[0,0])
print(o.fall(speed=[0,0],update_value=True,height=10))
print(o)
