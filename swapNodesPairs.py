# swap list nodes

from typing import Optional

class ListNode:

	def __init__(self, val = 0, next_ = None):
		self.val = val
		self.next = next_


class Solution:
	def swapPairs(self, head : Optional[ListNode]) -> Optional[ListNode]:
		if not head: return None
		if not head.next: return head

		curr_node = head # points to the first node
		next_node = head.next # points to the 2nd node
		return_node = next_node # points to the start

		while curr_node.next:
			temp = next_node.next # points to the 3rd node now

			# interchanging nodes
			next_node.next = curr_node
			curr_node.next = temp

			if temp:
				if temp.next:
					curr_node.next = temp.next
					curr_node = temp
					next_node = temp.next
				else: break

		return return_node


a = ListNode(40)
b = ListNode(30, a)
c = ListNode(20, b)
d = ListNode(10, c)

node = Solution().swapPairs(d)
while node:
	print(node.val)
	node = node.next
