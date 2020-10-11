def solution(arr):
    ck=-1
    answer=[]
    for num in arr:
        if num!=ck:
            answer.append(num)
            ck=num
    return answer
