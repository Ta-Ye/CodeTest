def solution(n):
    n**=0.5
    return (n+1)**2 if n-int(n)==0 else -1
