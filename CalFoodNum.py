#计算不同客人带来的食物数量总数
#技能包：嵌套字典的调用
allGuests = {'Alice': {'apples':5, 'pretzes':12},
			'Bob': {'ham sandwiches':3, 'apples':2},
			'Carol': {'cups':3, 'apple pies':1}}
			
def totalBrought(guests,item):
	numBrought = 0
	for k, v in guests.items():  #遍历guests的键值对,客人名字赋给k,带来的食物赋给v
		#如果带来的食物在键中，将值赋到numBrought中，如果不是键，get()方法返回0，添加到numBrouhgt.
		numBrought = numBrought + v.get(item,0) 
	return numBrought
	
print ('Number of things being bought:')
print (' - Apples ' + str(totalBrought(allGuests, 'Apples')))
print (' - Cups ' + str(totalBrought(allGuests, 'cups')))
print (' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print (' - Ham sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print (' - apple pies ' + str(totalBrought(allGuests, 'apple pies')))

		
