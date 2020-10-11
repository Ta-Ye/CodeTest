class Node:
    def __init__(self,item):
        self.item=item
        self.num=dict()
        self.child=[]
        
def solution(words, queries):
    f_head=Node('')
    b_head=Node('')
    for word in words:
        ck=f_head
        for spell in word:
            if len(word) in ck.num:
                ck.num[len(word)]+=1
            else:
                ck.num[len(word)]=1
            for i in ck.child:
                if spell==i.item:
                    ck=i
                    break
            else:
                new_node=Node(spell)
                ck.child.append(new_node)
                ck=new_node
                
        ck=b_head
        for spell in reversed(word):
            if len(word) in ck.num:
                ck.num[len(word)]+=1
            else:
                ck.num[len(word)]=1
            for i in ck.child:
                if spell==i.item:
                    ck=i
                    break
            else:
                new_node=Node(spell)
                ck.child.append(new_node)
                ck=new_node
    
    result=[]
    for query in queries:
        query=list(query)
        if query[0]=='?':
            ck=b_head
            query=list(reversed(query))
        else:
            ck=f_head
        for spell in query:
            if spell=='?':
                if len(query) in ck.num:
                    result.append(ck.num[len(query)])
                else:
                    result.append(0)
                break
            for i in ck.child:
                if spell==i.item:
                    ck=i
                    break
            else:
                result.append(0)
                break
        
    return result
