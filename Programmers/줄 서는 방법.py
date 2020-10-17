def solution(n, k):
    answer=[]
    num=list(range(1,n+1))
    
    while num:
        cp=1
        for i in range(2,n):
            cp*=i
        ck= k//cp if k%cp>0 else k//cp-1
        answer.append(num[ck])
        num=num[:ck]+num[ck+1:]
        k-=cp*ck
        n-=1
    return answer
