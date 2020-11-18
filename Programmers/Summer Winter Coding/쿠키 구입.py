def solution(cookie):
    answer=0
    for idx in range(len(cookie)-1):
        start,end = idx, idx+1
        yb, ob = cookie[start], cookie[end]
        while True:
            if yb<ob:
                start-=1
                if start<0:
                    break
                yb+=cookie[start]
            elif yb>ob:
                end+=1
                if end>=len(cookie):
                    break
                ob+=cookie[end]
            else:
                answer = max(answer,yb)
                end+=1
                start-=1
                if end>=len(cookie) or start<0:
                    break
                ob+=cookie[end]
                yb+=cookie[start]
                
    return answer
