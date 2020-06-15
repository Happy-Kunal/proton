from proton.matrices.decompose import *
m =[[1,2,3],[4,5,6],[7,8,9]]
l = matrix(m)
print("l now is " + str(l))
m[0][0] = 0
print(l)
