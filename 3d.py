import sympy as sp
A=sp.Point(0,5)
B=sp.Point(7,2)
len_AB=A.distance(B)
print(f" length of AB ,[len_AB] ")

mid_AB=A.midpoint(B)
print(f" midpoint of AB ,[mid_AB]")
