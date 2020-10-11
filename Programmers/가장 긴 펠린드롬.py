def solution(s):
    for num in range(len(s),1,-1):
        for i in range(len(s)-num+1):
            check=s[i:i+num]
            N=len(check)-1
            for n in range(len(check)//2):
                if check[n]!=check[N-n]:
                    break
            else:
                return num
    else:
        return 1
