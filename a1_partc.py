#    Main Author(s): Devon Chan
#    Main Reviewer(s): Vincent Le, Foad Ozgoli

class Stack:
	"""The Stack class implements a FILO data structure."""

	# This class constructor accepts an integer 'cap',
	# and initializes the class with the given capacity.
	def __init__(self, cap=10):
		self.cap = cap
		self.items = [None] * cap
		self.size = 0

	# This function returns the capacity of the class.
	def capacity(self):
		return self.cap

	# This function adds an item to the Stack,
	# and accepts one piece of data from the parameter.
	# If the stack is full, the capacity is doubled first.
	def push(self, data):            
	    if self.size == self.cap:
	        self.cap *= 2
	        new_items = [None] * self.cap
	        new_items[:self.size] = self.items
	        self.items = new_items
	    self.items[self.size] = data
	    self.size += 1

	# This function removes the item at the top of the Stack,
	# and returns the removed item.
	def pop(self):
		if self.size == 0:
			raise IndexError('pop() used on empty stack')
		self.size -= 1
		data = self.items[self.size]
		self.items[self.size] = None
		return data

	# This function returns the item at the top of the Stack,
	# or will return None if the Stack is empty.
	def get_top(self):
		if self.size > 0:
			return self.items[self.size - 1]
		return None

	# This function returns true is the Stack is empty or false if not empty.
	def is_empty(self):
		return self.size == 0
	
	# This function returns the size of the Stack.
	def __len__(self):
		return self.size


class Queue:
	"""The Queue class implements a FIFO data structure."""

	# This class constructor optionally accepts an integer 'cap',
	# and initializes the class with the given capacity.
	def __init__(self, cap=10):
		self.cap = cap
		self.items = [None] * cap
		self.size = 0
		self.front = 0
		self.rear = 0

	# This function returns capacity of the Queue.
	def capacity(self):
		return self.cap

	# This function adds an item to the end of the Queue,
	# and accepts one piece of data from the parameter.
	# If the Queue is full, the capacity is doubled first.
	def enqueue(self, data):
		if self.size == self.cap:
			new_items = [None] * (self.cap*2)
			for i in range(self.size):
				new_items[i] = self.items[(self.front+i) % self.cap]
			self.cap *= 2
			self.items = new_items
			self.front = 0
			self.rear = self.size
		self.items[self.rear] = data
		self.rear = (self.rear+1) % self.cap
		self.size += 1

	# This function removes an item from the front of the Queue,
	# and returns the removed item.
	def dequeue(self):
		if self.size == 0:
			raise IndexError('dequeue() used on empty queue')
		data = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front+1) % self.cap
		self.size -= 1
		return data
	
	# This function returns the item at the front of the Queue,
	# or None if the Queue is empty.
	def get_front(self):
		if self.size == 0:
			return None
		return self.items[self.front]
	
	# This function returns true if the Queue is empty, or false if not empty.
	def is_empty(self):
		return self.size == 0

	# This function returns the size of the Queue.
	def __len__(self):
		return self.size



class Deque:
	"""The Deque class implements a double-ended Queue data structure."""

	# This class constructor optionally accepts an integer 'cap'
	# and initializes the class with the given capacity.
	def __init__(self, cap=10):
		self.cap = cap
		self.items = [None] * cap
		self.size = 0
		self.front = 0
		self.back = 0

	# This function returns the capacity of the Deque.
	def capacity(self):
		return self.cap

	# This function adds an item to the front of the Deque,
	# and accepts one piece of data from the parameter.
	# If the deque is full, the capacity is doubled first.
	def push_front(self, data):
		if self.cap == self.size:
			new_items = [None] * (self.cap*2)
			for i in range(self.size):
				new_items[i] = self.items[(self.front+i) % self.cap]
			self.cap *= 2
			self.items = new_items
			self.front = 0
			self.back = self.size
		self.front = (self.front-1) % self.cap
		self.items[self.front] = data
		self.size += 1

	# This function adds an item to the back of the Deque,
	# and accepts one piece of data from the parameter.
	# If the deque is full, the capacity is doubled first.
	def push_back(self, data):
		if self.size == self.cap:
			new_items = [None] * (self.cap*2)
			for i in range(self.size):
				new_items[i] = self.items[(self.front+i) % self.cap]
			self.cap *= 2
			self.items = new_items
			self.front = 0
			self.back = self.size
		self.items[self.back] = data
		self.back = (self.back+1) % self.cap
		self.size += 1

	# This function removes the item at the front of the Deque,
	# and returns the removed item.
	def pop_front(self):
		if self.size == 0:
			raise IndexError('pop_front() used on empty deque')
		data = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front+1) % self.cap
		self.size -= 1
		return data
		
	# This function removes the item at the back of the Deque,
	# and returns the removed item.
	def pop_back(self):
		if self.size == 0:
			  raise IndexError('pop_back() used on empty deque')
		data = self.items[(self.back-1) % self.cap]
		self.items[(self.back-1) % self.cap] = None
		self.back = (self.back-1) % self.cap
		self.size -= 1
		return data
		
	# This function returns the item at the front of the Deque,
	# or None if the Deque is empty.
	def get_front(self):
		if self.size == 0:
			return None
		return self.items[self.front]

	# This function returns the item at the back of the Deque,
	# or None if the Deque is empty.
	def get_back(self):
		if self.size == 0:
			return None
		return self.items[(self.back-1) % self.cap]

	# This function returns true if the Deque is empty, or false if not empty.
	def is_empty(self):
		return self.size == 0

	# This function returns the size of the Deque.
	def __len__(self):
		return self.size

	# This function takes in an integer 'k',
	# and returns the item at position 'k' of the Deque.
	def __getitem__(self, k):
		if k < 0 or k >= self.size or self.items[k] == None:
			raise IndexError('Index out of range')
		return self.items[(self.front+k) % self.cap]