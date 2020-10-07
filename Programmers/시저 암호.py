def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=' '
        elif ord(i)+n>ord('z'):
            answer+=str(chr((ord(i)+n)-ord('z')+ord('a')-1))
        elif ord(i)<ord('a') and ord(i)+n>ord('Z'):
            answer+=str(chr((ord(i)+n)-ord('Z')+ord('A')-1))
        else:
            answer+=str(chr(ord(i)+n))
    return answer
