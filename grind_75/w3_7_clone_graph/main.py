# 先利用題目的neighbors array產生graph
# 先從頭到尾建立node, 並且放進新的array
# 第二輪從頭到尾, 取出每個node的neighbors index, 並且從node array中取出對應的node, 讓當下的node與它們關聯

# 先把第一個node放進existed_nodes裡, 也放進unchecked_nodes裡
# loop, 直到所有unchecked_nodes都確認過
# 每輪檢查uncheck_node的neighbors, uncheck_node放入的node是要copy的node
# current_node利用unchecked_node.val從existed_nodes中取得
# 如果已存在, 則從existed_nodes取出來, 作為current_node的neighbor,
# 如果不存在, 建立新的node, 放進existed_nodes, 作為當current_node的neighbor
# 如果unchecked_nodes中沒有當下neighbor.val, 則放入
# 只要沒有新的node.val就不會加入至unchecked_nodes中, 最後每輪從unchecked_nodes反覆確認neighbors, 就能走完整個graph

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
                
        existed_nodes = {}
        unchecked_nodes: List[Node] = []
        unchecked_nodes.append(node)
        new_node = Node()
        new_node.val = node.val
        new_graph:Optional[Node] = new_node
        existed_nodes[new_node.val] = new_node
        
        check_index = 0

        while check_index < len(unchecked_nodes):
            unchecked_node = unchecked_nodes[check_index]
            current_node = existed_nodes[unchecked_node.val]
                
            for neighbor in unchecked_node.neighbors:
                neighbor_node: Node = None
                if neighbor.val not in existed_nodes:
                    neighbor_node = Node()
                    neighbor_node.val = neighbor.val                    
                    existed_nodes[neighbor.val] = neighbor_node
                else:
                    neighbor_node = existed_nodes[neighbor.val]

                current_node.neighbors.append(neighbor_node)

                if all(node.val != neighbor.val for node in unchecked_nodes):
                    unchecked_nodes.append(neighbor)
            
            check_index+=1
                    
        return new_graph


    def create_graph(self, nodes: List[List[int]]) -> Optional['Node']:
        if len(nodes) == 0:
            return None
        
        node_objects: List[Node] = []
        
        index = 1
        for node_neighbors in nodes:
            node = Node()
            node.val = index
            node_objects.append(node)
            if len(node_neighbors) == 0:                
                return node
            
            index+=1
            
        index = 0
        for node_neighbors in nodes:
            node_object = node_objects[index]
            neighbor_objects = []
            for node_neighbor in node_neighbors:
                neighbor = node_objects[node_neighbor-1]
                neighbor_objects.append(neighbor)

            node_object.neighbors = neighbor_objects

            index+=1
        
        return node_objects[0]

def main():
    nodes = [[2,4],[1,3],[2,4],[1,3]]
    solution = Solution()
    graph = solution.create_graph(nodes)
    result = solution.cloneGraph(graph)

if __name__ == '__main__':
    main()