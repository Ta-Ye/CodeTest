def solution(answers):
    answer = []
    giveup1=[1,2,3,4,5]*2000
    giveup2=[2,1,2,3,2,4,2,5]*1250
    giveup3=[3,3,1,1,2,2,4,4,5,5]*1000
    ck=[0,0,0]
    for idx,ans in enumerate(answers):
        if ans==giveup1[idx]:
            ck[0]+=1
        if ans==giveup2[idx]:
            ck[1]+=1
        if ans==giveup3[idx]:
            ck[2]+=1
    
    for idx, i in enumerate(ck):
        if i==max(ck):
            answer.append(idx+1)
    return answer
