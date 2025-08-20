import time
import curses

def game_loop(window):
    # Setup inicial
    curses.curs_set(0)
    personagem = [
        [10,15],
        [9,15],
        [8,15],
        [7,15],
        
    ]

    current_direction = curses.KEY_RIGHT   
    
    while True:
        draw_screen(window=window)
        draw_actor(actor = personagem,window=window)
        direction = get_new_direction (window=window,timeout = 1000)
        if direction is None:
            direction = current_direction

        move_actor(actor=personagem,direction=direction)
        if actor_hit_border(actor=personagem,window = window):
            return
        current_direction = direction
        
def draw_screen(window):
    
    window.clear()
    window.border(0)
    
    
def draw_actor(actor,window):
    for numero in actor:
        window.addch(numero[0],numero[1], curses.ACS_DIAMOND)





def get_new_direction(window,timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP,curses.KEY_LEFT,curses.KEY_DOWN,curses.KEY_RIGHT]:
       return direction
    return None


def move_actor(actor,direction):
        
        match direction:
            case curses.KEY_UP:
                actor[3][0] -= 1
                actor.append([actor[3][0],actor[3][1]])
                actor.pop(0)
            case curses.KEY_LEFT:
                actor[3][1] -= 1
                actor.append([actor[3][0],actor[3][1]])
                actor.pop(0)
            case curses.KEY_DOWN:
                actor[3][0] += 1
                actor.append([actor[3][0],actor[3][1]])
                actor.pop(0)
            case curses.KEY_RIGHT:
                actor[3][1] += 1
                actor.append([actor[3][0],actor[3][1]])
                actor.pop(0)
            case _:
                pass



def actor_hit_border(actor,window):
    height,width = window.getmaxyx()
        

    if (actor[3][0] <=0) or (actor[3][0] >= height-1):
        return True
    if (actor[3][1] <=0) or (actor[3][1] >= width-1):
        return True
    else:
        return False
    
if __name__ == "__main__":
    curses.wrapper(game_loop)
    print('Perdeu!')
