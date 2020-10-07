from itertools import product
def solution(numbers, target):
    answer = 0
    for pro in product([1,-1],repeat=len(numbers)):
        if sum([pro[i]*numbers[i] for i in range(len(numbers))])==target:
            answer+=1
    return answer
