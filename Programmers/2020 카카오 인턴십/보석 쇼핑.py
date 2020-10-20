def solution(gems):
    ck=list(set(gems))
    pocket=dict()
    check,answer=[],[]
    num=0
    for idx,gem in enumerate(gems):
        if gem in pocket:
            pocket[gem]+=1
        else:
            pocket[gem]=1
        if check and check[num]==gem:
            while len(check)>num:
                if pocket[check[num]]==1:
                    break
                else:
                    pocket[check[num]]-=1
                    num+=1
        check.append(gem)
        if len(pocket)==len(ck):
            answer.append([num+1,len(check)])
    return sorted(answer,key=lambda x: x[1]-x[0])[0]
