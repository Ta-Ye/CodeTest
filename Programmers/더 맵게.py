def solution(scoville, K):
    answer = 0
    scoville.sort(reverse=True)
    while scoville[-1]<K:
        if len(scoville)==1:
            return -1
        a=scoville.pop()
        scoville[-1]=a+scoville[-1]*2
        scoville.sort(reverse=True)
        answer+=1
    return answer
