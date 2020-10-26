def solution(N, stages):
    try_stage=[0]*(N+2)
    clear_stage=[0]*(N+2)
    
    for stage in stages:
        for n in range(1,stage+1):
            clear_stage[n]+=1
        try_stage[stage]+=1
    
    for idx in range(1,N+1):
        if clear_stage[idx]==0:
            clear_stage[idx]+=1
            
    return sorted([i for i in range(1,N+1)],key=lambda x: (-try_stage[x]/clear_stage[x]))
