import math
def solution(begin, end):
    answer=[]
    for i in range(begin,end+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0 and i//j<10**7:
                answer.append(i//j)
                break
        else:
            answer.append(1)
    return answer if begin!=1 else [0]+answer[1:]
