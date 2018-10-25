# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-10-24 15:27:55
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-10-25 17:03:42
from __future__ import print_function
import random
import numpy as np
'''
cross_type表示该位置类型。0表示兵站，1表示行营
'''
class Cross(object):

	def __init__(self,id = None,cross_type = None):
		self.id = id
		self.cross_type = cross_type
		self.adjacent_cross = []
		self.chess = None

	def set_cross_type(self,cross_type):
		self.cross_type = cross_type

	def set_adjacent_cross(self,cross_ids):
		for element in cross_ids:
			self.adjacent_cross.append(element)

	def to_string(self):
		print("id:",self.id,"cross type:",self.cross_type)
		for i in self.adjacent_cross:
			print(i)
		'''
		for i in self.adjacent_cross:
			print(i,end=' ')
'''

class Chess(object):
	'''
	type:司长，军长，师长，旅长，团长,营长，连长，炸弹分别采用0,1,2,3,4,5,6,7表示
	'''
	def __init__(self,chess_type = None,seat = None,color = None,show = 0,index = 0):
		self.chess_type = chess_type
		self.seat = seat
		self.color = color
		self.show = show
		self.index = index
	def get_chess_name(self):
		if self.chess_type == 0:
			return 'a'
		elif self.chess_type == 1:
			return 'b'
		elif self.chess_type == 2:
			return 'c'
		elif self.chess_type == 3:
			return 'd'
		elif self.chess_type == 4:
			return 'e'
		elif self.chess_type == 5:
			return 'f'
		elif self.chess_type == 6:
			return 'g'
		elif self.chess_type == 7:
			return 'h'
	'''
	0表示同归于尽
	1表示战胜
	2表示战败
	'''
	def get_fight_result(self,attacked_chess):
		if attacked_chess.chess_type == 7 or self.chess_type == 7:
			return 0
		elif self.chess_type == attacked_chess.chess_type:
			return 0
		if self.chess_type < attacked_chess.chess_type:
			return 1
		else:
			return 2

	def to_string(self):
		print("type:",self.chess_type,"seat:",self.seat,"color:",self.color,"show:",self.show)



class Board(object):

	'''
	每位玩家具有如下棋子
	司令，军长，师长，师长，旅长，旅长，团长，团长，营长，营长，连长，炸弹 总共12颗棋
	'''
	def __init__(self):
		self.players = [0,1]
		self.cross_list = []
		for i in range(30):
			cross = Cross(i,0)
			self.cross_list.append(cross)
		self.cross_list[11].set_cross_type(1)
		self.cross_list[13].set_cross_type(1)
		self.cross_list[17].set_cross_type(1)
		self.cross_list[21].set_cross_type(1)
		self.cross_list[23].set_cross_type(1)
		self.cross_list[0].set_adjacent_cross([1,5])
		self.cross_list[1].set_adjacent_cross([0,2,6])
		self.cross_list[2].set_adjacent_cross([1,3,7])
		self.cross_list[3].set_adjacent_cross([2,4,8])
		self.cross_list[4].set_adjacent_cross([3,9])
		self.cross_list[5].set_adjacent_cross([0,6,10,11])
		self.cross_list[6].set_adjacent_cross([1,5,7,11])
		self.cross_list[7].set_adjacent_cross([2,6,8,11,12,13])
		self.cross_list[8].set_adjacent_cross([3,7,9,13])
		self.cross_list[9].set_adjacent_cross([4,8,13,14])
		self.cross_list[10].set_adjacent_cross([5,11,15])
		self.cross_list[11].set_adjacent_cross([5,6,7,10,12,15,16,17])
		self.cross_list[12].set_adjacent_cross([7,11,13,17])
		self.cross_list[13].set_adjacent_cross([7,8,9,12,14,17,18,19])
		self.cross_list[14].set_adjacent_cross([9,13,19])
		self.cross_list[15].set_adjacent_cross([10,11,16,20,21])
		self.cross_list[16].set_adjacent_cross([11,15,17,21])
		self.cross_list[17].set_adjacent_cross([11,12,13,16,18,21,22,23])
		self.cross_list[18].set_adjacent_cross([13,17,19,23])
		self.cross_list[19].set_adjacent_cross([13,14,18,23,24])
		self.cross_list[20].set_adjacent_cross([15,21,25])
		self.cross_list[21].set_adjacent_cross([15,16,17,20,22,25,26,27])
		self.cross_list[22].set_adjacent_cross([17,21,23,27])
		self.cross_list[23].set_adjacent_cross([17,18,19,22,24,27,28,29])
		self.cross_list[24].set_adjacent_cross([19,23,29])
		self.cross_list[25].set_adjacent_cross([20,21,26])
		self.cross_list[26].set_adjacent_cross([21,25,27])
		self.cross_list[27].set_adjacent_cross([21,22,23,26,28])
		self.cross_list[28].set_adjacent_cross([23,27,29])
		self.cross_list[29].set_adjacent_cross([23,24,28])

		#初始化所有的棋子
		self.all_chess = []
		#type,seat,color,show,index
		#seat = 0
		self.all_chess.append(Chess(0,0,0,1,0))
		self.all_chess.append(Chess(1,0,0,1,0))		
		self.all_chess.append(Chess(2,0,0,1,0))
		self.all_chess.append(Chess(2,0,0,1,1))		
		self.all_chess.append(Chess(3,0,0,1,0))
		self.all_chess.append(Chess(3,0,0,1,1))		
		self.all_chess.append(Chess(4,0,0,1,0))
		self.all_chess.append(Chess(4,0,0,1,1))	
		self.all_chess.append(Chess(5,0,0,1,0))
		self.all_chess.append(Chess(5,0,0,1,1))		
		self.all_chess.append(Chess(6,0,0,1,0))
		self.all_chess.append(Chess(7,0,0,1,0))	
		#seat = 1
		self.all_chess.append(Chess(0,1,1,1,0))
		self.all_chess.append(Chess(1,1,1,1,0))		
		self.all_chess.append(Chess(2,1,1,1,0))
		self.all_chess.append(Chess(2,1,1,1,1))		
		self.all_chess.append(Chess(3,1,1,1,0))
		self.all_chess.append(Chess(3,1,1,1,1))		
		self.all_chess.append(Chess(4,1,1,1,0))
		self.all_chess.append(Chess(4,1,1,1,1))	
		self.all_chess.append(Chess(5,1,1,1,0))
		self.all_chess.append(Chess(5,1,1,1,1))		
		self.all_chess.append(Chess(6,1,1,1,0))
		self.all_chess.append(Chess(7,1,1,1,0))

		self.width = 5
		self.height = 6


	def init_board(self,start_player = 0):
		self.current_player = self.players[start_player]
		self.last_action = None
		self.players_chess_number = [12,12]
		self.states = {}
		self.no_eat_chess_times = 0
		self.action_times = 0
		self.random_layout()
		current_index = 0
		for i in range(29):
			if i == 11 or i == 13 or i == 17 or i == 21 or i == 23:
				self.cross_list[i].chess = None
			else:
				self.cross_list[i].chess = self.all_chess[current_index]
				current_index = current_index + 1
		self.cross_list[29].chess = None

	def random_layout(self):
		for i in range(len(self.all_chess) - 1,-1,-1):
			random_index = random.randint(0,i)
			chess = self.all_chess[random_index]
			self.all_chess[random_index] = self.all_chess[i]
			self.all_chess[i] = chess

	def to_string(self):
		str_list = []
		for i in range(self.height):
			one_raw_str = ""
			for j in range(self.width):
				cross_index = i * 5 + j
				if self.cross_list[cross_index].chess == None:
					one_raw_str = one_raw_str +"*"
				else:
					if self.cross_list[cross_index].chess.seat == 0:
						one_raw_str = one_raw_str + str(self.cross_list[cross_index].chess.chess_type)
					else:
						one_raw_str = one_raw_str + self.cross_list[cross_index].chess.get_chess_name()
				one_raw_str = one_raw_str +"          "
			str_list.append(one_raw_str)

		for i in range(len(str_list) - 1,-1,-1):
			print(str_list[i])
			print("")

	def get_current_player(self):
		return self.current_player

	def do_action(self,action):

		self.last_action = action
		print("last action:")
		print(self.last_action)

		self.action_times = self.action_times + 1
		if self.cross_list[action[1]].chess == None:
			self.no_eat_chess_times = self.no_eat_chess_times + 1
		else:
			self.no_eat_chess_times = 0
		self.move_chess(action)
		if self.current_player == self.players[1]:
			self.current_player = self.players[0]
		else:
			self.current_player = self.players[1]
		print("no eat chess times:",self.no_eat_chess_times)
		print("action times:",self.action_times)

	def move_chess(self,action):
		if len(action) < 2:
			return 
		elif self.cross_list[action[0]].chess == None:
			return
		else:
			if self.cross_list[action[1]].chess == None:
				self.cross_list[action[1]].chess = self.cross_list[action[0]].chess
				self.cross_list[action[0]].chess = None
			else:
				fight_result = self.cross_list[action[0]].chess.get_fight_result(self.cross_list[action[1]].chess)
				if fight_result == 1:
					end_move_chess = self.cross_list[action[1]].chess
					self.players_chess_number[end_move_chess.seat] = self.players_chess_number[end_move_chess.seat] - 1
					self.cross_list[action[1]].chess= self.cross_list[action[0]].chess
				elif fight_result == 0:
					start_move_chess = self.cross_list[action[0]].chess
					end_move_chess = self.cross_list[action[1]].chess
					self.players_chess_number[start_move_chess.seat] = self.players_chess_number[start_move_chess.seat] - 1
					self.players_chess_number[end_move_chess.seat] = self.players_chess_number[end_move_chess.seat] - 1
					self.cross_list[action[1]].chess = None
				self.cross_list[action[0]].chess = None

	def has_a_winner(self):
		if self.players_chess_number[0] < 3:
			return True,1
		elif self.players_chess_number[1] < 3:
			return True,0
		return False,-1
		'''
		当没有棋子时，则判输
		当30步没吃子时，强制和棋
		当总步数超过250步时，强制和棋
		'''
	def game_end(self):
		win,winner = self.has_a_winner()
		if win:
			return True,winner
		elif self.no_eat_chess_times == 30:
			return True,-1
		elif self.action_times > 250:
			return True,-1
		return False,-1

	def can_select(self,position,seat):
		if self.cross_list[position].chess == None:
			return False
		elif self.cross_list[position].chess.seat != seat:
			return False
		return True

	def can_move_to(self,start_position,to_position):
		if to_position not in self.cross_list[start_position].adjacent_cross:
			return False
		if self.cross_list[start_position].chess == None:
			return False
		else:
			if self.cross_list[to_position].chess == None:
				return True
			else:
				fight_result = self.cross_list[start_position].chess.get_fight_result(self.cross_list[to_position].chess)
				if fight_result == 0 or fight_result == 1:
					return True
				else:
					return False
	'''
	第一个棋盘为当前玩家的棋子位置表示
	第二个棋盘为另一玩家的棋子位置表示
	第三个棋盘为最后一颗子的落子位置
	第四个棋盘为如果该己方行动，则为1，否则为0
	'''
	def current_state(self):
		square_state = np.zeros((4, self.width, self.height))
		if self.action_times > 0:
			for i in range(self.width):
				for j in range(self.height):
					chess = self.cross_list[self.width * self.height + self.height].chess
					if chess != None:
						if chess.seat == self.current_player:
							square_state[0][self.width,self.height] = chess.cross_type
						else:
							square_state[1][self.width,self.height] = chess.cross_type
			square_state[2][self.last_action[1]//self.width,self.last_action[1]%self.height] = 1.0
		if len(self.action_times) % 2 == 0:
			square_state[3][:,:] = 1.0
        #将棋盘最后一行放到第一行，倒数第二行放在第二行，依次类推
		return square_state[:,::-1,:]





class Game(object):
	def __init__(self,board):
		self.board = board

	def graphic(self,board):
		self.board.to_string()

	def start_play(self,player1,player2,start_player = 0,is_shown = 1):
		if start_player not in (0,1):
			raise Exception('start_player should be either 0(player1 first)'
				'or 1 (player2 first')
		self.board.init_board(start_player)
		p1,p2 = self.board.players
		player1.set_Human_seat(p1)
		player2.set_Human_seat(p2)
		players = {p1:player1,p2:player2}
		if is_shown:
			self.graphic(self.board)
		count = 0
		while count < 2:
			current_player = self.board.get_current_player()
			player_in_turn = players[current_player]
			action = player_in_turn.human_action(self.board)
			self.board.do_action(action)
			if is_shown:
				self.graphic(self.board)
			end,winner = self.board.game_end()
			count = count + 1
			if end:
				if is_shown:
					if winner != -1:
						print("Game end.Winner is",winner)
					else:
						print("Game end. Tie")
				return winner

	def start_self_play(self,player,is_shown = 0,temp = 1e-3):
		self.board.init_board()
		p1,p2 = self.board.players
		states,mcts_probs,current_players = [],[],[]
		while True:
			action,action_probs = player.get_action(self.board,temp=temp,ruturn_prob = 1)
			states.append(self.board.current_state())
			mcts_probs.append(action_probs)
			current_players.append(self.board.current_player)
			self.board.do_action(action)
			if is_shown:
				self.graphic(self.board)
			end,winner = self.board.game_end()
			if end:
				winners_z = np.zeros(len(current_players))
				if winner != -1:
					winners_z[np.array(current_players) == winner] = 1.0
					winners_z[np.array(current_players) != winner] = -1.0
				player.reset_player()
				if is_shown:
					if winner != -1:
						print("Game end.Winner is player:",winner)
					else:
						print("Game end. Tie")
				return winner,zip(states,mcts_probs,winners_z)







