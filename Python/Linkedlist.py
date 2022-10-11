# Python program to demonstrate circular linked list traversal

# Structure for a Node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	
	# Constructor to create a empty circular linked list
	def __init__(self):
		self.head = None

	# Function to insert a node at the beginning of a
	# circular linked list
	def push(self, data):
		ptr_first = Node(data)
		temp = self.head
		
		ptr_first.next = self.head

		# If linked list is not None then set the next of
		# last node
		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = ptr_first

		else:
			ptr_first.next = ptr_first # For the first node

		self.head = ptr_first

	# Function to print nodes in a given circular linked list
	def printList(self):
		temp = self.head
		if self.head is not None:
			while(True):
				print (temp.data, end=" ")
				temp = temp.next
				if (temp == self.head):
					break


# Driver program to test above function

# Initialize list as empty
clist = CircularLinkedList()

# Created linked list will be 11->2->56->12
clist.push(12)
clist.push(56)
clist.push(2)
clist.push(11)

print ("Contents of circular Linked List")
clist.printList()
		
