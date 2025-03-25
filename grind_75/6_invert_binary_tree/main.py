# DFS找到每個節點, 找到leaf node後, 再回到parent node左右反轉leaf node

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs_post_order(root)
        
    
    def dfs_post_order(self, node: Optional[TreeNode]):
        if node is None:
            return

        self.dfs_post_order(node.left)
        self.dfs_post_order(node.right)
        print(node.val)

    def set_binary_tree(self, nodes: List[int]) -> Optional[TreeNode]:
        if not nodes:
            return None

        parent_stack: List[TreeNode] = []  
        root = TreeNode(nodes[0])
        parent_stack.append(root)

        for index in range(1, len(nodes)):
            node = TreeNode(nodes[index])
            parent = parent_stack[0]

            if parent.left == None:
                parent.left = node            
            elif parent.right == None:
                parent.right = node
                parent_stack.pop(0)

            parent_stack.append(node)   

        return root     

def main():
    s = Solution()
    root = s.set_binary_tree([1,2,3,4,5,6,7])
    s.invertTree(root)

if __name__ == '__main__':
    main()