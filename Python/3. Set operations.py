# Python set is a mutable collection of data that does not allow any duplication. 
# Sets are basically used to include membership testing and eliminating duplicate entries. 
# The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average. 


#If Multiple values are present at the same index position, then the value is appended to that index position, 
# to form a Linked List. In, CPython Sets are implemented using a dictionary with dummy variables, 
# where key beings the members set with greater optimizations to the time complexity.


# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6,6, 'Geeks',2])
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
	print(i, end =" ")
print()

# Checking the element
# using in keyword
print("Geeks" in Set)
