# add two numbers

class ListNode:

	def __init__(self, val=0, next_=None):
		self.val = val
		self.next = next_


def addTwoNumbers(list1 : ListNode, list2 : ListNode) -> ListNode:
	num1 = turnToInt(list1, reverse=True)
	num2 = turnToInt(list2, reverse=True)
	return turnToList(num1 + num2)
	
def turnToInt(list_ : ListNode, reverse=False) -> int:
	num = ""
	node = list_
	while node.next:
		num += str(node.val)
		node = node.next
		if not node.next: num += str(node.val)
	if reverse:
		num = reversed(num)
	return int(''.join(ch for ch in num))

def turnToList(num : int, reverse=False) -> ListNode:
	lastNode = None
	temp = str(num) if not reverse else reversed(str(num))
	for ch in temp:
		node = ListNode(int(ch), lastNode)
		lastNode = node
	return lastNode
		

num3 = ListNode(3, None)
num2 = ListNode(4, num3)
num1 = ListNode(2, num2)

num3_ = ListNode(4, None)
num2_ = ListNode(6, num3_)
num1_ = ListNode(5, num2_)

print(turnToInt(addTwoNumbers(num1, num1_)))
# chatgpt solution (aka the optimized one)

def addTwoNumbers(l1 : ListNode, l2 : ListNode) -> ListNode:
	dummy = ListNode(0)
	current, carry = dummy, 0

	while l1 or l2 or carry:
		val1 = l1.val if l1 else 0
		val2 = l2.val if l2 else 0

		total = val1 + val2 + carry
		carry = total // 10

		current.next = ListNode(total % 10)
		current = current.next

		if l1: l1 = l1.next
		if l2: l2 = l2.next

	return dummy.next
