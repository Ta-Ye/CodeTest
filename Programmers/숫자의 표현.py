def solution(n):
    cnt=[]
    i=1
    while sum(cnt)<n:
        cnt.append(i)
        i+=1
    
    N=cnt[-1]
    answer=1
    for i in range(N,n):
        cnt=0
        cp=i
        while cnt<n:
            cnt+=cp
            cp-=1
        if cnt==n:
            answer+=1
            
    return answer
    
