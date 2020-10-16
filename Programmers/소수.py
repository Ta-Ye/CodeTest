def solution(n):
    answer=[1]*(n+1)
    answer[0]=answer[1]=0
    for i in range(2,n+1):
        if answer[i]==0:
            continue
        for j in range(2*i,n+1,i):
            answer[j]=0
    return answer.count(1)
