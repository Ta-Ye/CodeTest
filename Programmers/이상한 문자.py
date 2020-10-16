def solution(s):
    answer=''
    cnt=0
    for i in s:
        if i==' ':
            cnt=0
            answer+=' '
            continue
        answer+=i.upper() if cnt%2==0 else i.lower()
        cnt+=1
    return answer
