def depart(w):
    cnt1=cnt2=0
    u=''
    for idx in range(len(w)):
        u+=w[idx]
        if w[idx]=='(':
            cnt1+=1
        else:
            cnt2+=1
        if cnt1==cnt2:
            return u,w[idx+1:]

def reverse(w):
    ans=''
    for i in w:
        ans+=')' if i=='(' else '('
    return ans

def recursion(w):
    if w=='':
        return ''
    
    u,v=depart(w)
    if u[0]=='(':
        return u+recursion(v)
    else:
        v='('+recursion(v)+')'
        return v+reverse(u[1:-1])
    
def solution(p):
    return recursion(p)
