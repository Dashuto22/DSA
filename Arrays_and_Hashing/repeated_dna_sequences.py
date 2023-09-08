def repeated_dna_sequences(s):

    res, seen = set(), set()
    for i in range(len(s)-9):
        curstr = s[i:i+10]
        if curstr in seen:
            res.add(curstr)

        seen.add(curstr)
    return list(res)

if __name__ == '__main__':
    st = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    val = repeated_dna_sequences(st)
    print(val)