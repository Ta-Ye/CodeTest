def solution(n, arr1, arr2):
    arr1=[str(bin(num)[2:]).zfill(n) for num in arr1]
    arr2=[str(bin(num)[2:]).zfill(n) for num in arr2]
    answer=[]
    for x in range(n):
        ck=''
        for y in range(n):
            ck+= '#' if arr1[x][y]=='1' or arr2[x][y]=='1' else ' '
        answer.append(ck)
    return answer
