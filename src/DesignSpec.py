from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import pygame

class DesignSpec:
    def __init__(self, screen):
        self.play_auto_button = Button(screen, 20, 50, 100, 50, text='Play Auto', onClick=lambda: print('Play Auto clicked!'))
        self.rotate_right_and_left_slider = Slider(screen, 20, 120, 200, 20, min=0, max=100, step=1, initial=50)
        self.rotate_up_and_down_slider = Slider(screen, 20, 275, 200, 20, min=0, max=100, step=1, initial=50)
        self.zoom_in_and_out_slider = Slider(screen, 20, 430, 200, 20, min=0, max=100, step=1, initial=50)
        # self.rotate_right_and_left_slider.setText('Rotate right and left')
        # self.rotate_up_and_down_slider.setText('Rotate up and down')
        # self.zoom_in_and_out_slider.setText('Zoom in and out')

        pygame.font.init() # you have to call this at the start, 
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = my_font.render('Rotate right and left', False, (0, 0, 0))
    

    def get_play_auto_button(self):
        return self.play_auto_button

    def get_rotate_right_and_left_slider(self):
        return self.rotate_right_and_left_slider

    def get_rotate_up_and_down_slider(self):
        return self.rotate_up_and_down_slider

    def get_zoom_in_and_out_slider(self):
        return self.zoom_in_and_out_slider

    def get_text_surface(self):
        return self.text_surface
