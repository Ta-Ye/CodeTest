def solution(d, budget):
    ck=answer=0
    for i in sorted(d):
        ck+=i
        if ck<=budget:
            answer+=1
        else:
            break
    return answer
