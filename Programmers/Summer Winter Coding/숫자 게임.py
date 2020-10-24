def solution(A, B):
    A.sort()
    B.sort()
    answer=0
    while A and B:
        if B[-1]>A[-1]:
            answer+=1
            B.pop()
        A.pop()
    return answer
