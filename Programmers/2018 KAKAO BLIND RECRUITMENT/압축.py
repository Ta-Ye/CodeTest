def solution(msg):
    answer=[]
    LZW={chr(i):i-64 for i in range(ord("A"),ord("Z")+1)}
    cnt=27
    idx=0
    while idx<len(msg):
        for i in range(idx,len(msg)):
            if not msg[idx:i+1] in LZW:
                LZW[msg[idx:i+1]]=cnt
                cnt+=1
                answer.append(LZW[msg[idx:i]])
                break
        else:
            answer.append(LZW[msg[idx:i+1]])
            break
        idx=i
    return answer
