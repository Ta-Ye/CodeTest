def solution(board):
    for x in range(1,len(board)):
        for y in range(1,len(board[0])):
            if board[x][y]:
                board[x][y]=min(board[x-1][y],board[x-1][y-1],board[x][y-1])+1
    return max([max(i) for i in board])**2
