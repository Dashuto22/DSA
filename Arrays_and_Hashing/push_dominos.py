import collections


def push_dominoes(dominoes):
    dominos = list(dominoes)
    q = collections.deque()

    for i,d in enumerate(dominos):
        if d!=".":
            q.append((i,d))

    while q:
        i,d = q.popleft()
        if d =="L":
            if i>0 and dominos[i-1]==".":
                q.append((i-1,"L"))
                dominos[i-1]="L"
        if d =="R":
            if i+1 < len(dominos) and dominos[i+1]==".":
                if i+2 < len(dominos) and dominos[i+2]=="L":
                    q.popleft()
                else:
                    q.append((i+1,"R"))
                    dominos[i+1]="R"

    return "".join(dominos)




