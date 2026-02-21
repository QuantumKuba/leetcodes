# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def help(cur):
            if not cur: return 0
            
            curL = help(cur.left)
            curR = help(cur.right)

            if curL == -1 or curR == -1: return -1

            if abs(curL - curR) > 1: return -1
            return 1 + max(curL, curR)

        return True if help(root) != -1 else False


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.isBalanced(root))

