def solution(jobs):
    N=len(jobs)
    ck=answer=0
    jobs.sort(key= lambda x: x[1])
    while jobs:
        for idx, job in jobs:
            if idx<=ck:
                answer+=ck+job-idx
                ck+=job
                jobs.remove([idx,job])
                break
        else:
            ck+=1
    return answer//N
