from proton.matrices.operations import *
m = matrix([[1,2,3],[1,2,3],[1,2,3]])
m = elementary(m)
print(3// m["R1"])