from settings import *
def start_game():
    pole=[
        stock
    ]*x*y
    pole_mine=[
        stock
    ]*x*y
    #create mine on pole_mine
    for i in range(nym_mines):
        x_mine=random.randint(0, x-1)
        y_mine=random.randint(0, y-1)
        position=x*y_mine+x_mine
        if pole_mine[position]!=mine:
            pole_mine[position]=mine
    #check mine on pole_mine
    for y_pole in range(y):
        for x_pole in range(x):
            position=x*y_pole+x_pole
            if pole_mine[position]!=mine:
                number_of_mines=checkmine(x, y, x_pole, y_pole, pole_mine, mine)
                pole_mine[position]=number_of_mines
    game(pole, pole_mine)
def game(pole, pole_mine):
    loop=True
    while loop:
        game_input=input(f'input: [1;1] to [{x};{y}]__').split()
        loop=CheckGame(game_input, pole, pole_mine, x, y, mine, easy_start, infinity_life, developer_kit, show_pole_after_loss, coordinate_grid)

start_game()

