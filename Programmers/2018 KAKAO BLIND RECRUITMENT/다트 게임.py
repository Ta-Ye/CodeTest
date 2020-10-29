import re
def solution(dartResult):
    f=re.compile("(\d+)([A-Z])(\*|#?)")
    answer=[0]*len(dartResult)
    for idx,(score, bonus, option) in enumerate(f.findall(dartResult)):
        if bonus=='D':
            answer[idx]=int(score)**2
        elif bonus=='T':
            answer[idx]=int(score)**3
        else:
            answer[idx]=int(score)
            
        if option=='*':
            if idx!=0:
                answer[idx-1]*=2
            answer[idx]*=2
        elif option=='#':
            answer[idx]*=-1
            
    return sum(answer)
