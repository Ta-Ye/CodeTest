def change(num,n,number):
    answer=[]
    while num>0:
        num,last=divmod(num,n)
        answer=[number[last]]+answer
    return answer

def solution(n, t, m, p):
    answer=['0']
    number=[str(i) for i in range(10)]+[chr(i) for i in range(ord('A'),ord('G'))]
    cnt=1
    while len(answer)<t*m:
        answer+=change(cnt,n,number)
        cnt+=1
    
    if m==p:
        return "".join([i for idx,i in enumerate(answer) if (idx+1)%m==0])[:t]
    else:
        return "".join([i for idx,i in enumerate(answer) if (idx+1)%m==p])[:t]
