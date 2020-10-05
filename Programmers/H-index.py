def solution(citations):
    if max(citations)==0:
        return 0
    n=len(citations)
    answer = 0
    citations.sort(reverse=True)
    while citations and n>answer:
        answer=citations.pop()
        n=len(citations)+1
    return n
