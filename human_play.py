# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-10-24 15:24:39
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-10-25 16:57:15

from __future__ import print_function
from game import Board,Game

class Human(object):

	def __init__(self):
		self.human_seat = None

	def set_Human_seat(self,human_seat):
		self.human_seat = human_seat

	'''
	如果想要翻棋则输入"30,1",如果想要移动棋子，则输入"1,2"。1表示选中棋子位置，2表示棋子的终点位置
	'''
	def human_action(self,board):
		try:
			action = input("Please input your action:")
			action = [int(n, 10) for n in action.split(",")]
			print(action)			
		except Exception as e:
			action  = []
		if len(action) != 2:
			print("invalid move")
			action = self.human_action(board)
		if not board.can_select(action[0],self.human_seat):
			print(action[0],"is not your chess")
			action = self.human_action(board)
		if not board.can_move_to(action[0],action[1]):
			print(action[0],"can't move to",action[1])
			action = self.human_action(board)
		return action

def run():
	board = Board()
	game = Game(board)
	human1 = Human()
	human2 = Human()
	game.start_play(human1,human2)

if __name__ == '__main__':
	run()