import collections


class TreeNode:
    def __init__(self, val=0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_duplicate_subtree(self, root):

        subtrees = collections.defaultdict(list)
        res = []

        def dfs(node):
            if not node:
                return "null"
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(subtrees[s])==1:
                res.append(node)

            subtrees[s].append(node)

            return s

        dfs(root)

        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right.left.left = TreeNode(4)

    sol = Solution()

    res = sol.find_duplicate_subtree(root)

    print(res)


