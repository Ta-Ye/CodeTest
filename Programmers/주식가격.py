def solution(prices):
    answer=[]
    check=[[0,prices[0]]]
    for idx in range(1,len(prices)):
        if len(check):
            while len(check) and check[-1][1]>prices[idx]:
                i,num=check.pop()
                answer.append([i,idx-i])
        check.append([idx,prices[idx]])
    while len(check):
        i,num=check.pop()
        answer.append([i,len(prices)-i-1])
    answer.sort()
    answer=[i for idx,i in answer]
    return answer
