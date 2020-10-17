def solution(n, s):
    ans,last=divmod(s,n)
    answer=[ans for _ in range(n-last)]+[ans+1 for _ in range(last)]
    return answer if ans else [-1]
