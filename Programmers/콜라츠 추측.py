def solution(num):
    cnt=0
    while num>1 and cnt<=500:
        if num%2==0:
            num//=2
        else:
            num=num*3+1
        cnt+=1
    return cnt if cnt<=500 else -1
