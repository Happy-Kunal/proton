from matrix import matrix
a = [[1,2,3],[1,2,3]]
b = matrix(a)
a = matrix(a)
a+=b + b + a
print(a)