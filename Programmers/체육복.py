def solution(n, lost, reserve):
    answer = n-len(lost)
    lost2=[]
    for los in lost:
        if los in reserve:
            reserve.remove(los)
            answer+=1
        else:
            lost2.append(los)
    
    for los in lost2:
        if los-1 in reserve:
            reserve.remove(los-1)
            answer+=1
        elif los+1 in reserve:
            reserve.remove(los+1)
            answer+=1
            
    return answer
