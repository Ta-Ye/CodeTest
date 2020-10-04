def solution(priorities, location):
    answer = []
    cnt=1
    check=[i for i in range(len(priorities))]
    for idx,priorty in enumerate(priorities):
        if priorty>=max(priorities[idx:]):
            answer.append(check[idx])
        else:
            priorities.append(priorty)
            check.append(check[idx])
    
    for idx,i in enumerate(answer):
        if i==location:
            return idx+1
