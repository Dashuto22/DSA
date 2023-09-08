class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def house_robber(self, root):
        def dfs(node):
            if not node:
                return [0,0]

            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            withRoot = node.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)
            return [withRoot, withoutRoot]

        return max(dfs(root))

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(1)
    root.left.right = TreeNode(3)

    sol = Solution()
    res = sol.house_robber(root)

    print(res)