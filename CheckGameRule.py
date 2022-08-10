from tools import *
def CheckGame(game_input, field, field_mine, x, y, obj, easy_start, cheats, developer_kit, show_pole_after_loss, coordinate_grid):
    out=True
    if developer_kit==True and game_input[0]=='dev':
        showlist(x, y, field_mine, coordinate_grid)
    try:
        x1=int(game_input[0])-1
        y1=int(game_input[1])-1
        field[x*y1+x1]
    except:
        print('[invalid position]')
        out=True
        return out
    position=x*y1+x1
    if easy_start==True:
        if field_mine[position]!=obj:
            for i in range(y):
                for j in range(x):
                    if field_mine[x*i+j]==0:
                        field[x*i+j]=field_mine[x*i+j]
                        for i1 in range(-1, 2):
                            for j1 in  range(-1, 2):
                                k=i+i1
                                z=j+j1
                                if k<0 or k>=x or z<0 or z>=y:
                                    continue
                                if field_mine[x*k+z]!=0 and field_mine[x*k+z]!=obj:
                                    field[x*k+z]=field_mine[x*k+z]
                    if field_mine[x*i+j]!=0 and field_mine[x*i+j]!=obj:
                        pass

    if field_mine[position]==obj:
        out=False
        input('You are loss(')
    if cheats==True:
        out=cheats
    if show_pole_after_loss==False and out==False or out==True:
        field[position]=field_mine[position]
        showlist(x, y, field, coordinate_grid)
    if show_pole_after_loss==True and out==False:
        showlist(x, y, field_mine, coordinate_grid)
    return out
