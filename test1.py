from proton.matrices.decompose import *
l = matrix([[1,3,5],[2,4,7],[1,1,0]])
k = decompose.LU(l)
print(k)
lo = k[0]
up = k[1]
print(lo * up)
print(k[2] * l)