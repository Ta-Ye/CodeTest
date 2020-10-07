def solution(clothes):
    fashion=dict()
    for cloth, what in clothes:
        if what in fashion:
            fashion[what].append(cloth)
        else:
            fashion[what]=[cloth]
    answer=1
    for name in fashion:
        answer*=len(fashion[name])+1
    return answer-1
