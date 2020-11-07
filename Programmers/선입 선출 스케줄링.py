def solution(n, cores):
    if len(cores)>=n:
        return n
    n-=len(cores)
    
    new_cores=sorted(cores)
    start,end=1,new_cores[-1]*n
    while start<=end:
        middle= (start+end)//2
        num = sum([middle//core for core in cores])
        if num>=n:
            end=middle-1
        else:
            start=middle+1
    
    for idx, core in enumerate(cores):
        n-=(start-1)//core
    
    for idx, core in enumerate(cores):
        if start%core==0:
            answer=idx+1
            n-=1
            if n==0:
                return answer
