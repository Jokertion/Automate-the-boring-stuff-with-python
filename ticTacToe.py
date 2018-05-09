#ticTacToe.py 井字棋
#技能包：函数 字典 列表
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print (board['top-L'] + '|' +board['top-M'] + '|' + board['top-R'])
	print ('-+-+-')
	print (board['mid-L'] + '|' +board['mid-M'] + '|' + board['mid-R'])
	print ('-+-+-')
	print (board['low-L'] + '|' +board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
	printBoard(theBoard)
	print ('Turn for ' + turn + '.Move on which space?')
	move = input()
	theBoard[move] = turn #更新value
	if turn == 'X':		  #换出棋人
		turn = '0'
	else:
		turn = 'X'
printBoard(theBoard)