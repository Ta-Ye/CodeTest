def solution(n):
    num=bin(n)[2:].count('1')
    n+=1
    while num != bin(n)[2:].count('1'):
        n+=1
    return n
