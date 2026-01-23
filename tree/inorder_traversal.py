
class Solution(object):
    def inorderTraversal(self, root):
        r = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            r.append(node.val)
            dfs(node.right)
        dfs(root)
        return r
        
