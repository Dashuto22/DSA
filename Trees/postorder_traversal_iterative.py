class TreeNode:
    def __init__(self, val=0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def postorder(self, root):

        st = [root]
        res = []
        visit = [False]

        while st:
            cur, v = st.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)

                else:
                    st.append(cur)
                    visit.append(True)

                    st.append(cur.right)
                    visit.append(False)

                    st.append(cur.left)
                    visit.append(False)
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    res = solution.postorder(root)

    print(res)