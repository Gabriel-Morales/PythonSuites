#!/usr/bin/env python3

from Queue import *
from operator import *

class PriorityQueue(Queue):

	def __init__(self):
		super().__init__()

	#Overriding Queue version to support the priority and insert as tuple: O(1)
	def enqueue(self, obj, priority):
		item = (obj, priority)
		self.queue.append(item)

	def enqueue_insert(self, obj, priority):
		item = (obj, priority)
		#O(1)
		if priority >= self.queue[0][1]:
			self.queue.insert(0, item)
			return
		#O(1)
		if priority < self.queue[len(self.queue) - 1][1]:
			self.queue.append(item)
			return

		#Insertion: O(n) worst, O(1) best. O(n^2) worst with n elements to insert and n to search spot.
		#With O(1) best case, and n elements to insert: O(n) best case
		i = 1
		while i < len(self.queue) - 1:
			if priority >= self.queue[i + 1][1] and priority < self.queue[i - 1][1]:
				self.queue.append(i, item)
				break
			i += 1

	def enqueue_timsort(self, obj, priority):
		item = (obj, priority)
		#O(1) insertion
		self.queue.append(item)
		#Timsort: O(nlogn) worst, O(n) best
		#With n elements to insert and the worst case runtime, the total is O(n^2 * logn)
		#With n elements to insert and the best case runtime, the total is O(n^2)
		temp = list(self.queue)
		temp.sort(key=itemgetter(1), reverse=True)
		self.queue = deque(temp)

	#Overriding Queue version of dequeue to support extracting the highest priority: O(n)
	def dequeue(self):
		current_priority = -1
		item_highest = None
		for e in self.queue:
			if e[1] > current_priority:
				item_highest = e

		self.queue.remove(e)
		return item_highest

	def dequeue_priority(self, obj, priority):
		return self.queue.popleft()


