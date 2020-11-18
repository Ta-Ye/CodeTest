import queue
def solution(n, path, order):
    wait,check=[0]*(n+1),[0]*(n+1)
    path_dict=dict()
    
    for x, y in path:
        if x in path_dict:
            path_dict[x].append(y)
        else:
            path_dict[x]=[y]
        if y in path_dict:
            path_dict[y].append(x)
        else:
            path_dict[y]=[x]

    # order
    before={y:x for x,y in order} # y 가기전에 가야하는 방 x
    after={x:y for x,y in order} # x 가고나서 갈수있는 방 y

    q=queue.Queue()
    q.put(0)
    while q.qsize():
        ck=q.get()
        if ck in before and check[before[ck]]==0 and wait[ck]==0: # 방문 이전에 가야하는 방  방문x
            wait[ck]=1
            continue
            
        elif ck in after: # 다음에 방문 가능한 방 존재
            if wait[after[ck]]: # 기다리는 중
                q.put(after[ck]) # 우선적으로 함
        
        for nx in path_dict[ck]:
            if check[nx]==0:
                q.put(nx)
        
        check[ck]=1
        
    return True if sum(check)==n else False
