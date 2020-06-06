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
	"""
	def __init__(self , name , order = "1x1" , null = True , iterable =()) :
		
		self.name = name
		self.order = order
		self.rows = int(order.partition("x")[0])
		self.columns = int(order.partition("x")[2])
		
		if (null == True) :
			
			self.__matrix = self.__null_matrix()
			
		else :
			
			self.__matrix = self.__put_into_matrix(iterable)
		
	"""
	IF ON THE WAY AT ANY INSTANT IF YOU WANTS TO CHANGE THE WHOLE 
	MATRIX OR WANTS TO CHANGE THE INTIALY GENERATED MATRIX YOU CAN 
	USE THIS FUNCTION matrix_input() 
	"""
	def matrix_input(self) :
		
		self.InputList = []
		
		print("USE SPACES TO SEPRATE DIFFERENT ELEMENTS")
		
		for row in range(1 , self.rows + 1) :
				
				self.__x = input(f"ENTER THE ELEMENTS OF ROW {row} :")
				self.__x = self.__x.split(" " , self.columns)
				
				if (len(self.__x) != self.columns) :
					
					 print(f"NUMBER OF ELEMENTS IN ONE ROW CAN ONLY BE  {self.columns} BUT YOU GAVE {len(self.__x)}")
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
		
		for __x in iterable :
			
			if (len(__x) != self.columns) :
					
					 print(f"NUMBER OF ELEMENTS IN ONE ROW CAN ONLY BE  {self.columns} BUT YOU GAVE {len(__x)}")
					 __matrix = []
					 break
					 
			self.list = []
			for i in __x :
					
				self.__y = int(i)
				self.list += [self.__y]
					
			__matrix += [self.list]
			
		return __matrix
				
			
	"""
	THIS FUNCTION display() DISPLAYS THE MATRIX ON THE SCREEN IN A SPACIFIC 
	MANNER WITH ITS NAME
	"""	
	def display(self) :
		
		if (len(self.__matrix) > 0) :
				
			print(f"MATRIX {self.name} IS :")
			self.__str = ""
				
			for i in self.__matrix :
					
				self.__str += f"{i}\n"
			
			return self.__str
			
		else :
			
			print(f"NO CONTENT EXIST IN MARIX {self.name}")
	
	"""
	THIS FUNCTION __null_matrix() WILL MAKE THE MATRIX AS NULL MATRIX 
	IT WILL BE USED BY CONSTRUCTOR AT INITIAL INSTANT
	"""
	
	def __null_matrix(self) :
		
		self.__matrix = []
		
		for i in range(self.rows) :
			
			self.__list = []
			
			for j in range(self.columns) :
				
				self.__list += [0]
				
			self.__matrix += [self.__list]
			
		return self.__matrix
			

