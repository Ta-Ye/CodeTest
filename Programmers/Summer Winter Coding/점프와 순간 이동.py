def solution(n):
    answer=0
    while n!=0:
        n,last=divmod(n,2)
        answer+=last
    return answer
