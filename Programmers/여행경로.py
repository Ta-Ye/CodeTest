last=[]
def dfs(here,check,tickets,answer):
    if not 0 in check:
        last.append(answer)
        return
    
    for idx, s in enumerate(tickets):
        if check[idx]:
            continue
        if s[0]==here:
            check[idx]=1
            dfs(s[1],check,tickets,answer+[s[1]])
            check[idx]=0
            
def solution(tickets):
    dfs('ICN',[0]*len(tickets),tickets,['ICN'])
    return sorted(last)[0]
