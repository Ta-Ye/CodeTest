def solution(s):
    answer=sorted([int(i) for i in s.split()])
    return str(answer[0])+' '+str(answer[-1])
