#！ python3
# 技能包：random模块randint方法（给范围，取随机整数）
import random 

message = ['It is certain',
	'It is decidedly so',
	'Yes definitely',
	'Reply hazy try again',
	'Ask again later',
	'Concertrate and ask again',
	'My reply is no',
	'Outlook not so good',
	'Very doubtful']

print (message[random.randint(0,len(message)-1)])   #产生随机数作下标去索引列表
