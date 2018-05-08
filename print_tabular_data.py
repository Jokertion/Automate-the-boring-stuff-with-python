#打印表格式数据
#技能包：字符串操作的rjust()、ljust()、center()方法对齐文本
def printPicnic(itemsDict,leftWidth,rightWidth):
	print('PICNIC ITEMS'.center(leftWidth + rightWidth,'-'))
	for k,v in itemsDict.items():
		print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies': 8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
