import time
import sys
import random

def echo():
	sum = 0 #计数，到100s则完成
	random.seed(time.time)
	start = '开始下载: '
	end = " 下载完成"

	print(start,end='')
	for i in range(1,100):
		j = random.randint(1,5)
		sum += j
		print('>'*j,end='',flush=True)
		if sum >= 100:
			print("sum=",sum)
			return
		time.sleep(1)
	print(end)

echo()
