def solution(land):
    for x in range(1,len(land)):
        for y in range(len(land[0])):
            land[x][y]+=max([i for idx,i in enumerate(land[x-1]) if idx!=y])
    return max(land[-1])
