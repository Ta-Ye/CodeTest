def solution(arr):
    answer=1
    for num in arr:
        cnt=1
        while True:
            for x in range(2,max(answer,num)):
                if answer%x==0 and num%x==0:
                    answer//=x
                    num//=x
                    cnt*=x
                    break
            else:
                break
        answer*=num*cnt
    return answer
