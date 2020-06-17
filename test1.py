from proton.matrices.operations import *
m = matrix([[1,2,3],[1,2,3],[1,2,3]])
m = elementary(m)
print( m["R1"] * m["R0"] )