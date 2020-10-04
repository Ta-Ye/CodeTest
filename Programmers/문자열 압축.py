def depart(num, s):
    new_s=[]
    n=0
    for i in range(len(s)//num):
        new_s.append(s[num*i:num*(i+1)])
    if num*(i+1)<len(s):
        new_s.append(s[num*(i+1):])
    new_s.append('')
    ans=''
    cnt=0
    ck=new_s[0]
    for idx, ch in enumerate(new_s):
        if ch==ck:
            cnt+=1
        else:
            ans+=str(cnt)+ck if cnt>=2 else ck 
            cnt=1
            ck=ch
    return len(ans)

def solution(s):
    answer=len(s)
    for num in range(1, len(s)//2+1):
        answer=min(answer,depart(num,s))
    return answer
