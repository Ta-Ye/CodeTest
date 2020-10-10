def check(ck,bridge,start,end):
    if end in bridge[start]:
        return False
    
    for s in bridge[start]:
        if ck[s]==1:
            continue
        ck[s]=1
        if check(ck,bridge,s,end)==False:
            return False
    else:
        return True

def solution(n, costs):
    answer=0
    bridge=dict()
    for i in range(n):
        bridge[i]=[]
    
    for start, end, cost in sorted(costs,key=lambda x: x[2]):
        if check([0]*n,bridge,start,end):
            bridge[start].append(end)
            bridge[end].append(start)
            answer+=cost
    return answer
