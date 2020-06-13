from matrix import matrix
from errors.errors import *
'''
File for contaning all the decomppositors
'''
class decompose():
    '''
    Breaks a matrix into a upper and a lower triangular matrix.
    Returns a list of matrix as [UpperTrianglar , LowerTriangular, Pivotising]
    '''
    @staticmethod
    def LU(matr):
        if(type(matr) != matrix):
            raise OnlyMatrixIsAllowed(matr)
        
