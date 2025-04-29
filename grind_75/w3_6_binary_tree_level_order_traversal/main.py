# 需要先寫一個把List轉換成Tree的function
# 概念上是loop從List的頭到尾, 當下的node可以利用下列公式找到parent
# left child i為奇數, parent index = (i-1)//2
# right child i為偶數, parent index = (i-2)//2
# 把List走完就可以把所有child與parent關聯

# 列出tree每層的node value
# 利用List放入這層的所有node, 取出各自的值放進結果,
# 並且把所有node的child放進下層node List
# 當下層node List無內容則停止迴圈


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level_nodes = []
        
        if root is not None:
            nodes_value = []
            nodes_value.append(root.val)
            result.append(nodes_value)

            if root.left is not None:
                level_nodes.append(root.left)
            if root.right is not None:
                level_nodes.append(root.right)

            while len(level_nodes) > 0:
                nodes_value = []
                next_level_nodes = []
                for node in level_nodes:
                    nodes_value.append(node.val)
                    if node.left is not None and node.left.val is not None:
                        next_level_nodes.append(node.left)
                    if node.right is not None and node.right.val is not None:
                        next_level_nodes.append(node.right)
                level_nodes = next_level_nodes
                result.append(nodes_value)

        return result

    def create_tree(self, tree_list: List[int]) -> TreeNode:
        root = TreeNode()
        root.val = tree_list[0]
        nodes: List[TreeNode] = []
        nodes.append(root)

        for i in range(1, len(tree_list)):
            node = TreeNode()
            node.val = tree_list[i]
            nodes.append(node)

            root_index = None
            #left node
            if i % 2 == 1:
                root_index = (i-1)//2
                root = nodes[root_index]
                root.left = node
            #right node
            elif i % 2 == 0:
                root_index = (i-2)//2
                root = nodes[root_index]
                root.right = node
            i+=1            

        return nodes[0]

def main():
    tree = [3,9,20,None,None,15,7]   
    
    solution = Solution()
    root = solution.create_tree(tree)
    result = solution.levelOrder(root)
    print(result)

if __name__ == "__main__":
    main()