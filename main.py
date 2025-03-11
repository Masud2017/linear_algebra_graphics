import sys
import sdl2.ext
from config import resources

if __name__ == "__main__": 
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello world", size = (640, 480))
    window.show()
    
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(resources.get_path("pikachu.jpg"))

    spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer.render(sprite)
    
    run = True
    while run:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                run = False
                break
            window.refresh()
    sdl2.ext.quit()