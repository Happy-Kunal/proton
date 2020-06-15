from proton.matrices import matrix,decompose
l =matrix.matrix([[1,2,3],[4,5,6],[7,8,9]])
k = decompose.decompose.LU(l)
print(k)
