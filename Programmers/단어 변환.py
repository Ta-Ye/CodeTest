import queue
def solution(begin, target, words):
    if not target in words:
        return 0
    answer=dict()
    for word in words:
        answer[word]=10**9
    q=queue.Queue()
    q.put(begin)
    answer[begin]=0
    while q.qsize():
        ck=q.get()
        for idx, word in enumerate(words):
            cnt=0
            for n in range(len(ck)):
                if ck[n]!=word[n]:
                    cnt+=1
            if cnt==1 and answer[word]>answer[ck]+1:
                answer[word]=answer[ck]+1
                q.put(word)
    
    return answer[target] if answer[target]<10**9 else 0
