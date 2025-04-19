from src.operations import operations
from src.Matrix import Matrix


def project(point, win_width, win_height, fov, viewer_distance):
    x, y, z = point
    factor = fov / (viewer_distance + z)
    x_proj = x * factor + win_width / 2
    y_proj = -y * factor + win_height / 2
    return (int(x_proj), int(y_proj))

def apply_to_vertex(vertices,
                    fov,
                    viewer_distance,
                    angle = 0,
                    factor = 0,
                    projected_points:list = [],
                    screen_width = 800,
                    screen_height = 800):
    
    for vertex in vertices:
        # Apply rotations
        rotated = vertex
        if play_auto:
            rotated = Matrix.rotateX(vertex, angle)
            rotated = Matrix.rotateY(rotated, angle)
            rotated = Matrix.rotateZ(rotated, angle)
            # rotated = Matrix.zoomIn(rotated, zoom_in_and_out_slider.getValue())
            rotated = Matrix.shearX(rotated,factor)
            rotated = Matrix.zoomIn(rotated,factor)
            rotated = Matrix.translate(rotated, factor, 4,4)
            rotated = Matrix.translate(rotated,4,factor, 4)
            
            
        
        # Project the 3D point to 2D screen coordinates
        projected = project(rotated, screen_width, screen_height, fov, viewer_distance)
        projected_points.append(projected)
        
    return projected_points