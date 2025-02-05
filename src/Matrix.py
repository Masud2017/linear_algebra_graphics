import numpy as np

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

    