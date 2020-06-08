from matrix import matrix
<<<<<<< HEAD
b = [[1,2,3],[1,2,3]]
b = matrix(b)
a = matrix([[1,2],[1,2],[1,2]])

c = matrix([[1,22,3] , [5, 17 , 19] , [9 , 10 ,50]])
d = matrix([[1,0,0] , [0,1,0] , [0,0,1]])

print(f"b*a : {b*a}")
print(f"a * 2.5 : {a*2.5}")
print(f"c*d : {c*d}")

atrans = a.transpose()
btrans = b.transpose()

print(f"a is {a} and its transpose is {atrans}")
print(f"b is {b} and its transpose is {btrans}")

=======
a = [[1,2,3],[1,2,3]]
a= matrix(a)
b = matrix([[1,2],[1,2],[1,2]])
print(b*a)
>>>>>>> lunchspider-branch
