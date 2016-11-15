from matplotlib import pyplot as plt
from Tkinter import *
import time
import math
import sys
mode=int(sys.argv[1])
tau=2*math.pi
number=500
radPerNumber=tau/number
plt.ion()

if mode==0:
	root = Tk()
	root.geometry("100x100")
	e=Entry(root)
	e.pack()
	
	def run():
		plt.cla()
		multiplier=float(e.get())
		for i in range(0,number):
			plt.plot([math.cos((radPerNumber*i)),math.cos((radPerNumber*i*multiplier))],[math.sin((radPerNumber*i)),math.sin((radPerNumber*i*multiplier))], color="#ea4d13")
		plt.show()

	button=Button(root, text="submit", command=run)
	button.pack()
	root.mainloop()

if mode==1:
	def run(multiplier):
		plt.cla()
		for i in range(0,number):
			plt.plot([math.cos((radPerNumber*i)),math.cos((radPerNumber*i*multiplier))],[math.sin((radPerNumber*i)),math.sin((radPerNumber*i*multiplier))], color="#ea4d13")
		plt.show()


	i=.1
	while(i<=100):
		run(i)
		print(i)
		i+=.1
		plt.pause(.01)
else:
	print("use 0 to choose the input and 1 for continuious multiplier")

