from proton.matrices.decompose import *

def det(A) :
	
	try :
		
		U = decompose.LU(A)[1]
		diagonal = U.getdiagonal()
		detr = -1
		for i in diagonal :
		
			detr *= i
		
		return detr
	
	except ZeroDivisionError :
		
		return 0

