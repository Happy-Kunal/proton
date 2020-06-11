from proton.errors.IntFloatError import IntFloatError

from math import fsum

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
				matr+=[i]
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
		return self.__matrix[RowNumber-1]
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
			collist += [i[ColNumber-1]]
		return collist
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
		return self.__rows
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
		
		>>> a = matrix([[1,2,3] , [4,5,6] , [7,8,9]])
		>>> a.getOrderCount()
		3 * 3
		>>> c = matrix([[1 , 2 , 3] , [1,2,3]])
		>>> c.getOrderCount()
		2 * 3
		
	'''
	def getOrderCount(self):
		return self.__order
	
	'''
	IF USER WANTS HE/SHE CAN CHANGE ANY PARTICULAR VALUE OF
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
			raise TypeError(f"Cannot add {self} with {other}. Different datatypes.")
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
			raise TypeError(f"Cannot add {self} with {other}. Different datatypes.")
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
	
					for col in other.transpose() :
		
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
		

	'''
	Checks whether two matrix are equal or not.
	'''
	def __eq__(self, value):
		if(str(self) == str(value)):
			return True
		else:
			return False
			
	
	"""
	These methods symmMatrix() , skewsymmMatrix() performs task as
	per their names
	
	split() provides a tuple containing symmMatrix and skewsymmMatrix
	of a matrix in same order as written
	
	THESE ARE CURRENTLY UNDER CONSTRUCTION SO KINDLY DON'T USE THEM FOR NOW'
	
	"""
	
	def symmMatrix(self) :
		
		return (((self.__matrix) + (self.transpose())) * 0.5)
		
	def skewSymmMatrix(self) :
		
		return (((self.__matrix) - (self.transpose())) * 0.5)
		
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
		
			trans[i] = self.pullCol(i + 1)
		
		return trans
			
		
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
		
	
	
		
		
		
		
	
