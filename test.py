from proton.matrices import matrix
""" a = matrix.nullMatrix(order = (3,3))

b = matrix([[1,2,3],[4,5,6] ,[7,8,9]])

c = matrix.diagonalMatrix([1,2,3])
d = matrix.diagonalMatrix([2,4,6,8,10])
e = matrix.diagonalMatrix([1])

f = matrix.scalarMatrix(5 , order = 3)

i = matrix.identity(3)

print(a)
print(b)
print(b[1,1]) #expected result should be 5

b[1 , 1] = 400

print(b)

print(f"diagonal matrix \"c\" : {c}")
print(f"diagonal matrix \"d\" : {d}")
print(f"diagonal matrix \"e\" : {e}")

print()
print(f"scalar matrix \"f\" : {f}")

print()
print(f"identity matrix \"i\" : {i}")


print(b)
print(b*(-1))
print(b)



j = matrix([[1,2],[1,2]])
k = matrix([[1,2,3],[1,2,3]])
print(f"j*k : {j*k")
print(f"j*2 : {j*2}")

"""


l = matrix([[1,2 ,5],[1,2 ,5]])
m = matrix([[1,2,3] , [4,5,6]])


print(f"l : {l}")
print(f"m : {m}")
print(f"l - m : {l-m}")
print(f"l + m : {l+m}")
print(f"l : {l}")
print(f"m : {m}")
print(f"l transpose : {l.transpose()}")
print(f"now , l is : {l}")
l = matrix([[1,2],[1,2]])
print(f"{l**2}")
l = matrix([[2,1]])
l.rowSort()
print(l)
l.pushRow([[1,2]])
print(l)
l = matrix.columnMatrix([[1,2,3]])
print(l)
# print(f"l.split() : {l.split()}")