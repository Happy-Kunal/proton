from proton.matrices.matrix import matrix
from proton.errors.errors import *
'''
File for contaning all the decomppositors
'''
class decompose():

    @staticmethod
    def pivotise(matr):
        if(type(matr) != matrix):
            raise OnlyMatrixAllowed(matr)
        if(matr.isSquare()==False):
            raise ValueError("Only square matrix can be fivoised" + f" {matr}" + " is not a square matrix.")
        ID = matrix.identity(len(matr.pull()[0])).pull()
        n = matr.getRowCount()
        for i in range(0,n):
            maxm = matr[i,i]
            row = i
            for j in range(i,n):
                if(matr[j,i] > maxm):
                    maxm = matr[j,i]
                    row = j
            
            if(i != row):
                tmp = ID[i]
                ID[i] = ID[row]
                ID[row] = tmp
        print(ID)
        return matrix(ID)
    '''
    Breaks a matrix into a upper and a lower triangular matrix.
    Returns a list of matrix as [UpperTrianglar , LowerTriangular, Pivotising]
    '''
    @staticmethod
    def LU(matr):
        if(type(matr) != matrix):
            raise OnlyMatrixAllowed(matr)
        if(matr.isSquare()==False):
            raise ValueError("Only square matrix can be fivoised" + f" {matr}" + " is not a square matrix.")
        pivot = decompose.pivotise(matr)
        n = matr.getRowCount()
        matr = (pivot * matr).pull()
        up = [[0] * n] * n
        down =[[0] * n] * n
        for j in range(0,n):
            down[j][j] = 1
            for i in range(0,j+1):
                s1 = 0
                for k in range(0,i):
                    s1+= up[k][j] * down[i][k]
                up[i][j] = matr[i][j] - s1
            for m in range(i,n):
                s2 = 0
                for l in range(0,j):
                    s2+= up[l][j] * down[m][l]
                down[m][j] = (matr[m][j] - s2) / up[j][j]
        return (matrix(down),matrix(up),pivot)
