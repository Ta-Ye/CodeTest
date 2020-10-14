def solution(s):
    ck=0
    for i in s:
        ck= ck+1 if i=='(' else ck-1
        if ck<0:
            return False
    else:
        return False if ck else True
