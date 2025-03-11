import numpy as np

'''
<h1>Matrix</h1>
This class is responsible for handling matrix operations.
'''
class Matrix:
    def __init__(self, shape = (150,150)):
        self.matrix = np.zeros(shape)
        
    def __eq__(self, value):
        return self.matrix == value.matrix
    
    def __add__(self, value):
        return self.matrix + value.matrix
    def __sub__(self, value):
        return self.matrix - value.matrix
    def __mul__(self, value):
        return self.matrix * value.matrix
    def get_transpose(self):
        return self.matrix.T
    def get_inverse(self):
        return np.linalg.inv(self.matrix)
    def get_determinant(self):
        return np.linalg.det(self.matrix)

    