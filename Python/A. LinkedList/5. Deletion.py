#Iterative Method to delete an element from the linked list:
'''
To delete a node from the linked list, we need to do the following steps:

    - Find the previous node of the node to be deleted. 
    - Change the next of the previous node. 
    - Free memory for the node to be deleted.
'''


# Python program to implement the above approach
class Node:
	# constructor to initialize the node object
	def __init__(self, data):
		self.number = data
		self.next = None


def push(head, A):
	n = Node(A)
	n.number = A
	n.next = head
	head = n
	return head


def deleteN(head, position):
	temp = head
	prev = head
	for i in range(0, position):
		if i == 0 and position == 1:
			head = head.next

		else:
			if i == position-1 and temp is not None:
				prev.next = temp.next
			else:
				prev = temp

				# Position was greater than
				# number of nodes in the list
				if prev is None:
					break
				temp = temp.next
	return head


def printList(head):
	while(head):
		if head.next == None:
			print("[", head.number, "] ", "[", hex(id(head)), "]->", "nil")
		else:
			print("[", head.number, "] ", "[", hex(
				id(head)), "]->", hex(id(head.next)))
		head = head.next
	print("")
	print("")


head = Node(0)
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)

printList(head)

# Delete any position from list
head = deleteN(head, 1)
printList(head)
#--------------------------------------------------------------------------------------------------------------------------------
#Recursive Method to delete a node from linked list:
'''
To delete a node of a linked list recursively we need to do the following steps:

    - We pass node* (node pointer) as a reference to the function (as in node* &head)
    - Now since the current node pointer is derived from the previous node’s next (which is passed by reference) so now if the value of the current node pointer is changed, the previous next node’s value also gets changed which is the required operation while deleting a node (i.e points previous node’s next to current node’s (containing key) next).
    - Find the node containing the given value.
    - Store this node to deallocate it later using the free() function.
    - Change this node pointer so that it points to its next and by performing this previous node’s next also gets properly linked.
    https://media.geeksforgeeks.org/wp-content/uploads/20210211175616/Untitleddesign.png
    
    '''
    
# Python program to delete a node in
# singly linked list recursively

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

# Deletes the node containing 'data'
# part as val and alter the head of
# the linked list (recursive method)
def deleteNode(head, val):
	# Check if list is empty or we
	# reach at the end of the
	# list.
	if (head == None):
		print("Element not present in the list")
		return -1
	# If current node is the
	# node to be deleted
	if (head.data == val):
		# If it's start of the node head
		# node points to second node
		if head.next: 
			head.data = head.next.data
			head.next = head.next.next
			return 1
		else: return 0
	if deleteNode(head.next, val) == 0:
		head.next = None
		return 1

# Utility function to add a
# node in the linked list
# Here we are passing head by
# reference thus no need to
# return it to the main function
def push(head, data):
	newNode = Node(data) 
	newNode.next = head 
	head = newNode 
	return head

# Utility function to print
# the linked list (recursive
# method)
def printLL(head):
	if (head == None):
		return
	temp = head
	while temp:
		print(temp.data,end=' ')
		temp = temp.next
	print()

# Driver Code

# Starting with an empty linked list
head = None
# Adds new element at the
# beginning of the list
head = push(head, 10) 
head = push(head, 12) 
head = push(head, 14) 
head = push(head, 15)
# original list
printLL(head) 
# Call to delete function
deleteNode(head, 20) 
# 20 is not present thus no change
# in the list
printLL(head) 
deleteNode(head, 10) 
printLL(head) 
deleteNode(head, 14) 
printLL(head)
