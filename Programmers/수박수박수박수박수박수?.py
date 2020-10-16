def solution(n):
    answer=['수','박']*(1+n//2)
    return ''.join(answer[:n])
