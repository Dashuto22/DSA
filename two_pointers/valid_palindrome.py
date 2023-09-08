def valid_palindrome(s):
    l,r = 0, len(s)-1

    def isAlphanum(c):

        return ( ord('a') <= ord(c)<= ord('z') or
                 ord('A') <= ord(c) <= ord('Z') or
                 ord('0') <= ord(c) <= ord('9'))

    while l < r:
        while l<r and not isAlphanum(s[l]):
            l += 1

        while r> l and not isAlphanum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l +=1
        r -= 1

    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    val = valid_palindrome(s)

    print(val)