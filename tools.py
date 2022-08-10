def checkmine(x, y, cell_coordinate_x, cell_coordinate_y, field_list, obj):
    out=0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x1=cell_coordinate_x+j
            y1=cell_coordinate_y+i
            if x1<0 or x1>=x or y1<0 or y1>=y:
                continue
            if field_list[x*y1+x1]==obj:
                out+=1
    return out
def showlist(x, y, list, coordinate_grid):
    if coordinate_grid==True:
        axis_x=''
        for i in range(1,x+1):
            axis_x+=f'{i} '
        print(' '*4,axis_x,'\n'*1)
    space=4
    f=1
    for i in range(y):
        out_screen=''
        for j in range(x):
            position=x*i+j
            out_screen+=f'{list[position]} '
        if coordinate_grid==True:
            if (i+1)==10**f:
                space-=1
                f+=1
            out_screen=f'{i+1}{" "*(space)}{out_screen}'
        print(out_screen)
