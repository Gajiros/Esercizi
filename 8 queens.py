import time
def print_chessboard(queue: list):
    
    for read in queue:
        print(read)

def is_safe(queue_rows: list) -> bool:
    for row in queue_rows:
        

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
    for read_r in queue_rows:
        while (i < 8):
            if (len(queue_columns) < 8) or (len(queue_columns) == None):
                if (read_r[i] == '_') and (i not in queue_columns):
                    read_r[i] = 'Q'
                    queens.pop(0)
                    queue_columns.append(i)
                    i += 1
                    break
                else:
                    i += 1
    print_chessboard(queue_rows)
    #print(queens)