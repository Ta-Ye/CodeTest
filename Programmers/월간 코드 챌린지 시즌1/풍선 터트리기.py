def solution(a):
    if len(a)<=2:
        return len(a)
    
    ck_left=[i for i in a]
    ck_right=[i for i in a]
    for idx in range(1,len(a)):
        if ck_left[idx]>ck_left[idx-1]:
            ck_left[idx]=ck_left[idx-1]
    for idx in range(len(a)-2,-1,-1):
        if ck_right[idx]>ck_right[idx+1]:
            ck_right[idx]=ck_right[idx+1]
            
    answer=2
    for idx in range(1,len(a)-1):
        if a[idx]<=ck_left[idx-1] or a[idx]<=ck_right[idx+1]:
            answer+=1
    
    return answer
