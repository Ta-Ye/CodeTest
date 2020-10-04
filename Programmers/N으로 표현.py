def solution(N, number):
    answer = 0
    s=dict()
    s[1]=[N]
    if number in s[1]:
        return 1
    for num in range(2,9):
        s[num]=[]
        ck=N
        for a in range(1,num):
            ck+=N*(10**a)
        s[num].append(ck)
        
        for i in range(1,num):
            for ck1 in s[i]:
                for ck2 in s[num-i]:
                    s[num].append(ck1+ck2)
                    s[num].append(ck1-ck2)
                    s[num].append(ck2-ck1)
                    s[num].append(ck1*ck2)
                    if ck1!=0:
                        s[num].append(ck2/ck1)
                    if ck2!=0:
                        s[num].append(ck1/ck2)
        s[num]=list(set(s[num]))
        if number in s[num]:
            return num
    else:
        return -1
