import queue
def solution(maps):
    cost=[[10**5]*len(maps[0]) for _ in range(len(maps))]
    cost[0][0]=1
    
    move=[[0,1],[0,-1],[1,0],[-1,0]]
    
    q=queue.Queue()
    q.put([0,0])
    
    while q.qsize():
        x,y=q.get()
        for xx,yy in move:
            nx,ny=x+xx,y+yy
            if nx in [-1,len(maps)] or ny in [-1,len(maps[0])]:
                continue
            if maps[nx][ny]==0:
                continue
            if cost[nx][ny] > cost[x][y]+1:
                cost[nx][ny]=cost[x][y]+1
                q.put([nx,ny])
    
    return cost[-1][-1] if cost[-1][-1]!=10**5 else -1
