def unique_length_three_palindromic_subseq(s):
    res = set()
    left = set()
    right = {}


    for i in range(len(s)):
        right[s[i]] = 1 + right.get(s[i], 0)

    for i in range(len(s)):
        right[s[i]] -= 1
        if right[s[i]] == 0:
            right.pop(s[i])

        for j in range(26):
            c = chr(ord('a') + j)
            if c in left and c in right:
                res.add((s[i],c))

        left.add(s[i])

    return len(res)


if __name__ == '__main__':
    s = "aabca"
    val = unique_length_three_palindromic_subseq(s)

    print(val)