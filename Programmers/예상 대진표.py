def solution(n,a,b):
    answer=0
    while a!=b:
        answer+=1
        a=sum(divmod(a,2))
        b=sum(divmod(b,2))
    return answer
