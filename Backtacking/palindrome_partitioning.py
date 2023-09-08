def palindrome_partition(s):
    res = []
    part = []

    def isPali(s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l, r =l+1, r-1
        return True

    def build(i):
        if i >= len(s):
            res.append(part[:])
            return

        for j in range(i, len(s)):
            if isPali(s,i,j):
                part.append(s[i:j+1])
                build(j+1)
                part.pop()

    build(0)

    return res

if __name__ == '__main__':
    s= "aab"
    val = palindrome_partition(s)
    print(val)