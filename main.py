import pygame as py
import settings
import map
import player



screen = py.display.set_mode((settings.screen_w, settings.screen_h))
py.display.set_caption("Tik tak Toe") 
clock  = py.time.Clock()


white = (255,255,255)
blue = (52,159,255) 
red = (255, 159, 52)


                #p1 is x, p2 is o 
player_1 = player.Player(1, False, False)
player_2 = player.Player(2, False, False)

playing = False #in active game



def start_game():
    global playing

    clear_map()
    playing = True
    player_1.is_turn = True




def main():
    pass








def clear_map():
    for row in range(map.rows):
        for col in range(map.cols):
            map.grid[row][col] = 0










def draw():


    #add a offset to center the map
    map_width  = map.cols * map.tile_size
    map_height = map.rows * map.tile_size
    offset_x = (settings.screen_w  - map_width)  // 2
    offset_y = (settings.screen_h - map_height) // 2





    for row in range(map.rows):
        for col in range(map.cols):
            
            value = map.grid[row][col]


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
                




def mouse_down(m_x, m_y):
    global player_1, player_2


    map_width  = map.cols * map.tile_size
    map_height = map.rows * map.tile_size
    offset_x = (settings.screen_w  - map_width)  // 2
    offset_y = (settings.screen_h - map_height) // 2

    # convert mouse position to grid coordinates
    grid_x = (m_x - offset_x) // map.tile_size
    grid_y = (m_y - offset_y) // map.tile_size

    # check if clicked in the grid
    if 0 <= grid_x < map.cols and 0 <= grid_y < map.rows:

        
                
        if player_1.is_turn:
            if map.grid[grid_y][grid_x] != 0: #prevent placing on other players 
                return  
            map.grid[grid_y][grid_x] = player_1.value
            player_1.is_turn = False
            player_2.is_turn = True

        elif player_2.is_turn:
            if map.grid[grid_y][grid_x] != 0: 
                return  

            map.grid[grid_y][grid_x] = player_2.value
            player_2.is_turn = False
            player_1.is_turn = True





running = True
while running:
    screen.fill((0,0,0))
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False

        if event.type == py.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = event.pos
             mouse_down(mouse_x, mouse_y)
             


    if not playing:
        start_game()

    draw()


    keys = py.key.get_pressed()
    if keys[py.K_r]:
        clear_map()


    py.display.flip() 
    clock.tick(settings.fps)
