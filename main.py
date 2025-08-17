import pygame as py
import settings
import map
import player


py.init()  
screen = py.display.set_mode((settings.screen_w, settings.screen_h))
py.display.set_caption("Tik tak Toe") 
clock  = py.time.Clock()


white = (255,255,255)
blue = (52,159,255) 
red = (255, 159, 52)


                #p1 is x, p2 is o 
player_1 = player.Player(1, False, False, 0)
player_2 = player.Player(2, False, False, 0)

playing = False #in active game

font = py.font.SysFont('Arial', 20)


chose_first_turn = 1



def start_game():
    global playing, chose_first_turn

    clear_map()
    playing = True

    if chose_first_turn == 1: 
        chose_first_turn = 2
        player_1.is_turn = True

    else:
        chose_first_turn = 1
        player_2.is_turn = True

    


def text():
    if player_1.is_turn:
        current_player_txt = "Current turn, Player 1"
    elif player_2.is_turn:
        current_player_txt = "Current turn, Player 2"
     
    text_surface_1 = font.render(current_player_txt, True, white) 
    text_rect_1 = text_surface_1.get_rect()
    text_rect_1.center = (100, 25)
    screen.blit(text_surface_1, text_rect_1)



    score_txt = f"P1 {player_1.score} - {player_2.score} P2"
    text_surface_2 = font.render(score_txt, True, white) 
    text_rect_2 = text_surface_2.get_rect()
    text_rect_2.center = (400, 220)
    screen.blit(text_surface_2, text_rect_2)

    


def clear_map():
    for row in range(map.rows):
        for col in range(map.cols):
            map.grid[row][col] = 0


def win_check():
    #win check is using a genius system where it checks one position on the matrix, (if 0 return) then checks if the next positions are == to the first position, if all 3 == returns winner



    #rows
    for row in range(map.rows):
        if map.grid[row][0] != 0 and map.grid[row][0] == map.grid[row][1] == map.grid[row][2]:
            return map.grid[row][0]  # returns 1 or 2 depending on winner

    # columns
    for col in range(map.cols):
        if map.grid[0][col] != 0 and map.grid[0][col] == map.grid[1][col] == map.grid[2][col]:
            return map.grid[0][col]

    # diagonals
    if map.grid[0][0] != 0 and map.grid[0][0] == map.grid[1][1] == map.grid[2][2]:
        return map.grid[0][0]

    if map.grid[0][2] != 0 and map.grid[0][2] == map.grid[1][1] == map.grid[2][0]:
        return map.grid[0][2]

    return 0  

    #ret 0 - none 
    #ret 1 = p1 
    #ret 2  = p2




def is_board_full():
    #goes through the matrix, if it finds a cell with the value 0 (empty) it returns
    for row in map.grid:
        for cell in row:
            if cell == 0:
                return False 
    return True  

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

        winner = win_check()
        if winner != 0:
            game_end(winner)

        if is_board_full():
            game_end(0)




def game_end(winner):
    global playing 

    #add text on screen instead of in terminal?
    if winner == 1: 
        player_1.score += 1
        print("Congrats player " + str(winner) + " won the game")
    
    elif winner == 2:
        player_2.score += 1
        print("Congrats player " + str(winner) + " won the game")

    else:
        print("game drew")

    playing = False












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
    text()


    keys = py.key.get_pressed()
    if keys[py.K_r]:
        clear_map()


    py.display.flip() 
    clock.tick(settings.fps)
