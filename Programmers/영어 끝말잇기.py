def solution(n, words):
    ck=words[0][0]
    already=[]
    for idx, word in enumerate(words):
        if word[0]!=ck or word in already:
            break
        ck=word[-1]
        already.append(word)
    else:
        return [0,0]
    
    return [(idx+1)%n, 1+(idx+1)//n] if (idx+1)%n!=0 else [n, (idx+1)//n]
