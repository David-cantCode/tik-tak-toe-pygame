import pygame as py


screen = py.display.set_mode((settings.screen_w, settings.screen_h))
py.display.set_caption("Tik tak Toe") 
clock  = py.time.Clock()



running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False


    py.display.flip() 
    clock.tick(settings.fps)
