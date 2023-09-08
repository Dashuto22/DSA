class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def all_possible_full_binary_trees(self, n):
        dp = {0:[], 1:[TreeNode()]}

        def backtrack(n):
            if n in dp:
                return dp[n]

            res = []
            for l in range(n):
                r = n-1-l
                leftTrees, rightTrees = backtrack(l), backtrack(n)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0,t1,t2))

            dp[n]=res

            return res
        return backtrack(n)