from proton.matrices.operations import *
m = matrix([[1,2,3],[1,2,3],[1,2,3]])
m = elementary(m)
m["R2"] = m["R0"] + m["R1"]
print(m)