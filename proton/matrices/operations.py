from proton.matrices.matrix import *
from proton.errors.errors import *
import copy
class elementary():
	'''
	elemntary class hanndles elementry operarions on a matrix obj.
	'''
	def __init__(self,m):
		if(type(m)==list):
			m = matrix(m)
		if(type(m) != matrix):
			raise OnlyMatrixAllowed(m)
		self.__matlist = copy.deepcopy(m.pull())
		self.__numrow = m.getRowCount()
		self.__numcol = m.getRowCount()
	
	def __getitem__(self,index = ""):
		index = index.capitalize()
		if(index[0] == 'C'):
			pass
		if(index[0]=='R'):
			pass
		else:
			raise OrderMismatch("Can only return column or a row.")