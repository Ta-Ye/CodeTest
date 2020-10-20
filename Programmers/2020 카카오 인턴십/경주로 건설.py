import queue
def solution(board):
    mapp=[[[10**9]*4 for _ in range(len(board))] for _ in range(len(board))]
    q=queue.Queue()
    # 동서남북 0123
    q.put([0,0,2])
    q.put([0,0,0])
    mapp[0][0]=[0,0,0,0]
    while q.qsize():
        x,y,flag=q.get()
        for xx,yy,flagg in [[0,1,0],[0,-1,1],[1,0,2],[-1,0,3]]:
            nx,ny=x+xx,y+yy
            if nx in [-1,len(board)] or ny in [-1,len(board)]:
                continue
            if board[nx][ny]==1:
                continue
            cost= 1 if flag==flagg else 6
            if mapp[nx][ny][flagg]>mapp[x][y][flag]+cost:
                mapp[nx][ny][flagg]=mapp[x][y][flag]+cost
                q.put([nx,ny,flagg])
    
    return min(mapp[-1][-1])*100
