import pygame
import sys
from  src.Matrix import Matrix
from pygame_widgets.button import Button
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Linear Algebra graphics project")
clock = pygame.time.Clock()

# constants
play_auto = False

def start_auto():
    global play_auto
    play_auto = True
def stop_auto():
    global play_auto
    play_auto = False
play_auto_button = None
if play_auto:
    play_auto_button = Button(screen, 20, 50, 100, 50, text='Stop Auto', onClick=lambda: stop_auto())
    
else:
    play_auto_button = Button(screen, 20, 50, 100, 50, text='Play Auto', onClick=lambda: start_auto())

rotate_x_text_box = TextBox(screen, 20, 120, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
rotate_right_and_left_slider = Slider(screen, 20,190, 200, 20, min=0, max=100, step=1, initial=50)
rotate_y_text_box = TextBox(screen, 20, 230, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
rotate_up_and_down_slider = Slider(screen, 20, 280, 200, 20, min=0, max=100, step=1, initial=50)
zoom_text_box = TextBox(screen, 20, 310, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
zoom_in_and_out_slider = Slider(screen, 20, 350, 200, 20, min=0.1, max=5, step=0.5, initial=2.5)
shear_text_box = TextBox(screen, 20, 380, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
shear_slider = Slider(screen, 20, 420, 200, 20, min=0.1, max=2, step=0.01, initial=1)

translate_x_text_box = TextBox(screen, 20, 460, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
translate_x_slider = Slider(screen, 20, 500, 200, 20, min=-5, max=5, step=0.7, initial=0)
translate_y_text_box = TextBox(screen, 20, 540, 280, 25, fontSize=15, borderColour=(0, 0, 0), colour=(255, 255, 255), textColour=(0, 0, 0))
translate_y_slider = Slider(screen, 20, 580, 200, 20, min=-5, max=5, step=0.7, initial=0)


pygame.font.init() # you have to call this at the start, 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# text_surface = my_font.render('Rotate right and left', False, (0, 0, 0))

# Define the cube's vertices (a list of 3D points)
vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]

# Define the edges (pairs of indices into the vertices list)
# edges = [
#     (0, 1), (1, 2), (2, 3), (3, 0),
#     (4, 5), (5, 6), (6, 7), (7, 4),
#     (0, 4), (1, 5), (2, 6), (3, 7)
# ]


faces = [
    (0, 1, 2, 3),  # back face
    (4, 5, 6, 7),  # front face
    (0, 1, 5, 4),  # bottom face
    (3, 2, 6, 7),  # top face
    (1, 2, 6, 5),  # right face
    (0, 3, 7, 4)   # left face
]



# Parameters for projection
fov = 256  # Field of view
viewer_distance = 4  # How far the viewer is from the screen

# Main loop variables
angle = 0


while True:
    # Handle events (like quitting)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # translate down
                print("left")
                if not play_auto:
                    pass
            if event.key == pygame.K_RIGHT:
                # translate down
                print("right")
                
            
            if event.key == pygame.K_UP:
                # translate down
                print("UP")
                
            if event.key == pygame.K_DOWN:
                print("down")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase the rotation angle for animation
    screen.fill(color = pygame.Color(44,66,43))
    pygame_widgets.update(events)
    
    
    play_auto_button.listen(events)
    rotate_right_and_left_slider.listen(events)
    rotate_up_and_down_slider.listen(events)
    # screen.blit(text_surface, (20, 90))
    
    play_auto_button.draw()
    rotate_right_and_left_slider.draw()
    rotate_up_and_down_slider.draw()   
    translate_x_slider.draw()
    translate_y_slider.draw()
    rotate_x_text_box.setText("Rotate in x axis")
    rotate_y_text_box.setText("Rotate in y axis")
    zoom_text_box.setText("Zoom in and out")
    shear_text_box.setText("Shear ")
    translate_x_text_box.setText("Translate x axis")
    translate_y_text_box.setText("Translate y axis")

    

    angle += 0.01
    


    projected_points = []
    # for vertex in vertices:
    #     # Apply rotations
    #     rotated = vertex
    #     if play_auto:
    #         rotated = Matrix.rotateX(vertex, angle)
    #         rotated = Matrix.rotateY(rotated, angle)
    #         rotated = Matrix.rotateZ(rotated, angle)
    #         # rotated = Matrix.zoomIn(rotated, zoom_in_and_out_slider.getValue())
    #         rotated = Matrix.shearX(rotated,shear_slider.getValue())
    #         rotated = Matrix.zoomIn(rotated,zoom_in_and_out_slider.getValue())
    #         rotated = Matrix.translate(rotated, translate_x_slider.getValue(), 4,4)
    #         rotated = Matrix.translate(rotated,4,translate_y_slider.getValue(), 4)
    #         print(f"VAlue of hte slider is : {shear_slider.getValue()}")
            
            
        
    #     # Project the 3D point to 2D screen coordinates
    #     projected = project(rotated, screen_width, screen_height, fov, viewer_distance)
    #     projected_points.append(projected)

    # Draw the edges by connecting the vertices
    # for edge in edges:
    #     start, end = edge
    #     # pygame.draw.line(screen, (255, 255, 255), projected_points[start], projected_points[end], 2)
    #     pygame.draw.polygon(screen, (255,255,255), [projected_points[start], projected_points[end]],2)
    
    # Draw the filled faces
    face_colors = [
        (255, 0, 0),     # Red        - back face
        (0, 255, 0),     # Green      - front face
        (0, 0, 255),     # Blue       - bottom face
        (255, 255, 0),   # Yellow     - top face
        (255, 0, 255),   # Magenta    - right face
        (0, 255, 255)    # Cyan       - left face
    ]

    for i, face in enumerate(faces):
        point_list = [projected_points[i] for i in face]
        pygame.draw.polygon(screen, face_colors[i], point_list)
        # 3. Draw small rectangles at each projected vertex
    for point in projected_points:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(point[0]-3, point[1]-3, 6, 6))


    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(60)
