from matplotlib import pyplot as plt
from random import randint
plt.ion()
rnd = [0,0,0,0,0,0,0,0,0,0]
i=0
while(i<1000):
	i+=1
	rnd[randint(0,9)]+=1
	x=range(len(rnd))
	rects1 = plt.bar(x,rnd)
	plt.pause(.001)
plt.show()
