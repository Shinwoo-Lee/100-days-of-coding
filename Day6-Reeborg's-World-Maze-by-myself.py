def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn():
    if right_is_clear():
        turn_right()
    elif wall_on_right() and front_is_clear():
        '''Do nothing'''
    else:
        turn_left()
        turn()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    turn()
    move()