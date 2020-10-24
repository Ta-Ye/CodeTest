import re
def solution(str1, str2):
    str1=re.sub('[^a-z]',' ',str1.lower())
    str2=re.sub('[^a-z]',' ',str2.lower())
    
    A=[str1[idx]+str1[idx+1] for idx in range(len(str1)-1) if not ' ' in str1[idx]+str1[idx+1]]
    B=[str2[idx]+str2[idx+1] for idx in range(len(str2)-1) if not ' ' in str2[idx]+str2[idx+1]]
    
    C,D=[],[]
    for s in A:
        if s in B:
            C.append(s)
            B.remove(s)
        D.append(s)
    D+=B
    return int(65536*len(C)/len(D)) if D else 65536
