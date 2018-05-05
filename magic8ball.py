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

print (message[random.randint(0,len(message)-1)])  #产生随机数做下标
