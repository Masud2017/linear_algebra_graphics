def apply_to_vertex(vertices, angle):
    for vertex in vertices:
        # Apply rotations
        rotated = vertex
        if play_auto:
            rotated = Matrix.rotateX(vertex, angle)
            rotated = Matrix.rotateY(rotated, angle)
            rotated = Matrix.rotateZ(rotated, angle)
            # rotated = Matrix.zoomIn(rotated, zoom_in_and_out_slider.getValue())
            rotated = Matrix.shearX(rotated,shear_slider.getValue())
            rotated = Matrix.zoomIn(rotated,zoom_in_and_out_slider.getValue())
            rotated = Matrix.translate(rotated, translate_x_slider.getValue(), 4,4)
            rotated = Matrix.translate(rotated,4,translate_y_slider.getValue(), 4)
            print(f"VAlue of hte slider is : {shear_slider.getValue()}")
            
            
        
        # Project the 3D point to 2D screen coordinates
        projected = project(rotated, screen_width, screen_height, fov, viewer_distance)
        projected_points.append(projected)