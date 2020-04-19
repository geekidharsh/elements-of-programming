# create a chache for looking up price of books, identified by their ISBN

"""
following operation needs to be performed
insert: insert if not present check capacity, if present, do not update price but move isbn to the front
look up: if found update to the front and return, if not found return -1
erase: if isbn was present, remove and return true else false
"""

class LRUCache:

	def _init_(self, capacity):
		self.isbn_price_map = collections.OrderedDict()
		self.capacity = capacity


	def insert(self, isbn, price):
		if isbn in self.isbn_price_map:
			# since isbn exists already, we pop isbn, 
			# pop removes the last item returns the value / removes like a queue
			price = self.isbn_price_map.pop(isbn)
		elif len(self.isbn_price_map) == self.capacity:
			# pop items like, item
			# The pairs are returned in LIFO order if last is true or FIFO order if false.
			self.isbn_price_map.popitem(last=False)
		self.isbn_price_map[isbn] = price



	def lookup(self, isbn):
		if isbn not in self.isbn_price_map:
			return -1
		else:
			price = self.isbn_price_map.pop(isbn)
			self.isbn_price_map[isbn] = price


	def erase(self, isbn):
		if isbn in self.isbn_price_map:
			self.isbn_price_map.pop(isbn)
			return True
		else:
			return False


# time: o(1) for lookup, erase and insert respectively. so O(1) overall.





