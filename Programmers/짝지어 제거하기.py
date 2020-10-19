def solution(s):
    ck=[]
    for idx in range(len(s)):
        if ck and ck[-1]==s[idx]:
            ck.pop()
        else:
            ck.append(s[idx])
    return 0 if ck else 1
