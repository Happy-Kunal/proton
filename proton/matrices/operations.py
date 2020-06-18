from proton.errors.errors import *
import copy

class _element():
	def __init__(self,arg = []):
		self.arg = arg
	
	def __add__(self, value):
		if(type(value) == list):
			value = _element(value)
		if(len(self) != len(value)):
			raise ArithmeticError("Cannot add " + self + " with " + value + "order mismatch.")
		k = copy.deepcopy(self.arg)
		for i in range(len(self)):
			k[i]+= value.arg[i]
		return _element(k)


	def __mul__(self,value):
		if(type(value) == float or type(value) == int):
			k = copy.deepcopy(self.arg)
			for i in range(len(self)):
				k[i] *= value
			return _element(k)

		if(type(value) == _element):
			if(len(value) != len(self)):
				raise OrderMismatch("Cannot multiply " + self + " with " + value  + " order mismatch. ")
			k = copy.deepcopy(self.arg)
			for i in range(len(self)):
				k[i] *= value.arg[i]
			return _element(k)
		
		else:
			raise ArithmeticError("Cannot compute * of " + value + " with " + self)




	def __rmul__(self,value):
		if(type(value) == float or type(value) == int):
			k = copy.deepcopy(self.arg)
			for i in range(len(self)):
				k[i] *= value
			return _element(k)
		else:
			raise ArithmeticError("Cannot compute * of " + value + " with " + self)



	def __truediv__(self,value):
		if(type(value) == int or type(value) == float):
			k = copy.deepcopy(self.arg)
			for i in range(len(self.arg)):
				k[i] /= value
			return _element(k)
		
		if(type(value) == _element):
			k = copy.deepcopy(self.arg)
			for i in range(len(self.arg)):
				k[i] = k[i] / value.arg[i]
			return _element(k)
		

		else:
			raise ArithmeticError("Cannot compute / of " + value + " with " + self)

	
	def __rtruediv__(self,value):
		if(type(value) == int or type(value) == float):
			k = copy.deepcopy(self.arg)
			for i in range(len(self.arg)):
				k[i] = value/ k[i]
			return _element(k)
		
		else:
			raise ArithmeticError("Cannot compute / of " + value + " with " + self)



	def __floordiv__(self,value):
		if(type(value) == int or type(value) == float):
			k = copy.deepcopy(self.arg)
			for i in range(len(self.arg)):
				k[i] = k[i]// value
			return _element(k)
		
		if(type(value) == _element):
			k = copy.deepcopy(self.arg)
			for i in range(self.arg):
				k[i] = k[i] // value.arg[i]
			return _element(k)

		else:
			raise ArithmeticError("Cannot compute // of " + value + " with " + self)


	def __rfloordiv__(self,value):
		if(type(value) == int or type(value) == float):
			k = copy.deepcopy(self.arg)
			for i in range(len(self.arg)):
				k[i] = value// k[i]
			return _element(k)
		
		else:
			raise ArithmeticError("Cannot compute // of " + value +" with "  + self)

	def __pow__(self,value):
		if(type(value) == int or type(value) == float):
			k = copy.deepcopy(self.arg)
			for i in range(len(self.arg)):
				k[i] = k[i] ** value
			return _element(k)
		else:
			raise ArithmeticError("Cannot compute power for the " + value + " " + type(value) + " cannot be raised to power to " + self)
	
	def __str__(self):
		return str(self.arg)
	
	def __len__(self):
		return len(self.arg)


from proton.matrices.matrix import *
class elementary():
	'''
	elemntary class hanndles elementry operarions on a matrix obj.
	'''
	def __init__(self,matr):
		if(type(matr)==list):
			matr = matrix(matr)
		if(type(matr) != matrix):
			raise OnlyMatrixAllowed(matr)
		self.__matlist = copy.deepcopy(matr.pull())
		self.__numrow = matr.getRowCount()
		self.__numcol = matr.getRowCount()
	
	"""
	Returns a row or column of the parent matrix.
	usage:
	>>> from proton.matrices import *
	>>> m = matrix([[1,2,3],[1,2,3],[1,2,3]])
	>>> m = elementary(m)
	>>> m["r0"]
	<proton.matrices.operations._element object at 0x7f079bf46b80>
	>>> print(m["r0"])
	[1, 2, 3]
	>>> print(m["c0"])
	[1, 1, 1]
	"""

	def __getitem__(self,index = ""):
		index = index.capitalize()
		if(index[0] == 'C'):
			return self.__pullcol(int(index[1:len(index)]))
		if(index[0]=='R'):
			return self.__pullrow(int(index[1:len(index)]))
		else:
			raise OrderMismatch("Can only return column or a row.")
	

	"""
	Sets the row or the column of the parent matrix.
	usage :
	>>> from proton.matrices import *
	>>> m =  matrix([[1,2,3],[1,2,3],[1,2,3]])
	>>> m = elementary(m)
	>>> m["R1"] = m["r2"] + m['r1']
	>>> print(m['r1'])
	[2, 4, 6]
	"""

	def __setitem__(self,index="",value=[]):
		index = index.capitalize()
		if(index[0] == "C"):
			self.__pushcol(int(index[1:len(index)]),value)
		if(index[0]=='R'):
			self.__pushrow(int(index[1:len(index)]),value)
		else:
			raise OrderMismatch(f"Invalid {index} for {self}")


	"""
	Returns the row of the given index.
	"""

	def __pullrow(self,index):
		if(index>=self.__numrow or index <0):
			raise IndexError("Cannot find " + index +  " in " + self)
		return _element(copy.deepcopy(self.__matlist[index]))
	

	"""
	Returns the column of the given index.
	"""
	def __pullcol(self,index):
		if(index>=self.__numcol or index <0):
			raise IndexError("Cannot find " + index + " in " + self)
		m = [0 for k in range(self.__numcol)]
		for i in range(self.__numrow):
			m[i] = self.__matlist[i][index]
		return _element(m)
	
	def __pushcol(self,index,value=_element()):
		if(index>=self.__numcol or index <0):
			raise IndexError(f"Cannot find column {index} in {self}.")
		if(len(value)!= self.__numrow):
			raise IndexError(f"The index of {value} does not match that of {self}")

		for i in range(self.__numrow):
			self.__matlist[i][index] = value.arg[i]
	
	def __pushrow(self,index,value):
		if(index>=self.__numrow or index <0):
			raise IndexError(f"Cannot find row of {index} in {self}.")
		if(type(value) ==list):
			value = _element(value)
		if(len(value)!= self.__numcol):
			raise IndexError(f"The index of {value} does not match that of {self}")
		self.__matlist[index] = copy.deepcopy(value.arg)

	def __str__(self):
		return str(self.__matlist)