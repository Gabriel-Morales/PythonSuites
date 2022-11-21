#!/usr/bin/env python3

import sys
import os
import time
from random import *


def linear_search(my_list, num):
	mark = False
	time_start = time.time()
	i = 0
	while i < len(my_list):
		if my_list[i] == num:
			print("Found! ")
			mark = True
			break
		i += 1
	time_end = time.time()
	if mark == False:
		print("Number not found!")

	print("Time to search (seconds): " + str(time_end - time_start))


def binary_search(my_list, num):
	mark = False
	time_start = time.time()
	low = 0
	high = 29_999_999
	
	mid = (low + high) // 2
	while low <= high:
		if my_list[mid] == num:
			mark = True
			print("Found!")
			break
		if num < my_list[mid]:
			high = mid - 1
			mid = (low + high) // 2
		else:
			low = mid + 1
			mid = (low + high) // 2


	time_end = time.time()
	if mark == False:
		print("Number not found!")

	total_time = (time_end - time_start)
	print("Time to search (seconds): %f" % total_time)



seen = list()
print("Generating about 30 million numbers.")
print("Please wait, python iteration is slow :( ")
print("Progress:  ")

i = 0
while i < 30_000_000:
	update = (i/30_000_000)*100
	print("%d%%" % update, end="\r")
	seen.append(i)
	i += 1
print("100%", end="\r")


print()
print("Done generating!")
print("Performing linear search on list..")

try:
	user_input = int(input("Input number to search for: "))
except Exception as e:
	print("Invalid input! Try again. Error: " + str(e))
	sys.exit()

print()
print("Linear search for: " + str(user_input))
linear_search(seen, user_input)

print()

print("Performing binary search on list..")
binary_search(seen, user_input)

print()



