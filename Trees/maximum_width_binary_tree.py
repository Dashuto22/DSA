import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_width(self, root):

        res = 0
        q = collections.deque([[root,1,0]])

        prevnum, prevlevel = 1, 0

