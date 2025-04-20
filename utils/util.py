from src.operations import operations
from src.Matrix import Matrix


def project(point, fov, viewer_distance, win_width = 800, win_height = 800):
    x, y, z = point
    factor = fov / (viewer_distance + z)
    x_proj = x * factor + win_width / 2
    y_proj = -y * factor + win_height / 2
    return (int(x_proj), int(y_proj))


def init_projection(projected_points:list,fov, viewer_distance, vertices)-> list:
    for vertex in vertices:
        projected_points.append(project(vertex,fov, viewer_distance))
        
    return projected_points

def apply_to_vertex(vertices,
                    fov,
                    viewer_distance,
                    angle = 0,
                    factor = 0,
                    projected_points:list = [],
                    screen_width = 800,
                    screen_height = 800,operation_type:operations = operations.TRANSLATE_X):
    projected_points = []
    for vertex in vertices:
        rotated = vertex
        
        match(operation_type):
            case operations.TRANSLATE_X:
                rotated = Matrix.translate(rotated, factor, 4,4)        
            case operations.TRANSLATE_Y:
                rotated = Matrix.translate(rotated,4,factor, 4)
            case operations.ROTATE_X:
                rotated = Matrix.rotateX(vertex, angle)
            case operations.ROTATE_Y:
                rotated = Matrix.rotateY(rotated, angle)
            case operations.ROTATE_Z:
                rotated = Matrix.rotateZ(rotated, angle)
            case operations.ZOOM:
                rotated = Matrix.zoomIn(rotated,factor)
            case operations.SHEAR_X:
                rotated = Matrix.shearX(rotated,factor)
        
            
        
        # Project the 3D point to 2D screen coordinates
        projected = project(point = rotated, win_width = screen_width, win_height= screen_height, fov= fov, viewer_distance=viewer_distance)
        projected_points.append(projected)
    return projected_points