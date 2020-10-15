def solution(s):
    if not len(s) in [4,6]:
        return False
    for i in s:
        if not i.isdigit():
            return False
    return True
