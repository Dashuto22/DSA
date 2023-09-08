import collections


def name_a_company(ideas):
    wordmap = collections.defaultdict(set)

    for i in ideas:
        wordmap[i[0]].add(i[1:])

    res = 0
    for ch1 in wordmap:
        for ch2 in wordmap:
            if ch1 == ch2:
                continue

            intersect = 0
            for w in wordmap[ch1]:
                if w in wordmap[ch2]:
                    intersect += 1

            distinct1 = len(wordmap[ch1]) - intersect
            distinct2 = len(wordmap[ch2]) - intersect

            res += distinct2 * distinct1

    return res



if __name__ == '__main__':
    ideas = ["coffee", "donuts", "time", "toffee"]
    val = name_a_company(ideas)
    print(val)
