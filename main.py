import pygame as py
import settings
import map

screen = py.display.set_mode((settings.screen_w, settings.screen_h))
py.display.set_caption("Tik tak Toe") 
clock  = py.time.Clock()


white = (255,255,255)
blue = (52,159,255) 
red = (255, 159, 52)

def draw():


    #add a offset to center the map
    map_width  = map.cols * map.tile_size
    map_height = map.rows * map.tile_size
    offset_x = (settings.screen_w  - map_width)  // 2
    offset_y = (settings.screen_h - map_height) // 2





    for row in range(map.rows):
        for col in range(map.cols):
            
            value = map.map[row][col]


            #get location of each 'box'
            x = offset_x + col * map.tile_size + map.tile_size // 2
            y = offset_y + row * map.tile_size + map.tile_size // 2

            
            


            #draw a box outline
            py.draw.rect(screen, white, (offset_x + col * map.tile_size, offset_y + row * map.tile_size, map.tile_size, map.tile_size), 1)  


            #draw x
            if value == 1:
                py.draw.line(screen, red, (x -20, y -20), (x + 20, y +20), 1)
                py.draw.line(screen, red, (x + 20, y -20), (x - 20, y + 20), 1) #first try lol im a genius 

            #draw circle
            if value == 2:                                                  
                py.draw.circle(screen, blue, (x, y), settings.circle_size, 1)
                











running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False
        
        draw()


    py.display.flip() 
    clock.tick(settings.fps)
