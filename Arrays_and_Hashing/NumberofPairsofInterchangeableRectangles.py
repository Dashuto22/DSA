def num_pairs_interchangeable_rect(recs):
    cuntmap ={}

    for w,h in recs:
        cuntmap[w/h] = 1 + cuntmap.get(w/h, 0)

    res = 0
    for c in cuntmap.values():
        if c > 1:
            res += c*(c-1)//2

    return res


if __name__ == '__main__':
    rects =  [[4,8],[3,6],[10,20],[15,30]]
    val = num_pairs_interchangeable_rect(rects)

    print(val)