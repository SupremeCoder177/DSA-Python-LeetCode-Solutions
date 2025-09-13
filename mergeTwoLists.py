# sorted linked lists merger

class ListNode:
	def __init__(self, val=0, next_=None):
		self.val = val
		self.next = next_


def mergeTwoLists(list1 : ListNode, list2 : ListNode) -> ListNode:
	num_map = {}
	while list1 or list2:
		if list1:
			if num_map.get(list1.val, None):
				temp = num_map[list1.val]
				num_map[list1.val] = temp + 1
			else:
				num_map[list1.val] = 1

		if list2:
			if num_map.get(list2.val, None):
				temp = num_map[list2.val]
				num_map[list2.val] = temp + 1
			else:
				num_map[list2.val] = 1

		list1 = list1.next
		list2 = list2.next

	if not num_map: return []

	dummy = ListNode()
	node = ListNode()
	dummy.next = node
	temp = sorted(num_map.keys())
	i = 0
	while i < len(temp):
		val = temp[i]
		for j in range(num_map[val]):
			node.val = val
			node_ = ListNode()
			if i == len(temp) - 1 and j == num_map[val] - 1:
				break
			node.next = node_
			node = node_
		i += 1

	return dummy.next


def printList(s : ListNode):
	temp = []
	while s:
		temp.append(s.val)
		s = s.next if s else None
	return temp


num3 = ListNode(val = 4)
num2 = ListNode(val = 2, next_ = num3)
num1 = ListNode(val = 1, next_ = num2)

num3_ = ListNode(val = 4)
num2_ = ListNode(val = 3, next_ = num3_)
num1_ = ListNode(val = 1, next_ = num2_)

print(printList(mergeTwoLists(num1, num1_)))