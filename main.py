from settings import *
def start_game():
    field=[
        stock
    ]*x*y
    field_mine=[
        stock
    ]*x*y
    #create mine on pole_mine
    for i in range(nym_mines):
        x_mine=random.randint(0, x-1)
        y_mine=random.randint(0, y-1)
        position=x*y_mine+x_mine
        if field_mine[position]!=mine:
            field_mine[position]=mine
    #check mine on pole_mine
    for y_pole in range(y):
        for x_pole in range(x):
            position=x*y_pole+x_pole
            if field_mine[position]!=mine:
                number_of_mines=checkmine(x, y, x_pole, y_pole, field_mine, mine)
                field_mine[position]=number_of_mines
    game(field, field_mine)
def game(field, field_mine):
    loop=True
    while loop:
        game_input=input(f'input: [1;1] to [{x};{y}]__').split()
        loop=CheckGame(game_input, field, field_mine, x, y, mine, easy_start, infinity_life, developer_kit, show_pole_after_loss, coordinate_grid)

start_game()

