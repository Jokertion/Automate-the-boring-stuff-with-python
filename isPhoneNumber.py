#字符串中查找电话号码--正则表达式的使用
#技能包：def定义函数，for便利循环测试长字符，正则表达式
import re
def isPhoneNumber(text):
	if len(text) != 12:  #检查字符串是否刚好有12个字符
		return False
	for i in range(0,3): #检查前三个字符是否只有数字
		if not text[i].isdecimal(): 
			return False
	if text[3] != '-':   #检查第一个'-'
		return False
	for i in range(4,7): #检查中间三个字符是否只有数字
		if not text[i].isdecimal():
			return False
	if text[7] != '-':   #检查第一个'-'
		return False
	for i in range(8,12):#检查末尾四个字符是否只有数字
		if not text[i].isdecimal():
			return False
	return True 
	
"""
print ('415-555-4242 is a phone number')
print (isPhoneNumber('415-555-4242'))
print ('Moshi moshi is a phone number')
print (isPhoneNumber('Moshi moshi'))
"""
#遍历整个字符串，测试每一段12个字符，打印出所有满足函数的chunk
message = 'Call me at 415-555-1011 tomorrow.415-555-9999 is my office.'
for i in range(len(message)):
	chunk = me ssage[i:i+12]  #截取message一段新的12个字符赋给变量chunk
	if isPhoneNumber(chunk): #将chunk传递给isPhoneNumber()看是否符合电话号码模式
		print('Phone number found:' + chunk)
print ('Done')

""" 正则表达式"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 415-555-4242.')
print ('Phone number found: ' + mo.group())