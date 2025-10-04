from typing import Optional


class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p : Optional[TreeNode], q : Optional[TreeNode]) -> bool:

        if not p and q: return False
        if not q and p: return False
        if not p and not q: return True

        p_nodes = [p]
        q_nodes = [q]

        while True:
            all_None = True
            for i in range(len(p_nodes)):
                val1 = None 
                val2 = None
                if p_nodes[i]: 
                    val1 = p_nodes[i].val
                    all_None = False
                if q_nodes[i]: 
                    val2 = q_nodes[i].val
                    all_None = False

                if val1 != val2: return False

            if all_None: break

            old_p_nodes_end = len(p_nodes)
            old_q_nodes_end = len(q_nodes)
            
            temp = []
            for node in p_nodes:
                if node:
                    temp.append(node.left)    
                    temp.append(node.right)
                else:
                    temp.append(None)
                        
            p_nodes.extend(temp)
            p_nodes = p_nodes[old_p_nodes_end:]

            temp = []
            for node in q_nodes:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    temp.append(None)

            q_nodes.extend(temp)
            q_nodes = q_nodes[old_q_nodes_end:]
        return True


        
b = TreeNode(2)
c = TreeNode(1, left = None, right = b)

d = TreeNode(2)
f = TreeNode(1, left = d, right = None)

print(Solution().isSameTree(c, f))