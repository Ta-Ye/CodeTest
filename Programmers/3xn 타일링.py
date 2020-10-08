def solution(n):
    answer=[1]*(n//2+1)
    for i in range(1,n//2+1):
        answer[i]=(3*answer[i-1]+2*sum(answer[:i-1]))%1000000007
    return answer[n//2] if n%2==0 else 0
