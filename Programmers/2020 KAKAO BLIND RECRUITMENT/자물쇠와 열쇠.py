def rotate(key,N):
    k=[[] for _ in range(N)]
    for y in range(N):
        for x in range(N-1,-1,-1):
            k[y].append(key[x][y])
    return k

def check(key,lock):
    for x in range(len(key)-len(lock)+1):
        for y in range(len(key)-len(lock)+1):
            flag=True
            for xx in range(len(lock)):
                for yy in range(len(lock)):
                    if key[x+xx][y+yy]+lock[xx][yy]!=1:
                        flag=False
                        break
                if not flag:
                    break
            else:
                return True
    else:
        return False
                
    
def solution(key, lock):
    new_key=[[0]*(len(key)+2*len(lock)-2) for _ in range(len(key)+2*len(lock)-2)]
    for x in range(len(key)):
        for y in range(len(key)):
            new_key[x+len(lock)-1][y+len(lock)-1]=key[x][y]
    
    for _ in range(4):
        new_key=rotate(new_key,len(new_key))
        if check(new_key,lock):
            return True
    else:
        return False
