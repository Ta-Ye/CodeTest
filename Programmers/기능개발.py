def solution(progresses, speeds):
    answer = []
    cnt=0
    progresses.reverse()
    speeds.reverse()
    while progresses:
        speed=speeds.pop()
        a,b=divmod(100-progresses.pop()-cnt*speed,speed)
        cnt+=a if b==0 else a+1
        answer.append(1)
        while progresses and progresses[-1]+cnt*speeds[-1]>=100:
            progresses.pop()
            speeds.pop()
            answer[-1]+=1
    return answer
