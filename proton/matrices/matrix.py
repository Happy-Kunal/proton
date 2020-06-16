from proton.errors.errors import *
from math import fsum
import copy
# WHERE EVER YOU FOUND BUG WITH ITS ID , NEVER CUT THOSE LINE
# FOR MORE INFO VISIT BUG_INFO.txt


class matrix() :
	
	"""
	CONSTRUCTOR OF CLASS TAKES AN ITERABLE(MOST PROBABLY A LIST OR TUPLE) AS INPUT WHICH CAN BE USED TO ENTER ELEMENTS IN THE MATRIX LIKE :
		
		>>> x = [[1,2,3] , [4,5,6] , [7,8,9]]
		>>> a = matrix(x)
		>>> b = matrix(x)
		>>>print(b)
		
		[[1,2,3] , [4,5,6] , [7,8,9]]
		
		>>> type(b)
		
		class proton.matrices.matrix.matrix
	
	"""
	def __init__(self ,element = []) :
		
		self.__row = len(element)
		self.__col = len(element[0])
		self.__order = f"{self.__row} * {self.__col}"
		self.__matrix = self.__put_into_matrix(element)
		
	"""
	IF ON THE WAY AT ANY INSTANT IF YOU WANTS TO CHANGE THE WHOLE 
	MATRIX OR WANTS TO CHANGE THE INTIALY GENERATED MATRIX YOU CAN 
	USE THIS FUNCTION matrix_input() AS :
		
		>>> b = b.matrix_input()
		USE SPACES TO SEPRATE DIFFERENT ELEMENTS
		ENTER THE ELEMENTS OF ROW 1 :1 0 0
		ENTER THE ELEMENTS OF ROW 2 :0 1 0
		ENTER THE ELEMENTS OF ROW 3 :0 0 1
		
		>>> print(b)
		
		[[1,2,3] , [4,5,6] , [7,8,9]]
	
	
	"""
	def matrix_input(self) :
		
		print("USE SPACES TO SEPRATE DIFFERENT ELEMENTS")
		
		for row in range(1 , self.__row + 1) :
				
				self.__x = input(f"ENTER THE ELEMENTS OF ROW {row} :")
				self.__x = self.__x.split(" " , self.__col)
				
				if (len(self.__x) != self.__col) :
					
					print(f"NUMBER OF ELEMENTS IN ONE ROW CAN ONLY BE  {self.__col} BUT YOU GAVE {len(self.__x)}")
					self.__matrix = []
					break
					 
				self.list = []
				for i in self.__x :
					
					self.__y = int(i)
					self.list += [self.__y]
					
				self.__matrix += [self.list]
		
	"""
	IF USER DOES NOT WANTS THE INITIAL NULL MATRIX AND INSTEAD PROVIDED 
	AN ITERABLE SO THIS FUNCTION __put_into_matrix() WILL RUN
	"""		
	def __put_into_matrix(self , iterable) :
		
		matr = []
		for i in iterable:
			if(len(i) != self.__col):
				raise TypeError(f"Cannot make {iterable} a matrix.")
			else:
				for value in i:
					if(isinstance(value,(int,float))== False):
						raise IntFloatError(value)
				matr+=[copy.deepcopy(i)]
		return matr
				
			
	'''
	pull() Returns a list containing the matrix
	
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.pull()
	
		[[1,2,3] , [4,5,6] , [7,8,9]]
	
		>>> b.pull()
	
		[[1,0,0] , [0,1,0] , [0,0,1]]
	
	'''
	def pull(self):
		return self.__matrix
	'''
	pullRow() Returns the row of the given index. AS :
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.pullRow(1)
		[1,2,3]
		>>> a.pullRow(2)
		[4,5,6]
		>>>a.pullRow(3)
		[7,8,9]
	
	
	'''
	def pullRow(self,RowNumber):
		return self.__matrix[RowNumber]
	'''
	pullCol() Returns the column at a the given index. AS :
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.pullCol(1)
		[1,4,7]
		>>> a.pullCol(2)
		[2,5,8]
		>>> a.pullCol(3)
		[3,6,9]
		
	'''
	def pullCol(self,ColNumber):
		collist = list()
		for i in self.__matrix:
			collist += [i[ColNumber]]
		return collist
	
	def pushRow(self,Row):
		self.pushRowAt(Row,self.__row)
	'''
	ADDS ROWS AFTER THE GIVEN POSTION.
	'''
	def pushRowAt(self,Row,Pos):
		if(type(Row) != list and type(Row) != matrix):
			raise OnlyMatrixAllowed(Row)
		if(type(Row)== list):
			Row = matrix(Row)
		if(Row.__col != self.__col):
			raise OrderMismatch(Row + f" cannot be added to {self}")
		matr = self.__matrix[0:Pos]
		for i in range(0,Row.__row):
			matr +=[Row.__matrix[i]]
		self.__row += Row.__row
		matr += self.__matrix[Pos+Row.__row:self.__row ]
		self.__matrix = matr


	def pushColAt(self,Col,Pos):
		if(type(Col) != list and type(Col) != matrix):
			raise OnlyMatrixAllowed(Col)
		if(type(Col)== list):
			Col = matrix.columnMatrix(Col)
		if(Col.__col != self.__col):
			raise OrderMismatch(Col + f" cannot be added to {self}")
		k = 0
		self.__row +=Col.__row
		matr = [[0] * self.__col] * self.__row
	'''
	To get the value of the individual element. As :
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a[0,0]
		1
		>>> a[0,1]
		2
		>>> a[1,2]
		4
		
	'''
	def __getitem__(self , index = (0,0)) :
		
		return self.__matrix[index[0]][index[1]]
		
		
	'''
	getRowCount() Returns the total number of rows in the matrix. As :
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.getRowCount()
		3
		>>> c = matrix([[1 , 2 , 3] , [1,2,3]])
		>>> c.getRowCount()
		2
		
		
	'''
	def getRowCount(self):
		return self.__row
	'''
	getColCount() Returns the total number of columns iin the matrix. As :
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.getColCount()
		3
		>>> c = matrix([[1 , 2 , 3] , [1,2,3]])
		>>> c.getColCount()
		3
		
		
	'''
	def getColCount(self):
		return self.__col
	'''
	getOrderCount() Returns the order of the matrix. As :
		def colSort(self):
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.getOrderCount()
		3 * 3
		>>> c = matrix([[1 , 2 , 3] , [1,2,3]])
		>>> c.getOrderCount()
		2 * 3
		
	'''
	def getOrderCount(self):
		return self.__order
	
	"""
	diagonal related operations by vikas
	"""
	def getdiagonal(self) :
		diaglist=list()
		if self.isSquare()==False :
			raise TypeError(f"{self} is not a square matrix")
		else :
			for i in range(self.__row) :
				diaglist+=[self.__matrix[i][i]]
				
			return diaglist
	
	def getdiagonalsum(self) :
		
		sum = 0
		if self.isSquare()==False :
			raise TypeError(f"{self} is not a square matrix")
		else :
			for i in range(self.__row) :
				sum += self.__matrix[i][i]
				
			return sum

	
	
	'''
	IF USER WANTS THEY CAN CHANGE ANY PARTICULAR VALUE OF
	ELEMENT OF MATRIX AS :
	
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		
		>>> a[0,0]
		1
		>>> a[0,0] = 400
		>>> a
		[[400,2,3] , [4,5,6] , [7,8,9]]
		
		>>> a[0,1]
		2
		>>> a[0,1] = 50
		[[400,50,3] , [4,5,6] , [7,8,9]]
		
		>>> a[1,2]
		4
		>>> a[1,2] = 100
		[[400 , 50 ,3] , [100 ,5,6] , [7,8,9]]
	
	'''
	
	def __setitem__(self , index = (0,0) , value = None) :
		
		if(isinstance(value,(int,float))==False):
			raise IntFloatError(value)
			
		else :
			self.__matrix[index[0]][index[1]] = value
		
		

	"""
	These methods converts the matrix object into string.
	
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> str(a)
		"[[1,2,3] , [4,5,6] , [7,8,9]]"
		
	"""
	def __str__(self):
		return str(self.__matrix)
	
	def __repr__(self):
		return str(self.__matrix)
		
	"""
	==================================================
	BASIC ARITHMATIC OPERATIONS ON MATRICES
	==================================================
	"""
	
	
	'''
	Adds two or more matrices together.
	
		>>> a = matrix([[1,2],[1,2]])
		>>> b = matrix([[2,4],[2,4]])
		>>> a + b
		[[3,4] , [3,4]]
	
	
	'''
	def __add__(self , other) :
	
		if(type(other) != matrix):
			raise OnlyMatrixAllowed(other)
		if(self.__order != other.__order):
			raise TypeError(f"Different order matrices : {self} and {other}")
	
		answer = self.__matrix.copy() # this is done to solve bug b001
	
		for i in range(other.__row) :
			list1 = answer[i].copy() # this is done to solve bug b001
		
			for j in range(other.__col) :
			
				list1[j] += other.__matrix[i][j]
			
			answer[i] = list1
		
		return matrix(answer)
		
	"""
	Subtracts two or more matrices .
	
		>>> a = matrix([[1,2],[1,2]])
		>>> b = matrix([[2,4],[2,4]])
		>>> a - b
		[[-1,-2] , [-1,-2]]
		
	"""	
	def __sub__(self , other) :
	
		if(type(other) != matrix):
			raise OnlyMatrixAllowed(other)
		if(self.__order != other.__order):
			raise TypeError(f"Different order matrices : {self} and {other}")
	
		answer = self.__matrix.copy() # this is done to solve bug b001
	
		for i in range(other.__row) :
			list1 = answer[i].copy() # this is done to solve bug b001
		
			for j in range(other.__col) :
			
				list1[j] -= other.__matrix[i][j]
			
			answer[i] = list1
		
		return matrix(answer)

	
	'''
	MULTIPLES TWO MATRICES OR MATRIX AND SCALER WITH EACH OTHER
	
		>>> a = matrix([[1,2],[1,2]])
		>>> b = matrix([[1,2,3],[1,2,3]])
		>>> a*b
		[[3.0, 6.0, 9.0], [3.0, 6.0, 9.0]]
		
		>>> a * 2
		[[2, 4], [2, 4]]
	
	
	'''
	def __mul__(self,other):
	
		if (isinstance(other , matrix)) :
		
			if(self.__col != other.__row):
			
				raise ArithmeticError(f"Cannot muliply {self} with {other} . Clashing orders")
			
			else :
			
				answer = []
				
				for row in self.__matrix :
	
					list1 = [] # this is done to solve bug b001
	
					for col in other.transpose().__matrix :
		
						list1 += [fsum(matrix.__directmul(row , col))] # this is done to solve bug b001
		
					answer += [list1]
	
				return matrix(answer)
		
			
		elif(isinstance(other , (int , float))) :
		
			answer = self.__matrix.copy()
		
			for i in range(0,self.__row):
				
				list1 = answer[i].copy()
				for j in range(0,self.__col):
					list1[j] *= other
					
				answer[i] = list1
				
			return matrix(answer)
		
		else :
		
			raise TypeError(f"Cannot multiply {self} with {other} . Operation On Unsupported Datatypes.")		
		
	
	def __pow__(self , power) :
		
		if (power != int(power)) :
			
			 raise TypeError(f"{power} is not an integer .\nonly whole numbers are allowed") 
		
		elif self.isSquare() == False :
			
			raise TypeError(f"{self} is not a square matrix . \nonly square matrices are allowed")
				
		else :
			
			return matrix.powermatrix(self , power)
			
			
	
	'''
	Checks whether two matrix are equal or not.
	'''
	def __eq__(self, value):
		if(str(self) == str(value)):
			return True
		else:
			return False
	'''
	Sorts a matrix in rows position
	'''
	def rowSort(self):
		for i in range(0,self.__row):
			self.__matrix[i].sort()

	@staticmethod
	def powermatrix(matr , power ) :
				
				if power == 0 :
				
					return matrix.identity(matr.getRowCount())
					
				else :
					
					mul = matr
					for i in range(1,power):
						mul *= matr
					return mul
			
	
	"""
	These methods symmMatrix() , skewsymmMatrix() performs task as
	per their names
	
	split() provides a tuple containing symmMatrix and skewsymmMatrix
	of a matrix in same order as written
	
	
	"""
	
	def symmMatrix(self) :
		
		return ((self + self.transpose()) * 0.5)
		
	def skewSymmMatrix(self) :
		
		return ((self - self.transpose()) * 0.5)
		
	def split(self) :
		
		return (self.symmMatrix() , self.skewSymmMatrix())
	
	'''
	Muliply some scalar value with each element of the matrix.
	'''
	def scalarMul(self,value):
		for i in range(0,self.__row):
			for j in range(0,self.__col):
				self.__matrix[i][j] *= value

	
	def rightscalarDiv(self,value):
		for i in range(0,self.__row):
			for j in range(0,self.__col):
				self.__matrix[i][j] = self.__matrix[i][j] / value
	
	def leftscalarDiv(self,value):
		for i in range(0,self.__row):
			for j in range(0,self.__col):
				self.__matrix[i][j] = value/self.__matrix[i][j]
	
	
	"""
	transpose() returns the transpose of a matrix
	"""
	
	def transpose(self) :
	
		trans = [[0] * self.__row] * self.__col
	
		for i in range(self.__col) :
		
			trans[i] = self.pullCol(i)
		
		return matrix(trans)
			
		
	@staticmethod
	def __directmul(list1 , list2) :
	
		list3 = []
	
		for i in range(len(list1)) :
		
			list3 += [list1[i] * list2[i]]
		
		return list3	
			
	
	"""
	==================================================
	SOME ALTERNATIVE CONSTRUCTORS
	==================================================
	"""
	
	@classmethod
	def nullMatrix(cls , order = (1,1)) :
		
		__row = order[0]
		__col = order[1]
		
		__matrix = [[0] * __col] * __row
		
		return matrix(__matrix)
	
	@classmethod
	def diagonalMatrix(cls , diagonalElements = (0 ,)) :
		
		__k = len(diagonalElements)
		__matr = [[0] * __k] * __k
		
		for i in range(__k) :
			
			list1 = __matr[i].copy()
			
			list1[i] = diagonalElements[i]
			
			__matr[i] = list1
			
		return matrix(__matr)
		
		
	@classmethod
	def scalarMatrix(cls , element , order = 1) :
			
		return cls.diagonalMatrix((element ,)*order)
		
	@classmethod
	def identity(cls , order = 1) :
		
		return cls.scalarMatrix(element = 1 , order = order)
		
	@classmethod
	def columnMatrix(cls,column):
		return matrix.transpose(matrix(column))
	
	
	"""
	SOME BOOLEAN METHODS
	"""
		
	def isSingle(self) :
		
		if self.__row==1 and self.__col==1 :
			return True
			
		return False
			

	def isColumn(self) :
		
		if self.__row!=0 and self.__col==1 :
			return True
		return False
			
				
	def isRow(self) :
		
		if self.__row==1 and self.__col !=0 :
			return True
			
		return False
		
	def isSquare(self) :
		
		if (self.__row==self.__col) :
			return True
		return False
			
		
	def isAdditive(self , other) :
		
		if type(other)!=matrix :
			return False
		
		elif ((self.__row == other.__row) and (self.__col == other.__col)) :
			
			return True
		
		return False			
	
	def isSymmetric(self) :
		
		if self.transpose()==self :
			return True
		
		return False

			
	def isNull(self) :
		
		if self == matrix.nullMatrix(self.__row) :
			
			return True
			
		return False
		
	
	def isSkew(self) :
		
		if self.isSquare()==False :
			return False
		
		elif self.transpose()==(self * (-1)) :
			return True
			
		return False
		
	def isDiagonal(self) :
		
		if self.isSquare()==False :
			return False
		
		else :
			
			for i in range(self.__row) :
				for j in range(self.__col) :
					
					if i == j :
						continue
						
					elif self[i,j] != 0 :
						
						return False
						
			return True
	
	def isScalar(self) :
		
		if self.isdiagonal() :
			
			a11 = self[0,0]
			
			for i in range(1 , self.__row) :
				
				if self[i , i] != a11 :
					return False
					
			return True
			
	def isIdentity(self) :
		
		if self == matrix.identity(self.__row) :
			
			return True
			
		return False
	
	def isUpperTri(self) :
		if self.isSquare()==False :
			print(f"{self}is not a SQUARE MATRIX first.")		
		else :
			for i in range(self.__row) :
				for j in range(self.__col) :					
					if i>j :
						if self.__matrix[i][j]==0 :
							return True
						else :
							return False
							break
					else :
						pass
			
	
	def isLowerTri(self) :
		if self.isSquare()==False :
			print(f"{self}is not a SQUARE MATRIX first.")		
		else :
			for i in range(self.__row) :
				for j in range(self.__col) :					
					if i<j :
						if self.__matrix[i][j]==0 :
							return True
						else :
							return False
							break
					else :
						pass
			
	
	def isTriangular(self) :
		if self.isSquare()==False :
			print(f"{self} is not a SQUARE MATRIX first.")
		if self.isuppertri()==True or self.islowertri()==True :
			return True
		return False
	
	def det(self):
		if(self.isSquare==False):
			raise ArithmeticError(f"Cannot find determinant of {self} . This is not a square matrix.")
		try:
			from .decompose import decompose
			m = (decompose.LU(self)[1]).pull()
			Det = -1.0
			for i in range(self.__row):
				Det *= m[i][i]
			del decompose
			return Det
		except ZeroDeterminantError:
			del decompose
			return 0.0