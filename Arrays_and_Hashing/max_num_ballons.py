def max_balloons(st):
    counttext = {}

    for i in range(len(st)):
        counttext[st[i]] =  1 +counttext.get(st[i], 0)

    b  = "balloon"
    countBalloon = {}
    for i in range(len(b)):
        countBalloon[b[i]] = 1 + countBalloon.get(b[i], 0)

    res = len(st)

    for c in countBalloon:
        res = min(res, counttext.get(c,0)// countBalloon[c])

    return res

if __name__ == '__main__':
    text = "nlaebolko"
    val = max_balloons(text)
    print(val)