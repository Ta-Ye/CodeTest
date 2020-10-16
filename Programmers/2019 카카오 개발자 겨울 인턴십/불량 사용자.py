answer=set()
def check(num,ck,ans):
    if num==len(ans):
        ck=sorted(list(set(ck)))
        if len(ck)==len(ans):
            answer.add(tuple(ck))
        return
    for i in ans[num]:
        if not i in list(ck):
            check(num+1,ck+[i],ans)
        
def solution(user_id, banned_id):
    ans=[[] for _ in range(len(banned_id))]
    
    for idx,name in enumerate(banned_id):
        for user in user_id:
            if len(name)!=len(user):
                continue
            for n in range(len(name)):
                if name[n]!='*' and name[n]!=user[n]:
                    break
            else:
                ans[idx].append(user)
                
    check(0,[],ans)
    return len(answer)
