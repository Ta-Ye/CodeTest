import queue
def move(robot,check,board,N):
    q=queue.Queue()
    q.put(robot)
    m = [[0,1],[0,-1],[1,0],[-1,0]]
    while q.qsize():
        x,y,flag=q.get()
        for xx,yy in m: #상하좌우
            nx,ny=x+xx,y+yy
            if flag:
                if -1 in [nx,ny,nx-1] or N in [nx,ny]:
                    continue
                if board[nx][ny] or board[nx-1][ny]:
                    continue
            else:
                if -1 in [nx,ny,ny-1] or N in [nx,ny,ny-1]:
                    continue
                if board[nx][ny] or board[nx][ny-1]:
                    continue
            if check[nx][ny][flag]>check[x][y][flag]+1:
                check[nx][ny][flag]=check[x][y][flag]+1
                q.put([nx,ny,flag])
        if flag: #세로
            # 왼쪽 위로
            if y+1<N and board[x][y+1]==0 and board[x-1][y+1]==0 and check[x-1][y+1][0]>check[x][y][1]+1:
                check[x-1][y+1][0]=check[x][y][1]+1
                q.put([x-1,y+1,0])
            # 왼쪽 아래
            if y+1<N and board[x][y+1]==0 and board[x-1][y+1]==0 and check[x][y+1][0]>check[x][y][1]+1:
                check[x][y+1][0]=check[x][y][1]+1
                q.put([x,y+1,0])
            # 오른쪽 위로
            if y-1>=0 and board[x][y-1]==0 and board[x-1][y-1]==0 and check[x-1][y][0]>check[x][y][1]+1:
                check[x-1][y][0]=check[x][y][1]+1
                q.put([x-1,y,0])
            # 오른쪽 아래
            if y-1>=0 and board[x][y-1]==0 and board[x-1][y-1]==0 and check[x][y][0]>check[x][y][1]+1:
                check[x][y][0]=check[x][y][1]+1
                q.put([x,y,0])
        else: #가로
            # 왼쪽 위로
            if x-1>=0 and board[x-1][y]==0 and board[x-1][y-1]==0 and check[x][y][1]>check[x][y][0]+1:
                check[x][y][1]=check[x][y][0]+1
                q.put([x,y,1])
            # 왼쪽 아래
            if x+1<N and board[x+1][y]==0 and board[x+1][y-1]==0 and check[x+1][y][1]>check[x][y][0]+1:
                check[x+1][y][1]=check[x][y][0]+1
                q.put([x+1,y,1])
            # 오른쪽 위로
            if x-1>=0 and board[x-1][y]==0 and board[x-1][y-1]==0 and check[x][y-1][1]>check[x][y][0]+1:
                check[x][y-1][1]=check[x][y][0]+1
                q.put([x,y-1,1])
            # 오른쪽 아래
            if x+1<N and board[x+1][y]==0 and board[x+1][y-1]==0 and check[x+1][y-1][1]>check[x][y][0]+1:
                check[x+1][y-1][1]=check[x][y][0]+1
                q.put([x+1,y-1,1])

def solution(board):
    N=len(board)
    robot=[0,1,0]
    check=[[[10**5,10**5] for _ in range(N)] for _ in range(N)]
    check[0][1][0]=0
    move(robot,check,board,N)
    return min(check[N-1][N-1])
