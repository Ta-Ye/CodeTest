import re
def solution(word, pages):
    meta=re.compile('<meta property="og:url" content="(.*?)"/>')
    href=re.compile('<a href="(.*?)">')
    base_score,links=dict(),dict()
    
    for page in pages:
        my_url=meta.findall(page)[0]
        base_score[my_url]=re.sub("[^a-z]",".",page.lower()).split('.').count(word.lower())
        othre_url=href.findall(page)
        for url in othre_url:
            if url in links:
                links[url]+=base_score[my_url]/len(othre_url)
            else:
                links[url]=base_score[my_url]/len(othre_url)
    
    answer=[]
    for i in base_score:
        if i in links:
            answer.append(base_score[i]+links[i])
        else:
            answer.append(base_score[i])
    
    return answer.index(max(answer))
