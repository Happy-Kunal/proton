from proton.matrices.matrix import *
from proton.errors.errors import *
class elementary():
	'''
	elemntary class hanndles elementry operarions on a matrix obj.
	'''
	def __init__(self,m):
		if(type(m)==list):
			m = matrix(m)
		if(type(m) != matrix):
			raise OnlyMatrixAllowed(m)
		self.matrixobj = m
	