class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):
        st = []
        res = []
        cur = root

        while cur or st:
            if cur:
                res.append(cur.val)
                st.append(cur.right)
                cur = cur.left
            else:
                cur = st.pop()
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    solution = Solution()

    res = solution.preorder(root)

    print(res)
