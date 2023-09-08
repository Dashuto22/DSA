import collections


class TreeNode:
    def __init__(self, val=0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_width_binary_tree(self, root):
        res = 0
        q = collections.deque([[root,1,0]])

        prevnum, prevlevel = 1,0

        while q:
            node, num, level =q.popleft()

            if level > prevlevel:
                prevlevel = level
                prevnum = num

            res = max(res, num- prevnum +1)

            if node.left:
                q.append([node.left, 2*num, level +1])

            if node.right:
                q.append([node.right, 2*num+1, level+1])

        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)


    solution = Solution()

    val = solution.max_width_binary_tree(root)

    print(val)


