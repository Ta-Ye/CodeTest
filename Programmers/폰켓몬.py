def solution(nums):
    N=len(list(set(nums)))
    return len(nums)//2 if N>=len(nums)//2 else N
