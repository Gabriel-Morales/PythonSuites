#!/usr/bin/env python3

try:

	import sys
	from random import *
	from LinkedList import *
	from DoublyLinkedList import *

	seen = list()
	seen2 = list()
	i = 0
	while i < 20:
		num = randrange(20)
		while num in seen:
			num = randrange(20)
		seen.append(num)
		seen2.append(num)
		i += 1

	print("Starting tests for LinkedList.py ...")
	print("Elements to be inserted: ")
	print(seen)
	print()


	print("Testing empty list... ")
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	my_list = LinkedList()
	if my_list is None:
		print("Object cannot be null. The test cases will not run.")
		sys.exit()

	if my_list.getHead() is None:
		print("Current head node is None --- passed!")
	else:
		print("Head node expected None, got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getTail() is None:
		print("Current tail node is None --- passed!")
	else:
		print("Tail node expected None, got: " + str(my_list.getTail()) + " --- failed!")
		sys.exit()

	if my_list.getSize() == 0:
		print("List size expected 0, got: 0 --- passed!")
	else:
		print("List size expected 0, got: " + str(my_list.getSize()) + " --- failed!")
		sys.exit()

	if my_list.get(5) != None:
		print("Obtaining item out of bounds! --- failed!")
		sys.exit()
	else:
		print("Getting item and index 5.. expected NONE, got NONE --- passed!")

	if my_list.contains(60) is False:
		print("List containing item \"60\" is FALSE --- passed!")
	else:
		print("List containing item \"60\" expected FALSE, got: " + my_list.contains(60) + " --- failed!")
		sys.exit()

	if my_list.remove(60) == None:
		print("Removing from empty list without index: expected None, got: None --- passed!")
	else:
		print("Removing from empty list without index: expected None, got: " + str(my_list.remove(60)) + " --- failed!")
		sys.exit()

	try:
		my_list.remove(60, 9)
		print("Removing from empty list with index exception NOT thrown! --- failed!")
		sys.exit()
	except Exception:
		print("Removing from empty list with index exception THROWN! --- passed!")

	if my_list.printList() == "":
		print("Print list expected \"\", got: \"" + my_list.printList() + "\" --- passed!")
	else:
		print("Print list expected \"\", got: \"" + my_list.printList() + "\" --- failed!")
		sys.exit()

	print()
	print("Testing single element list...")
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	my_list.insert(seen[0])

	if my_list.getHead().getData() == seen[0]:
		print("Single insertion head node data expected " + str(seen[0]) + " got: " + str(my_list.getHead().getData()) + " --- passed!")
	else:
		print("Single insertion head node data expected " + str(seen[0]) + " got: " + str(my_list.getHead().getData()) + " --- failed!")
		sys.exit()

	if my_list.getTail().getData() == seen[0]:
		print("Single insertion tail node data expected " + str(seen[0]) + " got: " + str(my_list.getHead().getData()) + " --- passed!")
	else:
		print("Single insertion tail node data expected " + str(seen[0]) + " got: " + str(my_list.getHead().getData()) + " --- failed!")
		sys.exit()

	if my_list.getSize() == 1:
		print("Current list size expected 1, got: 1 --- passed!")
	else:
		print("Current list size expected 1, got: " + str(my_list.getSize()) + " --- failed!")
		sys.exit()

	if my_list.get(0).getData() == seen[0]:
		print("Retrieving element at index 0, expected " + str(seen[0]) + " got: " + str(my_list.get(0).getData()) + " --- passed!")
	else:
		print("Retrieving element at index 0, expected " + str(seen[0]) + " got: " + str(my_list.get(0).getData()) + " --- failed!")
		sys.exit()

	try:
		my_list.get(3)
		print("Retrieving element at index 3, Exception NOT thrown! --- failed!")

	except Exception:
		print("Retrieving element at index 3, Exception THROWN! --- passed!")

	if my_list.contains(seen[0]) is True:
		print("List contains " + str(seen[0]) + " --- passed!")
	else:
		print("List does NOT contain " + str(seen[0]) + " or function is invalid. --- failed!")
		sys.exit()

	print()
	print("Executing printList()...")
	ret_list = my_list.printList()
	if ret_list[0] == seen[0]:
		print("Print list function succeeded. Expected \"" + str(seen[0]) + "\", got: \"" + str(ret_list[0]) + "\" --- passed!")
	else:
		print("Print list function failed. Expected \"" + str(seen[0]) + "\", got: \"" + str(ret_list[0]) + "\" --- failed!")


	print()
	print("Temporarily removing only element...")
	el = my_list.remove(seen[0])
	if el == seen[0]:
		print("Element removed is expected " + str(seen[0]) + ", got: " + str(el) + " --- passed!")
	else:
		print("Element removed expected " + str(seen[0]) + ", got: " + str(el) + " --- failed!")
		sys.exit()

	if my_list.getHead() is None:
		print("After removal of only node, head expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- passed!")
	else:
		print("After removal of only node, head expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getTail() is None:
		print("After removal of only node, tail expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- passed!")
	else:
		print("After removal of only node, tail expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getSize() == 0:
		print("Current list size expected 0, got 0 --- passed!")
	else:
		print("Current list size expected 0, got " + str(my_list.getSize()))
		sys.exit()

	print()
	print("Reinserting single element and clearing the list...")
	my_list.insert(seen[0])
	my_list.clear()

	if my_list.getHead() is None:
		print("After clearing, head expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- passed!")
	else:
		print("After clearing, head expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getTail() is None:
		print("After clearing, tail expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- passed!")
	else:
		print("After clearing, tail expected " + str(my_list.getHead()) + ", got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getSize() == 0:
		print("Current list size expected 0, got 0 --- passed!")
	else:
		print("Current list size expected 0, got " + str(my_list.getSize()))
		sys.exit()

	print()
	print("Testing multi-element list... ")
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	size = 0
	my_list.clear()
	for e in seen:
		my_list.insert(e)
		size += 1
		if my_list.getSize() != size:
			print("Expected size " + str(size) + ", got: " + str(my_list.getSize()) + " --- failed!")
			sys.exit()

		if my_list.getTail().getData() == e:
			print("Element " + str(e) + " successfully inserted. --- passed!")
		else:
			print("Element " + str(e) + " unsuccessfully inserted. --- failed!")

	print()
	print("Testing list construction...")
	temp = my_list.getHead()
	for e in seen:
		if e != temp.getData():
			print("Construction invalid. Expected " + str(e) + " got: " + str(temp.getData()) + " --- failed!")
			sys.exit()
		else:
			print("Expected " + str(e) + " got: " + str(temp.getData()) + " --- passed!")
		temp = temp.getNext()
	print("List construction --- passed!")

	print()
	print("Testing zero indexing...")
	print("List size: " + str(my_list.getSize()))
	print("Max index allowed: " + str(my_list.getSize() - 1))
	print()

	if my_list.get(my_list.getSize() - 1).getData() == my_list.getTail().getData():
		print("Accessing getSize() - 1 expected " + str(my_list.getTail().getData()) + ", got: " + str(my_list.get(my_list.getSize() - 1).getData()) + " --- passed!")
	else:
		print("Accessing getSize() - 1 expected " + str(my_list.getTail().getData()) + ", got: " + str(my_list.get(my_list.getSize() - 1).getData()) + " --- failed!")
		sys.exit()

	try:
		my_list.get(my_list.getSize())
		print("Accessing getSize() expected exception! --- failed!")

	except Exception:
		print("Accessing getSize() exception thrown! --- passed!")

	try:
		my_list.get(-1)
		print("Accessing -1 expected exception! --- failed!")

	except Exception:
		print("Accessing -1 exception thrown! --- passed!")

	i = 0
	while i < 20:
		if my_list.get(i).getData() == seen[i]:
			print("Accessing element " + str(i) + " expected " + str(seen[i]) + ", got: " + str(seen[i]) + " --- passed!")
		else:
			print("Accessing element " + str(i) + " expected " + str(seen[i]) + ", got: " + str(seen[i]) + " --- failed!")
			sys.exit()

		i += 1

	print()
	print("Executing printList()...")
	ret_list = my_list.printList()
	if len(seen) != my_list.getSize():
		print("Size expected " + str(len(seen)) + ", got: " + str(my_list.getSize()))
		sys.exit()


	if ret_list == seen:
		print("Print list --- passed!")
	else:
		i = 0
		while i < 20:
			if seen[i] != ret_list[i]:
				print("Element " + str(i) + " print list expected " + str(seen[i]) + ", got: " + str(ret_list[i]) + " --- failed!")
				sys.exit()
			i += 1
	print()

	try:
		my_list.insert(12, -2)
		print("Inserting at index -2, exception NOT thrown. --- failed!")
	except Exception:
		print("Inserting at index -2, exception THROWN! --- passed!")

	try:
		my_list.insert(12, my_list.getSize() + 1)
		print("Inserting at index getSize() + 1, exception NOT thrown. --- failed!")
	except Exception:
		print("Inserting at index getSize() + 1, exception THROWN! --- passed!")

	my_list.insert(120, my_list.getSize())
	if my_list.getTail().getData() == 120:
		print("One: Inserting 120 at end of list using getSize() --- passed!")
	else:
		print("One: Inserting at end of list using getSize() expected 120, got: " + str(my_list.getTail().getData()) + " --- failed!")
		sys.exit()

	my_list.insert(180, my_list.getSize())
	if my_list.getTail().getData() == 180:
		print("Two: Inserting 180 at end of list using getSize() --- passed!")
	else:
		print("Two: Inserting at end of list using getSize() expected 180, got: " + str(my_list.getTail().getData()) + " --- failed!")
		sys.exit()

	seen.append(120)
	seen.append(180)

	my_list.insert(120, 0)
	if my_list.getHead().getData() == 120:
		print("One: Inserting 120 at start of list --- passed!")
	else:
		print("One: Inserting at start of list expected 120, got: " + str(my_list.getTail().getData()) + " --- failed!")
		sys.exit()

	my_list.insert(180, 0)
	if my_list.getHead().getData() == 180:
		print("Two: Inserting 180 at start of list --- passed!")
	else:
		print("Two: Inserting at start of list, got: " + str(my_list.getTail().getData()) + " --- failed!")
		sys.exit()

	seen.insert(0, 120)
	seen.insert(0, 180)

	print("Executing printList() for modified list...")
	ret_list = my_list.printList()

	if seen == ret_list:
		print("New print list --- passed!")
	else:
		i = 0
		while i < 20:
			if seen[i] != ret_list[i]:
				print("Element " + str(i) + " print list expected " + str(seen[i]) + ", got: " + str(ret_list[i]) + " --- failed!")
				sys.exit()
			i += 1

	print()

	print("Inserting 99 at index 5")
	my_list.insert(99, 5)

	print("Inserting 76 at index 8")
	my_list.insert(76, 8)

	print("Inserting 62 at index 2")
	my_list.insert(76, 2)

	print("Inserting 91 at index 15")
	my_list.insert(91, 15)

	seen.insert(5, 99)
	seen.insert(8, 76)
	seen.insert(2, 76)
	seen.insert(15, 91)

	print("Executing final printList()...")
	ret_list = my_list.printList()
	if len(seen) != my_list.getSize():
		print("Size expected " + str(len(seen)) + ", got: " + str(my_list.getSize()))
		sys.exit()

	if seen == ret_list:
		print("Final print list --- passed!")
	else:
		i = 0
		while i < 20:
			if seen[i] != ret_list[i]:
				print("Element " + str(i) + " print list expected " + str(seen[i]) + ", got: " + str(ret_list[i]) + " --- failed!")
				sys.exit()
			i += 1

	print()

	print("Testing contains()...")
	for e in seen:
		if my_list.contains(e) == True:
			print("List contains " + str(e) + " --- passed!")
		else:
			print("Contain method not functional for element " + str(e) + " --- failed!")
			sys.exit()

	if my_list.contains(900) == False:
		print("For contains(900) expected False got False --- passed!")
	else:
		print("For contains(900) expected False got True --- failed!")
		sys.exit()

	print()
	print("Testing remove()...")
	num = my_list.remove(None, 0)
	if num == seen[0]:
		print("Remove index 0 expected " + str(seen[0]) + " got: " + str(num) + " --- passed!")
	else:
		print("Remove index 0 expected " + str(seen[0]) + " got: " + str(num) + " --- failed!")
		sys.exit()


	num = my_list.remove(180)
	if num == seen[len(seen) - 1]:
		print("Remove 180 expected " + str(seen[len(seen) - 1]) + " got: " + str(num) + " --- passed!")
	else:
		print("Remove 180 expected " + str(seen[len(seen) - 1]) + " got: " + str(num) + " --- failed!")
		sys.exit()

	seen = seen[1:]
	seen.pop()

	num = my_list.remove(None, 17)
	if num == seen[17]:
		print("Remove index 17 expected " + str(seen[17]) + " got: " + str(num) + " --- passed!")
	else:
		print("Remove index 17 expected " + str(seen[17]) + " got: " + str(num) + " --- failed!")
		sys.exit()

	seen.remove(num)

	try:
		my_list.remove(None, 80)
		print("Removing index 80 exception NOT thrown --- failed!")
		sys.exit()
	except Exception:
		print("Removing index 80 exception THROWN --- passed!")

	num = my_list.remove(600)
	if num is None:
		print("Removing element 600 expected None got None --- passed!")
	else:
		print("Removing element 600 expected None got " + str(num) + " --- failed!")
		sys.exit()

	i = 0
	for e in seen:
		num = my_list.remove(e)
		if num == e:
			print("Removing " + str(e) + " --- passed!")
		else:
			print("Removing " + str(e) + ", got: " + str(num) + " --- failed!")
			sys.exit()
		
		seen = seen[1:]
		print("Checking list integrity upon removal...")
		construction = list()
		temp = my_list.getHead()
		while temp != None:
			construction.append(temp.getData())
			temp = temp.next

		if construction == seen:
			print("List sill in tact --- passed!")
		else:
			print()
			print("List integrity damaged (see below)")
			print("Obtained list construction: " + str(construction))
			print("Expected list construction: " + str(seen))
			print(" --- failed! ---")
			sys.exit() 

		print()
		i += 1

	if my_list.getHead() is None:
		print("Removal of everything head expected None --- passed!")
	else:
		print("Removal of everything head expected None, got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getTail() is None:
		print("Removal of everything tail expected None --- passed!")
	else:
		print("Removal of everything tail expected None, got: " + str(my_list.getHead()) + " --- failed!")
		sys.exit()

	if my_list.getSize() is 0:
		print("Removal of everything size expected 0 --- passed!")
	else:
		print("Removal of everything size expected 0, got: " + str(my_list.getSize()) + " --- failed!")
		sys.exit()

	print()
	print("Starting tests for DoublyLinkedList.py ... ")
	print("Elements to be inserted: ")
	print(seen2)
	seenr = seen2[::-1]
	print()
	print(" ** As this is a modification of the original, the tests are slightly smaller ** ")
	print()
	my_list = DoublyLinkedList()
	for e in seen2:
		my_list.insert(e)
		if e == my_list.getTail().getData():
			print("Insertion of " + str(e) + " succesfull --- passed!")
		else:
			print("Insertion of " + str(e) + " unsuccesfull --- failed!")
			sys.exit()

	print()
	print("Executing normal printList()...")
	ret_list_reg = my_list.printList()

	if ret_list_reg == seen2:
		print("Initial print list --- passed!")
	else:
		i = 0
		while i < 20:
			if seen2[i] != ret_list_reg[i]:
				print("Element " + str(i) + " print list expected " + str(seen2[i]) + ", got: " + str(ret_list_reg[i]) + " --- failed!")
				sys.exit()
			i += 1
	print()

	print("Executing printListReverse()...")
	ret_list = my_list.printListReverse()

	if ret_list == seenr:
		print("Reversed print list --- passed!")
	else:
		i = 0
		while i < 20:
			if seen2[i] != ret_list_reg[i]:
				print("Element " + str(i) + " print list expected " + str(seenr[i]) + ", got: " + str(ret_list[i]) + " --- failed!")
				sys.exit()
			i += 1
	print()

	print("Testing removal and integrity of reverse traversal...")
	i = 0
	for e in seenr:
		num = my_list.remove(e)
		if num == e:
			print("Removing " + str(e) + " --- passed!")
		else:
			print("Removing " + str(e) + ", got: " + str(num) + " --- failed!")
			sys.exit()
		
		seenr = seenr[1:]
		print("Checking list integrity upon removal...")
		construction = list()
		temp = my_list.getTail()
		while temp != None:
			construction.append(temp.getData())
			temp = temp.prev

		if construction == seenr:
			print("List sill in tact --- passed!")
		else:
			print()
			print("List integrity damaged (see below)")
			print("Obtained list construction: " + str(construction))
			print("Expected list construction: " + str(seenr))
			print(" --- failed! ---")
			sys.exit() 

		print()
		i += 1

	print()
	print("ALL CASES PASSED! ")

except Exception as e:
	print("During testing, your code has thrown an unexpected error.")
	print("This could be the result of: ")
	print("\t- Out of bounds accesses")
	print("\t- Calling methods on a 'None' object")
	print("\t- Wrong import statemets")
	print("\t- Unlikely, but the test cases are corrupted")
	print("\t- Other")
	print("Look through your code first and if all else fails, feel free to contact me.")
	print()
	print("Detail: " + str(e))
	print()
