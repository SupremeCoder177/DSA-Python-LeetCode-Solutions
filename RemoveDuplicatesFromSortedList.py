from typing import Optional


class ListNode:

    def __init__(self, val = 0, _next = None):
        self.val = val
        self.next = _next


class Solution:

    def deleteDuplicates(self, head : Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        curr_node = head
        out_node = ListNode(val = curr_node.val)
        dummy = ListNode()
        dummy.next = out_node
        last_val = curr_node.val

        while curr_node:
            curr_node = curr_node.next
            if not curr_node: break
            if curr_node.val != last_val:
                out_node.next = ListNode(val = curr_node.val)
                last_val = curr_node.val
                out_node = out_node.next
            print(f'Current node val : {curr_node.val}, Out Node val : {out_node.val}')

        return dummy.next
        
        
            
    

a = ListNode(3)
b = ListNode(3, a)
c = ListNode(2, b)
d = ListNode(1, c)
e = ListNode(1, d)

node = Solution().deleteDuplicates(e)

while node:
    print(node.val)
    node = node.next