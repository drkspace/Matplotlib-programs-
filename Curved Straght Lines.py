from matplotlib import pyplot as plt
for i in range(0,10):
	plt.plot([0,i+1],[10-i,0])
for i in xrange(0,-10,-1):
	plt.plot([0,i-1],[10+i,0])
for i in range(0,10):
	plt.plot([0,i+1],[-10+i,0])
for i in range(0,10):
	plt.plot([0,-i-1],[-10+i,0])
plt.plot([0,0],[-10,10])
plt.plot([-10,10],[0,0])
plt.ylabel('some numbers')
plt.show()
