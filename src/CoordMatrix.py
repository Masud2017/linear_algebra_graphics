import numpy as np

'''
<h1>CoordMatrix</h1>
This class represents a matrix (physical form) aka matrix defination.
It is capable of performing some regular operations like shearing, rotation, mirroring and scaling and transposition.
'''
class CoordMatrix:
    def __init__(self, shape = (50,50,50), x_range = 50, y_range = 50, z_range = 50 ,value_to_character_mapper:dict = {}):
        self.matrix = np.zeros(shape)
        self.x_range = x_range
        self.y_range = y_range
        
        print(f"Printign the value of the matrix")
        print(self.matrix)
        
    def __eq__(self, value):
        return self.matrix == value.matrix


    def get_transpose(self):
        return self.matrix.T
    def get_inverse(self):
        return np.linalg.inv(self.matrix)
    def get_determinant(self):
        return np.linalg.det(self.matrix)

    
if __name__ == "__main__":
    matrix = CoordMatrix()
    