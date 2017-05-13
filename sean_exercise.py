manhattan_grid = []

for r in range(8):
    row_list = []
    for i in range(8):
        row_list.append('O')

    manhattan_grid.append(row_list)

#print manhattan_grid

manhattan_grid[0][4] = 'W'
manhattan_grid[1][3] = 'B'
manhattan_grid[2][1] = 'B'
manhattan_grid[2][2] = 'W'
manhattan_grid[2][7] = 'W'
manhattan_grid[3][5] = 'B'
manhattan_grid[4][0] = 'W'
manhattan_grid[4][3] = 'B'
manhattan_grid[5][2] = 'W'
manhattan_grid[5][5] = 'W'
manhattan_grid[6][0] = 'B'
manhattan_grid[6][6] = 'B'
manhattan_grid[7][3] = 'W'
manhattan_grid[7][4] = 'B'


for m in manhattan_grid:
    print m


dp_table = []

for r in range(9):
    row_list = []
    for i in range(9):
        row_list.append(0)

    dp_table.append(row_list)


# fill in the first row in dp_table
for column_index in range(8):
    stuff =  manhattan_grid[0][column_index]
    if stuff == 'B':
        dp_table[0][column_index + 1] = dp_table[0][column_index] + 10000
    elif stuff == 'W':
        dp_table[0][column_index + 1] = dp_table[0][column_index] - 20000
    else:
        dp_table[0][column_index + 1] = dp_table[0][column_index]


for row_index in range(8):
    stuff =  manhattan_grid[row_index][0]
    if stuff == 'W':
        dp_table[row_index + 1][0] = dp_table[row_index][0] - 20000
    elif stuff == 'B':
        dp_table[row_index + 1][0] = dp_table[row_index][0] + 10000
    else:
        dp_table[row_index + 1][0] = dp_table[row_index][0]



# find neighboring blocks that matter

def find_neighbors(row_index, col_index):
    if row_index-1 >= 0 and row_index-1 < 8 and col_index-1 >= 0 and col_index-1 <8:
        nw_stuff = manhattan_grid[row_index-1][col_index-1]
    else:
        nw_stuff = 'O'

    if row_index-1 >= 0 and row_index-1 < 8 and col_index >= 0 and col_index <8:
        ne_stuff = manhattan_grid[row_index-1][col_index]
    else:
        ne_stuff = 'O'

    if row_index >= 0 and row_index < 8 and col_index-1 >= 0 and col_index-1 <8:
        sw_stuff = manhattan_grid[row_index][col_index-1]
    else:
        sw_stuff = 'O'

    return (nw_stuff, ne_stuff, sw_stuff)


# print find_neighbors(8,1)

for r in range(1,9):
    for c in range(1,9):
        (nw_stuff, ne_stuff, sw_stuff) = find_neighbors(r, c)
        option1_money = dp_table[r-1][c]
        if nw_stuff == 'B':
            option1_money += 10000
        elif nw_stuff == 'W':
            option1_money -= 20000

        if ne_stuff == 'B':
            option1_money += 10000
        elif ne_stuff == 'W':
            option1_money -= 20000

        option2_money = dp_table[r][c-1]
        if nw_stuff == 'B':
            option2_money += 10000
        elif nw_stuff == 'W':
            option2_money -= 20000

        if sw_stuff == 'B':
            option2_money += 10000
        elif sw_stuff == 'W':
            option2_money -= 20000

        if option2_money >= option1_money:
            dp_table[r][c] = option2_money
        else:
            dp_table[r][c] = option1_money


for row in dp_table:
    print row