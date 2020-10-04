def solution(participant, completion):
    ans=dict()
    for maratoner in participant:
        if maratoner in ans:
            ans[maratoner]-=1
        else:
            ans[maratoner]=-1
    
    for maratoner in completion:
        ans[maratoner]+=1
    
    for maratoner in ans:
        if ans[maratoner]<0:
            return maratonerd
