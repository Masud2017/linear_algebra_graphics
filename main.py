import sys
import sdl2.ext

if __name__ == "__main__": 
    resources = sdl2.ext.Resources(__file__, "resources")
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello world", size = (640, 480))
    window.show()
    
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(resources.get_path("pikachu.jpg"))

    spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer.render(sprite)
    
    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)
    sdl2.ext.quit()
    
    print("Hello world this is my linear algebra project")