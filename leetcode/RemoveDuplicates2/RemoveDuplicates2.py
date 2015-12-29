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
    
    
    if head == None:
        return None
            
    prevNode = head
    currNode = head
    nextNode = head.next

    returnHead = head

    while currNode != None and currNode.next != None:

        didRemove = False

#            print "Starting iteration"
#            print "    prevNode: %d" % (prevNode.val)
#            print "    currNode: %d" % (currNode.val)
#            print "    nextNode: %d" % (nextNode.val)

        while currNode.val == nextNode.val:
            didRemove = True
            if(nextNode.next == None):
                currNode.next = None
                nextNode = None
                break
            else:
                currNode.next = nextNode.next
                nextNode = currNode.next
                print "removed"
                    
        print "Post Removal"
        if not prevNode == None:
            print "    prevNode: %d" % (prevNode.val)
        else:
            print "    prevNode: None"
                
        if not currNode == None:
            print "    currNode: %d" % (currNode.val)
        else:
            print "    currNode: None"
                
        if not nextNode == None:
            print "    nextNode: %d" % (currNode.next.val)
        else:
            print "    nextNode: None"

        if currNode == head:
            returnHead = currNode.next
            prevNode = returnHead
            currNode = returnHead
            if not currNode == None:
                nextNode = currNode.next
        elif didRemove == True:
            if not currNode == None:
                if currNode.next == None:
                    prevNode.next = None
                else:
                    prevNode.next = currNode.next
                    currNode = prevNode.next
                    nextNode = currNode.next
        else:
            if not currNode == None:
                if not nextNode.next == None:
                    prevNode = currNode
                    currNode = currNode.next
                    nextNode = currNode.next

    return returnHead
        

lst = [1, 2, 3]
node = ListNode(None)
head = node
for e in lst:

    if node.val == None:
        node.val = e
    else:
        node.next = ListNode(e)
        node = node.next

node = head
while(node != None):
    print node.val
    node = node.next

print "Now Removing"
head = deleteDuplicates(head)
node = head
while(node != None):
    print node.val
    node = node.next
