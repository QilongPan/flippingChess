# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-10-24 15:23:57
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-10-25 17:10:24
from __future__ import print_function
import random
import numpy as np 

class Student(object):
	def __init__(self):
		self.name = "abc"

	def di(self):
		self.display()

	def display(self):
		print(self.name)

def get_type_name(type_int):
	if type_int == 0:
		print("司")

action = [[1,2],[2,1],[3,4]]
a = [3,4]
if a not in action:
	print("enter")