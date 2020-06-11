from proton.matrices import matrix
a = matrix.nullMatrix(order = (3,3))

b = matrix([[1,2,3],[4,5,6] ,[7,8,9]])

c = matrix.diagonalMatrix([1,2,3])
d = matrix.diagonalMatrix([2,4,6,8,10])
e = matrix.diagonalMatrix([1])

f = matrix.scalarMatrix(5 , order = 3)

i = matrix.identity(3)

print(a)
print(b)


Print(a.isnull()) # Print True/a is a null matrix.

Print(b.diagonal()) # Print diagonal elements of b matrix.

Print(b.trace()) # Print Trace of Matrix b.

Print(b.exponent(2)) # Print b matrix raised to power 2.

Print(b.negative()) # print negative of Matrix b.

Print(d.issquare()) # print False/d is not a square matrix.

Print(d.isrow()) # Print True/d is a row matrix.


