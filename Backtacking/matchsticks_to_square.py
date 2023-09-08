def matchsticks_to_square(matchsticks):
    lenth = len(matchsticks)//4

    sides = [0] *4

    if len(matchsticks)/4 != lenth:
        return False

    matchsticks.sort(reverse=True)

    def backtrack(i):
        if i==len(matchsticks):
            return True

        for j in range(4):
            if sides[j] + matchsticks[i]<=lenth:
                sides[j] += matchsticks[i]
                if backtrack(i+1):
                    return True
                sides[j] -= matchsticks[i]

        return False

    return backtrack(0)

if __name__ == '__main__':
    matchsticks = [1, 1, 2, 2, 2]
    val = matchsticks_to_square(matchsticks)
    print(val)