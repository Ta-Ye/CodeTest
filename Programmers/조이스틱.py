def solution(name):
    answer = 0
    alpha=dict()
    for num in range(ord('A'),ord('Z')+1):
        alpha[chr(num)]=num-65
    for n in name:
        answer+=min(alpha[n]-alpha['A'],26-alpha[n])
    
    check=[]
    for idx,n in enumerate(name):
        if n!='A':
            check.append(idx)
    
    cnt=ans=0
    while check:
        if cnt in check:
            check.remove(cnt)
        check.sort(key=lambda x: (min(abs(cnt-x),len(name)-abs(cnt-x)),x),reverse=True)
        ans+=min(abs(cnt-check[-1]),len(name)-abs(cnt-check[-1]))
        cnt=check.pop()
    
    return answer+ans
