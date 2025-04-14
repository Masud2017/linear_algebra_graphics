import math

class Matrix:
    
    @staticmethod
    def rotateX(point, angle):
        x, y, z = point
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_y = y * cos_theta - z * sin_theta
        new_z = y * sin_theta + z * cos_theta
        return (x, new_y, new_z)

    @staticmethod
    def rotateY(point, angle):
        x, y, z = point
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = x * cos_theta + z * sin_theta
        new_z = -x * sin_theta + z * cos_theta
        return (new_x, y, new_z)

    @staticmethod
    def rotateZ(point, angle):
        x, y, z = point
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = x * cos_theta - y * sin_theta
        new_y = x * sin_theta + y * cos_theta
        return (new_x, new_y, z)

    @staticmethod
    def zoomIn(point,angle):
        x, y, z = point
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = x * cos_theta - y * sin_theta
        new_y = x * sin_theta + y * cos_theta
        return (new_x, new_y, z)
    
    @staticmethod
    def zoomOut(point,angle):
        x, y, z = point
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = x * cos_theta + y * sin_theta
        new_y = -x * sin_theta + y * cos_theta
        return (new_x, new_y, z)
    
    @staticmethod
    def shearX(point, angle):
        x, y, z = point
        shear_factor = math.tan(angle)
        new_x = x + shear_factor * y
        return (new_x, y, z)