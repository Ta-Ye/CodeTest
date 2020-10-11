def find(n,fight,num,result,ck):
    if ck[n]:
        return result[n]
    answer=[]
    for idx,fi in enumerate(fight[n]):
        if fi==num:
            answer.append(idx)
            answer+=find(idx,fight,num,result,ck)
    answer=list(set(answer))
    result[n]=answer
    ck[n]=1
    return answer

def solution(n, results):
    answer=0
    fight=[[0]*(n+1) for _ in range(n+1)]
    for w,l in results:
        fight[w][l]=1
        fight[l][w]=-1
    win=[[] for _ in range(n+1)]
    lose=[[] for _ in range(n+1)]
    win_ck=[0]*(n+1)
    lose_ck=[0]*(n+1)
    
    for i in range(1,n+1):
        if len(find(i,fight,1,win,win_ck)+find(i,fight,-1,lose,lose_ck))==n-1:
            answer+=1
    return answer
