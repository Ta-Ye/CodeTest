def solution(n):
    answer=[]
    ans=[[0]*i for i in range(1,n+1)]
    ck=0
    for i in ans:
        ck+=len(i)
        
    cnt=0
    x=y=0
    n1=n
    while cnt!=ck:
        for i in range(x,n):
            cnt+=1
            ans[i][y]=cnt
        for j in range(y+1,n1):
            cnt+=1
            ans[i][j]=cnt
        for k in range(n-2,x,-1):
            j-=1
            cnt+=1
            ans[k][j]=cnt
        x+=2
        y+=1
        n-=1
        n1-=2
    for i in ans:
        for j in i:
            answer.append(j)
    return answer
