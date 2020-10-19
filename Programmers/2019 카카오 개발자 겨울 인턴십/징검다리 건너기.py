def solution(stones, k):    
    start,end=0,max(stones)
    while start<=end:
        middle=(start+end)//2
        cnt=cnt2=0
        for stone in stones:
            if stone-middle<=0:
                cnt2+=1
            else:
                cnt=max(cnt,cnt2)
                cnt2=0
        else:
            cnt=max(cnt,cnt2)
        if cnt>=k:
            end=middle-1
        else:
            start=middle+1
    
    return start
