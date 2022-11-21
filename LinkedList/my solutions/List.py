#!/usr/bin/env python3

from ListNode import *

# This class is to be used as an "abstract class". 
class List:

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def clear(self):
		self.head = None
		self.tail = None
		self.size = 0

	def get(self, index):
		if self.size == 0:
			return None

		if index >= self.size or index < 0:
			raise IndexError("Index exceeds range of list.")

		temp = self.head
		i = 0
		while temp != None and i < index:	
			temp = temp.next
			i += 1

		return temp

	def contains(self, obj):
		if self.size == 0:
			return False

		temp = self.head
		while temp != None:
			if temp.data is obj:
				return True
			temp = temp.next 

		return False

	def printList(self):
		if self.size == 0:
			return ""

		ret_list = list()

		temp = self.head
		while temp != None:
			print(str(temp.getData()))
			ret_list.append(temp.getData())
			temp = temp.next

		return ret_list

	def getSize(self):
		return self.size

	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail

