import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def time_needed(self,n,headID, manager, informTime):
        adj = collections.defaultdict(list)

        for i in range(n):
            adj[manager[i]].append(i)

        q = collections.deque([(headID,0)])
        res = 0

        while q:
            id, time = q.popleft()
            res = max(res, time)
            for emp in adj[id]:
                q.append((emp, time+ informTime[id]))

        return res

if __name__ == '__main__':
    n = 6
    headID = 2
    manager = [2, 2, -1, 2, 2, 2]
    informTime = [0, 0, 1, 0, 0, 0]

    solution = Solution()
    val = solution.time_needed(n, headID, manager, informTime)

    print(val)
