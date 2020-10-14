def solution(number, k):
    number=list(number)
    N=0
    answer=[]
    while k:
        for i in range(N,len(number)):
            N=i
            if answer and number[i]>answer[-1]:
                answer.pop()
                break
            else:
                answer.append(number[i])
        else:
            return ''.join(answer[:-k])
        k-=1
    return ''.join(answer+number[N:])
