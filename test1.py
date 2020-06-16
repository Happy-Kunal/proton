from proton.matrices.operations import *
m = matrix([[1,2,3],[1,2,3],[1,2,3]])
m = elementary(m)
m["c1"] = [1,1,1]
print(m["c1"])