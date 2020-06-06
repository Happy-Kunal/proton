class matrix() :
	
	"""
	THIS CLASS HANDLES ALL THE OPERATIONS RELATED TO THE GENERATION OF A MATRIX
	SOON IT WILL BE INHERITED FROM ANOTHER CLASS OF NAME OPERATIONS SO THAT WE CAN
	PROVIDE THE BASIC OPERATIONS LIKE CONCATINATION , MATRIX MULTIPLICATION , SPLITING
	INTO A SYMMETRIC AND SKEW SYMMETRIC MATRIX ETC .
	"""
	
	"""
	CONSTRUCTOR OF CLASS TAKES INPUT LIKE NAME OF MATRIX , ORDER 
	AND IS MATRIX NULL OR NOT IF IT IS NOT NULL SO YOU HAVE TO PROVIDE 
	AN ITERABLE(MOST PROBABLY A LIST OR TUPLE) WHICH CAN BE USED TO 
	ENTER ELEMENTS IN THE MATRIX
	IF ONLY A ROW LIST OR A TUPLE IS GIVEN THE CONSTRUCTOR CREATE A COLUMN MATRIX OF THE GIVEN LENGHT
	"""
	def __init__(self , order = "" , null = False , iterable =()) :
		if(null==False):
			self.__row=0
			self.__col=0
			self.__order=0
			self.__matrix = self.__null_matrix()
		else:
			self.__row = len(iterable)
			self.__col = len(iterable[0])
			self.__order = __row * __col
			self.__matrix = self.__put_into_matrix(iterable)
	"""
	IF ON THE WAY AT ANY INSTANT IF YOU WANTS TO CHANGE THE WHOLE 
	MATRIX OR WANTS TO CHANGE THE INTIALY GENERATED MATRIX YOU CAN 
	USE THIS FUNCTION matrix_input() 
	"""
	def matrix_input(self) :
		
		self.InputList = []
		
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
	AN ITERABLE SO THIS FUNCTION __put_into_matrix() WILL RUN  , AFTER SOME TIME WE WILL GONNA 
	MAKE THIS FUNCTION USEABLE BY matrix_input() TOO
	"""		
	def __put_into_matrix(self , iterable) :
		
		__matrix = []
		
		for self.__x in iterable :
			
			if (len(self.__x) != self.__col) :
					
					 print(f"NUMBER OF ELEMENTS IN ONE ROW CAN ONLY BE  {self.__col} BUT YOU GAVE {len(self.__x)}")
					 __matrix = []
					 break
					 
			self.list = []
			for i in self.__x :
					
				self.__y = int(i)
				self.list += [self.__y]
					
			__matrix += [self.list]
			
		return __matrix
				
			
	
	"""
	THIS FUNCTION __null_matrix() WILL MAKE THE MATRIX AS NULL MATRIX 
	IT WILL BE USED BY CONSTRUCTOR AT INITIAL INSTANT
	"""
	
	def __null_matrix(self) :
		
		self.__matrix = []
		
		for i in range(self.__row) :
			
			self.__list = []
			
			for j in range(self.__col) :
				
				self.__list += [0]
				
			self.__matrix += [self.__list]
		return self.__matrix
	'''
	Returns a list containing the matrix
	'''
	def pullMatrix(self):
		return self.__matrix
	'''
	Returns the row of the given index.
	'''
	def pullRow(self,RowNumber):
		return self.__matrix[RowNumber-1]
	'''
	Returns the column at a the given index.
	'''
	def pullCol(self,ColNumber):
		collist = list()
		for i in self.__matrix:
			collist = [i[ColNumber-1]]
		return collist
	'''
	Returns the total numbber of rows in the matrix.
	'''
	def getRowCount(self):
		return self.__rows
	'''
	Returns the total number of columns iin the matrix.
	'''
	def getColCount(self):
		return self.__col
	'''
	Returns the order of the matrix.
	'''
	def getOrderCount(self):
		return self.__order
	
	"""
	This method converts the matrix object into string.
	"""
	def __str__(self):
		return str(self.__matrix)
	def __repr__(self):
		return str(self.__matrix)
	
	