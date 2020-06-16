from proton.matrices.matrix import *
from proton.matrices.decompose import decompose
m =[[1,2,3],[4,5,6],[7,8,10]]
l = matrix(m)
print("l now is " + str(l))
m[0][0] = 0
print(l)
print(decompose.LU(l))
print(l.det())