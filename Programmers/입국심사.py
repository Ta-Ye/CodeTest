def solution(n, times):
    start=0
    end=min(times)*n
    answer=[]
    while start<=end:
        middle=(start+end)//2
        cnt=0
        for time in times:
            cnt+=middle//time
        if cnt>=n:
            end=middle-1
        else:
            start=middle+1
    return start
