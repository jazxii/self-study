'''
Given a Linked List, the task is to insert a new node in this given Linked List at the following positions: 

At the front of the linked list  
After a given node. 
At the end of the linked list.
'''
#--------------------------------------------------------------------------------------------------------------------------------
#How to Insert a Node at the Front/Beginning of Linked List
'''
Approach: 

To insert a node at the start/beginning/front of a Linked List, we need to:

- Make the first node of Linked List linked to the new node
- Remove the head from the original first node of Linked List
- Make the new node as the Head of the Linked List.
https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist_insert_at_start.png
'''

# Node class
class Node:

	# Function to initialize the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize
						# next as null

# Linked List class
class LinkedList:
	
	# Function to initialize the Linked
	# List object
	def __init__(self):
		self.head = None

# This function is in LinkedList class
# Function to insert a new node at the beginning
def push(self, new_data):

	# 1 & 2: Allocate the Node &
	# Put in the data
	new_node = Node(new_data)

	# 3. Make next of new Node as head
	new_node.next = self.head

	# 4. Move the head to point to new Node
	self.head = new_node
 
#--------------------------------------------------------------------------------------------------------------------------------
#How to Insert a Node after a Given Node in Linked List

'''
Approach: 

To insert a node after a given node in a Linked List, we need to:

Check if the given node exists or not. 
If it do not exists, 
    terminate the process.
If the given node exists,
    = Make the element to be inserted as a new node
    = Change the next pointer of given node to the new node
    = Now shift the original next pointer of given node to the next pointer of new node
    https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist_insert_middle.png
'''
# This function is in LinkedList class.
# Inserts a new node after the given prev_node. This method is
# defined inside LinkedList class shown above */
def insertAfter(self, prev_node, new_data):

	# 1. check if the given prev_node exists
	if prev_node is None:
		print("The given previous node must inLinkedList.")
		return

	# 2. Create new node &
	# 3. Put in the data
	new_node = Node(new_data)

	# 4. Make next of new Node as next of prev_node
	new_node.next = prev_node.next

	# 5. make next of prev_node as new_node
	prev_node.next = new_node

#--------------------------------------------------------------------------------------------------------------------------------
#How to Insert a Node at the End of Linked List
'''
To insert a node at the end of a Linked List, we need to:

- Go to the last node of the Linked List
- Change the next pointer of last node from NULL to the new node
- Make the next pointer of new node as NULL to show the end of Linked List
https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist_insert_last.png
'''
# This function is defined in Linked List class
# Appends a new node at the end. This method is
# defined inside LinkedList class shown above
def append(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next = new_node

