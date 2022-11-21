#!/usr/bin/env python3

# just standard in-case imports
import os
import sys

from collections import deque

class Queue:

	def __init__(self):
		self.queue = deque(list())

	def enqueue(self, obj):
		self.queue.append(obj)

	def dequeue(self):
		return self.queue.popleft()

	def isEmpty(self):
		return len(self.queue) == 0

	def size(self):
		return len(self.queue)

	def printQueue(self):
		print(list(self.queue))
		return list(self.queue)

