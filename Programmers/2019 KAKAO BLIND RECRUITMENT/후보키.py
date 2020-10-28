from itertools import combinations as coms
def solution(relation):
    answer=[]
    for num in range(1,len(relation[0])+1):
        for com in coms([i for i in range(len(relation[0]))],num):
            ck=[]
            for x in range(len(relation)):
                ck.append(tuple([relation[x][y] for y in com]))
            if len(ck)==len(set(ck)):
                answer.append(list(com))
    
    last=[1]*len(answer)
    for i in range(len(answer)):
        if last[i]==0:
            continue
        for j in range(i+1,len(answer)):
            for k in range(len(answer[i])):
                if not answer[i][k] in answer[j]:
                    break
            else:
                last[j]=0
    return sum(last)
