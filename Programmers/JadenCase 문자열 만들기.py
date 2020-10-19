def solution(s):
    s=list(s)
    cnt=0
    for idx,i in enumerate(s):
        if i==' ':
            cnt=0
            continue
        if cnt==0:
            s[idx]=s[idx].upper()
        else:
            s[idx]=s[idx].lower()
        cnt+=1
    return ''.join(s)
