def solution(numbers):
    return str(int(''.join(sorted(list(map(str,numbers)),key=lambda x: (x*4),reverse=True))))
