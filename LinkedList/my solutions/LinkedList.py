#!/usr/bin/env python3

from List import *

class LinkedList(List):

	def __init__(self):
		super().__init__()

	def insert(self, obj, index=-1):
		
		if index > self.getSize() or index < -1:
			raise IndexError("Index exceeds range of list.")

		if self.getSize() == 0:
			self.head = ListNode(obj)
			self.tail = self.head
			self.size += 1
			return

		if index == -1:
			temp = self.tail
			self.tail = ListNode(obj)
			temp.next = self.tail
			temp = None
			self.size += 1
			return

		if index == 0:
			node = ListNode(obj)
			node.next = self.head
			self.head = node
			self.size += 1
			return

		if index == self.getSize():
			node = ListNode(obj)
			self.tail.next = node
			self.tail = node
			node.next = None
			self.size += 1
			return

		position = self.head
		prev = self.head
		trace = 0
		while trace < index:
			prev = position
			position = position.next
			trace += 1

		node = ListNode(obj)
		node.next = position
		prev.next = node
		self.size += 1

		if index == self.getSize():
			self.tail = node

	def remove(self, obj, index=-1):

		if index >= self.getSize() or index < -1:
			raise IndexError("Index exceeds range of list.")

		if self.getSize() == 0:
			return None

		if not self.contains(obj) and index == -1:
			return None

		if self.getSize() == 1:
			data = self.head.data
			self.head.next = None
			self.tail.next = None
			self.head.data = None
			self.head = None
			self.tail = None
			self.size = 0
			return data

		if index != -1:
			prev = self.head
			position = self.head
			i = 0
			while i < index and position != None:
				prev = position
				position = position.next
				i += 1

			prev.next = position.next
			if position == self.head:
				self.head = position.next
			if prev.next is None:
				self.tail = prev

			position.next = None
			self.size -= 1
			
			return position.data

		prev = self.head
		trace = self.head

		while trace != None and trace.data != obj:
			prev = trace
			trace = trace.next

		self.size -= 1

		prev.next = trace.next
		
		if trace == self.head:
			self.head = trace.next
		if prev.next is None:
			self.tail = prev
		trace.next = None

		return trace.data



		








		
