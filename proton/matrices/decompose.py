from proton.errors.errors import *
from proton.matrices.matrix import matrix
'''
File for contaning all the decomppositors
'''
class decompose():
	@staticmethod
	def pivot(M):
		"""Returns the pivoting matrix for M, used in Doolittle's method."""
		m = len(M)

	# Create an identity matrix, with floating point values                                                                                                                                                                                            
		id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]

	# Rearrange the identity matrix such that the largest element of                                                                                                                                                                                   
	# each column of M is placed on the diagonal of of M                                                                                                                                                                                               
		for j in range(m):
			row = max(range(j, m), key=lambda i: abs(M[i][j]))
			if j != row:
			# Swap the rows                                                                                                                                                                                                                            
				id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

		return matrix(id_mat)
	@staticmethod
	def LU(A):
		"""Performs an LU Decomposition of A (which must be square)                                                                                                                                                                                        
	into PA = LU. The function returns P, L and U."""
		n = len(A.pull())

	# Create zero matrices for L and U                                                                                                                                                                                                                 
		L = [[0.0] * n for i in range(n)]
		U = [[0.0] * n for i in range(n)]

	# Create the pivot matrix P and the multipled matrix PA                                                                                                                                                                                            
		P = decompose.pivot(A.pull())
		PA =(P*A).pull()

	# Perform the LU Decomposition
		try:                                                                                                                                                                                                                  
			for j in range(n):
			# All diagonal entries of L are set to unity                                                                                                                                                                                                   
				L[j][j] = 1.0

			# LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}                                                                                                                                                                                      
				for i in range(j+1):
					s1 = sum(U[k][j] * L[i][k] for k in range(i))
					U[i][j] = PA[i][j] - s1

			# LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )                                                                                                                                                                  
				for i in range(j, n):
					s2 = sum(U[k][j] * L[i][k] for k in range(j))
					L[i][j] = (PA[i][j] - s2) / U[j][j]
			return (matrix(L),matrix(U),P) 
		except ZeroDivisionError:
			raise ZeroDeterminantError(f"Cannot find LU deompostion of {A}")