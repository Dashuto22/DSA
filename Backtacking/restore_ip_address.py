def restore_ip_address(s):
    if len(s) > 12:
        return []

    res = []
    def dfs(i, dots, curIP):
        if i==len(s) and dots==4:
            res.append(curIP[:-1])
            return

        if dots > 4:
            return

        for j in range(i, min(i+3, len(s))):
            if int(s[i:j+1]) < 256 and (i==j or s[i]!="0"):
                dfs(j+1, dots +1, curIP+ s[i:j+1] + ".")

    dfs(0,0, "")

    return res


if __name__ == '__main__':
    s = "25525511135"
    val = restore_ip_address(s)
    print(val)