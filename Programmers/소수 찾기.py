from itertools import permutations as pers
def solution(numbers):
    ans=[]
    for num in range(1,len(numbers)+1):
        for per in pers(numbers,num):
            ans.append(int(''.join(per)))
    ans=list(set(ans))
    
    check=[1]*(max(ans)+1)
    check[0],check[1]=0,0
    for i in range(2,len(check)//2):
        if check[i]==0:
            continue
        n=2
        while n*i<len(check):
            check[n*i]=0
            n+=1
            
    answer=0
    for i in ans:
        if check[i]:
            answer+=1
    return answer
