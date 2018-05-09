m,n = map(int,input().split())

board = input()
board = board.replace('[','')
board = board.replace(']','')
board = board.split(',')
for idx, city in enumerate(board):
    board[idx] = list(city.strip().strip('“').strip('”'))
disppearedBlocks = set()
def findHitBlock():
    global board
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '*':
                #print('hit',i,j)
                disppearedBlocks.add((i,j))
                disppearedBlocks.add((i,j+1))
                disppearedBlocks.add((i+1,j))
                disppearedBlocks.add((i+1,j+1))
def arrangeBoard():
    global board
    global disppearedBlocks
    for point in disppearedBlocks:
        board[point[0]][point[1]] = '*'
    for i in range(len(board)-1):
        for j in range(len(board[0])):
            if board[i+1][j] == '*' and board[i][j] != '*':
                temp = board[i][j]
                board[i][j] = board[i+1][j]
                board[i+1][j] = temp
for _ in range(n*n-1):
    findHitBlock()
    arrangeBoard()
    disppearedBlocks = set()
count = 0
for block in board:
    count += block.count('*')
print(count)