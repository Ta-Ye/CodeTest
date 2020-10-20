from itertools import combinations as coms
def solution(nums):
    check=[1]*3001
    check[:2]=[0,0]
    for i in range(2,3001):
        if check[i]==0:
            continue
        for j in range(2*i,3001,i):
            check[j]=0
    
    return sum([check[sum(com)] for com in coms(nums,3)])
