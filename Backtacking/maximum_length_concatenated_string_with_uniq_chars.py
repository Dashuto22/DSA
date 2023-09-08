def max_length_uniq_chars(arr):
    charset = set()

    def overlap(charset,s):
        prev = set()
        for c in s:
            if c in charset or c in prev:
                return True
            prev.add(c)

        return False

    def backtrack(i):
        if i == len(arr):
            return len(charset)

        res = 0
        if not overlap(charset, arr[i]):
            for c in arr[i]:
                charset.add(c)
            res = backtrack(i+1)
            for c in arr[i]:
                charset.remove(c)

        return max(res, backtrack(i+1))

    return backtrack(0)

if __name__ == '__main__':
    arr = ["un", "iq", "ue"]
    val = max_length_uniq_chars(arr)
    print(val)