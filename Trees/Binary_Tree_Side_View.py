import collections


class TreeNode:
    def __init__(self, val=0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_sideview(self, root):
        res = []

        q = collections.deque()
        if root:
            q.append(root)

        while q:
            qlen = len(q)
            rightside = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)

        return res




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)


    solution = Solution()

    res = solution.right_sideview(root)


    print(res)