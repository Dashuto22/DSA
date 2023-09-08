def min_swaps_make_string_balanced(s):
    extraclose, res = 0, 0

    for c in s:
        if c==']':
            extraclose += 1

        else:
            extraclose -= 1

        res = max(res, extraclose)

    return (res+1)//2


if __name__ == '__main__':
    s = "][]["
    swaps = min_swaps_make_string_balanced(s)
    print(swaps)