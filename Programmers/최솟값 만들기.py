def solution(A,B):
    A.sort()
    B.sort()
    return sum([A[i]*B[len(A)-1-i] for i in range(len(A))])
