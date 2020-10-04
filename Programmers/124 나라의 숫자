def solution(n):
    answer = ''
    while n>3:
        n, last= divmod(n,3)
        if last==0:
            n-=1
            last+=3
        answer=str(last)+answer if last!=3 else str(4)+answer
    answer=str(n)+answer if n!=3 else str(4)+answer
    return answer
