def letter_combs(s):

    res = []
    digitToChar = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
    }

    def backtrack(i, cur):
        if len(cur)== len(s):
            res.append(cur)
            return

        for c in digitToChar[s[i]]:
            backtrack(i+1, cur+c)

    if s:
        backtrack(0,"")

    return res



if __name__ == '__main__':
    digits = "23"
    val = letter_combs(digits)
    print(val)