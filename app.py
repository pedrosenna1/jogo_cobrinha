import time
import curses
import random

 

def game_loop(window):
    # Setup inicial
    curses.curs_set(0)
    personagem = [
        [10,15],
        [9,15],
        [8,15],
        [7,15],
        
    ]

    fruit = get_new_fruit(window=window)
    current_direction = curses.KEY_RIGHT
    timeout = 500   
    contagem_fruits = 0
    while True:
        draw_screen(window=window)
        draw_snake(personagem=personagem,window=window)
        draw_actor(actor=fruit,window=window,char=curses.ACS_DIAMOND)
        direction = get_new_direction (window=window,timeout = timeout)
        if direction is None:
            direction = current_direction
        if direction_is_opposite(direction=direction,current_direction = current_direction):
            direction = current_direction
    
        move_snake(personagem=personagem,direction=direction)
        if personagem[0] in personagem[1:]:
            break
        if snake_hit_border(personagem=personagem,window = window):
            break
        if snake_hit_fruit(personagem=personagem,fruit=fruit):
            snake_add(personagem=personagem)
            contagem_fruits = contagem_fruits + 1
            if timeout > 200:
                timeout = timeout - 50
            elif timeout > 100:
                timeout = timeout - 20
            else:
                timeout = timeout - 1
            fruit = get_new_fruit(window=window)
        
        current_direction = direction
    
    finish_game(contagem_fruits,window=window)


def finish_game(contagem_fruits,window):
        height, width = window.getmaxyx()
        s = f'Você perdeu! Coletou {contagem_fruits} frutas!'
        y = int(height / 2)
        x = int((width - len(s)) / 2)
        window.addstr(y,x,s)
        window.refresh()
        time.sleep(4)
    
    
      

def direction_is_opposite(direction,current_direction):
        match direction:
            case curses.KEY_UP:
                return current_direction == curses.KEY_DOWN
            case curses.KEY_LEFT:
                return current_direction == curses.KEY_RIGHT
            case curses.KEY_DOWN:
                return current_direction == curses.KEY_UP

            case curses.KEY_RIGHT:
                return current_direction == curses.KEY_LEFT


def get_new_fruit(window):
    height,width = window.getmaxyx()

    return [random.randint(1,height-2),random.randint(1,width-2)]


def snake_hit_border(personagem,window):
    head = personagem[0]
    return actor_hit_border(actor=head,window=window)

def snake_hit_fruit(personagem,fruit):
    return fruit in personagem

def snake_add(personagem):
    aumentar = personagem[-1][0] - 1
    personagem.append([aumentar,15])
        
def draw_screen(window):
    
    window.clear()
    window.border(0)


def draw_snake(personagem, window):
    head = personagem[0]
    draw_actor(actor=head,window=window,char='@')
    body = personagem[1:]
    for body_part in body:
        draw_actor(actor=body_part,window=window,char='s') 
    
def draw_actor(actor,window,char):
    # for numero in actor:
        window.addch(actor[0],actor[1], char)





def get_new_direction(window,timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP,curses.KEY_LEFT,curses.KEY_DOWN,curses.KEY_RIGHT]:
       return direction
    return None

def move_snake(personagem,direction):
    head = personagem[0].copy()
    move_actor(actor=head,direction=direction)
    personagem.insert(0,head)
    personagem.pop()
    
        


def move_actor(actor,direction):
        
        match direction:
            case curses.KEY_UP:
                actor[0] -= 1
            case curses.KEY_LEFT:
                actor[1] -= 1
            case curses.KEY_DOWN:
                actor[0] += 1

            case curses.KEY_RIGHT:
                actor[1] += 1





def actor_hit_border(actor,window):
    height,width = window.getmaxyx()
        

    if (actor[0] <=0) or (actor[0] >= height-1):
        return True
    if (actor[1] <=0) or (actor[1] >= width-1):
        return True
    else:
        return False
    

if __name__ == "__main__":
    curses.wrapper(game_loop)
    print('Perdeu!')
    
