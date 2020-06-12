from proton.errors.IntFloatError import IntFloatError

from math import fsum

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
	def __init__(self ,element = []) :
		
		self.__row = len(element)
		self.__col = len(element[0])
		self.__order = f"{self.__row} * {self.__col}"
		self.__matrix = self.__put_into_matrix(element)
	"""
	IF ON THE WAY AT ANY INSTANT IF YOU WANTS TO CHANGE THE WHOLE 
	MATRIX OR WANTS TO CHANGE THE INTIALY GENERATED MATRIX YOU CAN 
	USE THIS FUNCTION matrix_input() 
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
	AN ITERABLE SO THIS FUNCTION __put_into_matrix() WILL RUN  , AFTER SOME TIME WE WILL GONNA 
	MAKE THIS FUNCTION USEABLE BY matrix_input() TOO
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
	Returns a list containing the matrix
	'''
	def pull(self):
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
			collist += [i[ColNumber-1]]
		return collist
	'''
	Returns the value of the individual elements.
	'''
	def __getitem__(self , index = (0,0)) :
		
		return self.__matrix[index[0]][index[1]]
		
		
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
	
	'''
	
	'''
	
	def __setitem__(self , index = (0,0) , value =None) :
		
		if(isinstance(value,(int,float))==False):
			raise IntFloatError(value)
			
		else :
			self.__matrix[index[0]][index[1]] = value
		
		

	"""
	This method converts the matrix object into string.
	"""
	def __str__(self):
		return str(self.__matrix)
	
	def __repr__(self):
		return str(self.__matrix)
	'''
	Adds two or more matrices together.
	'''
	def __add__(self,other):
		if(type(other) != matrix):
			raise TypeError(f"Cannot add {self} with {other}. Different datatypes.")
		if(self.__order != other.__order):
			raise TypeError(f"Different order matrices : {self} and {other}")
		answer = other.__matrix
		for j in range(0,self.__row):
			for i in range(0,self.__col):
				answer[j][i] += self.__matrix[j][i]
		return matrix(answer)

	
	'''
	MULTIPLES TWO MATRICES OR MATRIX AND SCALER WITH EACH OTHER
	'''
	def __mul__(self,other):
	
		if (isinstance(other , matrix)) :
		
			if(self.__col != other.__row):
			
				raise ArithmeticError(f"Cannot muliply {self} with {other} . Clashing orders")
			
			else :
			
				answer = []
				
				for row in self.__matrix :
	
					list1 = []
	
					for col in other.transpose() :
		
						list1 += [fsum(matrix.__directmul(row , col))]
		
					answer += [list1]
	
				return matrix(answer)
		
			
		elif(isinstance(other , (int , float))) :
		
			answer = self.__matrix.copy()
		
			for i in range(0,self.__row):
				for j in range(0,self.__col):
					answer[i][j] *= other
				
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
		
	
			def issingle(self) :
	    result=str()
	    if self.__row==1 and self.__col==1 :
	        result=True
	    else :
	        result=False
	        
	    return result
	    
	def iscolumn(self) :
	    result=str()
	    if self.__row!=0 and self.__col==1 :
	        result=True
	    else :
	        result=False
	    
	    return result
	    
	def isrow(self) :
	    result=str()
	    if self.__row==1 and self.__col !=0 :
	        result=True
	    else :
	        result=False
	    
	    return result
	        	        	    
	def issquare(self) :
	    result=str()
	    if (self.__row==self.__col) :
	        result=True
	    else :
	        result=False
	        
	    return result
	
	def isalgebraic(self,other) :
	    if type(other)!=matrix :
	        print(f"{other} is NOT a MATRIX first.")
	    elif type(other)==matrix :
	        if self.__row==other.__row and self.__col==other.__col :
	            result=True
	        else :
	            result=False
	        return result
	    
	def issymmetric(self) :
	    result=str()
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        if self.transpose()==self :
	            result=True
	        else :
	            result=False
	    return result
	
	def diagonal(self) :
	    diaglist=list()
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        for i in range(self.__row) :
	            diaglist+=[self.__matrix[i][i]]
	            
	        return diaglist
	        
	def trace(self) :
	    tracenum=0
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        tracenum=fsum(self.diagonal())
	        
	    return tracenum
	    
	def negative(self) :
	    negat=matrix(self.transpose())	
	    for i in range(negat.__row) :
	        for j in range(negat.__col) :	            	            
	            negat.__matrix[i][j]=-negat.__matrix[i][j]
	    return negat.transpose()
	    
	def isnull(self) :
	    result=str()
	    matr=self.__matrix
	    for i in range(self.__row):
	        for j in range(self.__col):
	            if (matr[i][j]==0) :
	                result=True
	            else :
	                result=False
	                break
	    return result
	    
	def isskew(self) :
	    result=str()
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        if self.transpose()==self.negative() :
	            result=True
	        else :
	            result=False
	    return result
	    
	def isdiagonal(self) :	    
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        matr=self.transpose()
	        result=str()
	        for i in range(self.__row) :
	            for j in range(self.__col):
	                if j==i :
	                    continue
	                else :
	                    if matr[i][j]!=0 :
	                        result=False
	                        break
	                    else :
	                        result=True
	    return result
	    
	def isscalar(self) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    elif self.isdiagonal()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        result=str()
	        if self.trace()==self.__row*(int(self.__matrix[1][1])) :
	            result=True
	        else :
	            result=False
	            
	        return result
	        
	def isidentity(self) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    elif self.isdiagonal()==False :
	        print(f"{self}is not a DIAGONAL MATRIX first.")
	    else :
	        result=str()
	        if self.trace()==self.__row :
	            result=True
	        else :
	            result=False
	        return result	      
        
        def exponent(self,expn) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first .")
	    else :
	        if type(expn)==int :
	            result=matrix(self.__matrix.copy())
	            if expn==1 :
	                result=matrix(self.__matrix)
	            elif expn==0 :
	                result=self.__identity__()
	            else  :
	                for i in range(int(expn)-1) :
	                    result=result.__mul__(self)
	        else :
	            result=f"{expn} is Invalid Token for EXPONENT of Matrix."
	        return result
	def isidem(self) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        if (self.exponent(2).__matrix==self.__matrix) :
	            result=True
	        else :
	            result=False
	        return result
	
	def isinvoluntary(self) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")
	    else :
	        if (self.exponent(2).__matrix==self.__identity__()) :
	            result=True
	        else :
	            result=False
	        return result
	
	def isuppertri(self) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")	    
	    else :
	        for i in range(self.__row) :
	            for j in range(self.__col) :	                
	                if i>j :
	                    if self.__matrix[i][j]==0 :
	                        result=True
	                    else :
	                        result=False
	                        break
	                else :
	                    pass
	        return result
	
	def islowertri(self) :
	    if self.issquare()==False :
	        print(f"{self}is not a SQUARE MATRIX first.")	    
	    else :
	        for i in range(self.__row) :
	            for j in range(self.__col) :	                
	                if i<j :
	                    if self.__matrix[i][j]==0 :
	                        result=True
	                    else :
	                        result=False
	                        break
	                else :
	                    pass
	        return result
	
	def istriangular(self) :
	    if self.issquare()==False :
	        print(f"{self} is not a SQUARE MATRIX first.")
	    if self.isuppertri()==True or self.islowertri()==True :
	        result=True
	    else :
	        result=False
	
		
		
		
	
