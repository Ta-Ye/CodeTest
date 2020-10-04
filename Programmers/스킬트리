def solution(skill, skill_trees):
    answer = 0
    s=dict()
    for skill_tree in skill_trees:
        for i in skill:
            s[i]=100
        for idx,tree in enumerate(skill_tree):
            if tree in s:
                s[tree]=idx
        check=[s[i] for i in skill]
        if check==sorted(check):
            answer+=1
    return answer
