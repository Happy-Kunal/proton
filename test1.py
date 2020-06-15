from proton.matrices.decompose import *
from proton.linalge.det import det

l = matrix([[1,3,5],[2,4,7],[1,1,0]])
m = matrix([[1,2,3],[4,5,6],[7,8,9]])



print(f"l = {l}")
print(f"det(l) = {det(l)}")

print(f"m = {m}")
print(f"det(m) = {det(m)}")
