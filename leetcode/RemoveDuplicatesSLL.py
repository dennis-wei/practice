# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
        
    currNode = head
    nextNode = head.next
        
    while currNode.next != None:
    	if currNode.val == nextNode.val:
    		currNode.next = nextNode.next
    		nextNode = currNode.next
    	else:
    		currNode = currNode.next
    		nextNode = currNode.next
    return head

lst = [1, 2, 3, 3]
head = ListNode(1)
node = head
for e in lst:
	newnode = ListNode(e)
	node.next = newnode
	node = newnode

node = head
while(node != None):
	print node.val
	node = node.next

head = deleteDuplicates(head)
node = head
while(node != None):
	print node.val
	node = node.next
