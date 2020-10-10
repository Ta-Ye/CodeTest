def solution(routes):
    answer=[]
    for x,y in sorted(routes):
        for idx, s in enumerate(answer):
            if x<=s[1] and y>=s[0]:
                answer[idx]=[max(x,s[0]),min(y,s[1])]
                break
        else:
            answer.append([x,y])
    return len(answer)
