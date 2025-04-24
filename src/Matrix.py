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
    def zoomIn(point, zoom_factor):
        x, y, z = point
        # Scale by zoom factor greater than 1 (e.g., 1.2)
        new_x = x * zoom_factor
        new_y = y * zoom_factor
        new_z = z * zoom_factor
        return (new_x, new_y, new_z)
    
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
    @staticmethod
    def shearY(point, angle):
        x, y, z = point
        shear_factor = math.tan(angle)
        new_y = y + shear_factor * x
        return (x, new_y, z)
    @staticmethod
    def shearZ(point, angle):
        x, y, z = point
        shear_factor = math.tan(angle)
        new_z = z + shear_factor * x
        return (x, y, new_z)
    
    
    @staticmethod
    def translate(point, dx:int = 0, dy:int = 0, dz:int = 0):
        x, y, z = point
        new_x = 0
        new_y = 0
        new_z = 0
        if dx != 0:
            new_x = x + dx
        else:
            new_x = x
        if dy != 0:
            new_y = y + dy
        else:
            new_y = y
        if dz != 0:
            new_z = z + dz
        else:
            new_z = z
        return (new_x, new_y, new_z)
    
    @staticmethod
    def mirror_x(point):
        point[1][1] = - point[1][1]
        point[2][2] = - point[2][2]
        return point