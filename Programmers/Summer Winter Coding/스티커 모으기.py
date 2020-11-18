def solution(sticker):
    answer=0
    if len(sticker)<=3:
        return max(sticker)
    
    ck=[0]*len(sticker)
    ck[1]=sticker[1]
    ck[2]=sticker[2]
    for i in range(3,len(sticker)):
        ck[i]=sticker[i]+max(ck[i-2],ck[i-3])
    answer=max(ck)
    
    ck=[0]*len(sticker)
    ck[0]=sticker[0]
    ck[2]=sticker[0]+sticker[2]
    for i in range(3,len(sticker)-1):
        ck[i]=sticker[i]+max(ck[i-2],ck[i-3])
    ans=max(ck)
    answer=max(ans,answer)
    return answer
