import time 
def calcProd():
	product = 1
	for i in range(1,100000): #循环遍历1 - 99999乘积
		product = product * i
	return product
		
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.'%(len(str(prod))))  #打印结果长度
print('Took %s second to calculate.'%(endTime-startTime)) #打印运行时间
