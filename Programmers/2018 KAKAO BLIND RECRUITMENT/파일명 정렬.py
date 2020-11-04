import re
def solution(files):
    newfiles=[re.findall("([^0-9]+)([0-9]+)(.+)?",file.lower())+[idx] for idx,file in enumerate(files)]
    return [files[idx] for a,idx in sorted(newfiles,key=lambda x: (x[0][0],int(x[0][1])))]
