class Solution:
    def min_time_collect(self, n, edges, hasApple):

        adj = {i:[] for i in range(n)}

        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)


        def dfs(cur, par):
            time = 0

            for child in adj[cur]:
                if child ==par:
                    continue

                childtime =  dfs(child, cur)
                if childtime or hasApple[child]:
                    time += childtime +2

            return time

        return dfs(0, -1)

if __name__ == '__main__':
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple = [False, False, True, False, True, True,False]

    sol = Solution()
    res = sol.min_time_collect(n,edges,hasApple)

    print(res)


