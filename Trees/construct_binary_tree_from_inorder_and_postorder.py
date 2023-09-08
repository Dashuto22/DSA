class TreeNode:
    def __init(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

class Solution:

    def build_binary_tree_from_inorder_postorder(self, inorder, postorder):
        treeidx = {v:i for i,v in enumerate(inorder)}

        def build_tree(l,r):
            if l>r:
                return None
            root = TreeNode(postorder.pop())
            idx = treeidx[root.val]
            root.right = build_tree(idx+1,r)
            root.left = build_tree(l, idx-1)

            return root

        return build_tree(0, len(inorder)-1)

if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    sol = Solution()

    res = sol.build_binary_tree_from_inorder_postorder(inorder, postorder)

    print(res)