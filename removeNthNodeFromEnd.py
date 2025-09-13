# remove nth node from LinkedList

from typing import Optional

class ListNode:

	def __init__(self, val = 0, next_ = None):
		self.val = val
		self.next = next_


class Solution:

	def removeNthFromEnd(self, head : Optional[ListNode], n : int) -> Optional[ListNode]:
		if not head: return None
		if not head.next: return None

		length = 0
		curr_node = head
		while curr_node:
			curr_node = curr_node.next
			length += 1
		
		count = 0
		curr_node = head
		prev_node = None
		
		while curr_node:
			prev_node = curr_node
			curr_node = curr_node.next
			count += 1

			if count == length - n:
				prev_node.next = curr_node.next
				break

		return head



a = ListNode(40)
b = ListNode(30, a)
c = ListNode(20, b)
d = ListNode(10, c)


node = Solution().removeNthFromEnd(d, 2)

while node:
	print(node.val)
	node = node.next