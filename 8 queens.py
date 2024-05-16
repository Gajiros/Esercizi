import time
def print_chessboard(queue: list):
    
    for read in queue:
        print(read)

def is_safe(queue: list, row: int, column: int) -> bool:
    
    for i in range(column):
        if queue[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if queue[i][j] == 'Q':
            return False
    for i, j in zip(range(row, len(queue)), range(column, -1, -1)):
        if queue[i][j] == 'Q':
            return False
    return True
        
        

row_1: list = ['_'] * 8
row_2: list = ['_'] * 8
row_3: list = ['_'] * 8
row_4: list = ['_'] * 8
row_5: list = ['_'] * 8
row_6: list = ['_'] * 8
row_7: list = ['_'] * 8
row_8: list = ['_'] * 8
queue_rows: list = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8]
queue_columns: list = []
queens: list = ['Q'] * 8
while (queens != []):
    i: int = 0
    for row_i, row in enumerate(queue_rows):
        while (i < 8):
            if (len(queue_columns) < 8) or (i not in queue_columns):
                if (row[i] == '_') and (is_safe(queue_rows,row_i, i) == True):
                    row[i] = 'Q'
                    queens.pop(0)
                    queue_columns.append(i)
                    i += 1
                    break
                else:
                    i += 1
    print_chessboard(queue_rows)
    #print(queens) 