from matplotlib import pyplot as plt
from Tkinter import *
import time
import math
import sys
mode=int(sys.argv[1])
toWrite = False
if(sys.argv[2] is not None):
	toWrite = sys.argv[2] is "1"
tau=2*math.pi
number=100
radPerNumber=tau/number
plt.ion()
plt.axis('off')
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)

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
	def p1():
		tmp = float(e.get())
		e.delete(0,len(e.get()))
		e.insert(0, tmp+1)
		run()
	def m1():
		tmp = float(e.get())
		e.delete(0,len(e.get()))
		e.insert(0, tmp-1)
		run()
	
	button=Button(root, text="submit", command=run)
	button2 = Button(root, text='+1', command=p1)
	button3 = Button(root, text='-1', command=m1)
	button.pack()
	button2.pack()
	button3.pack()
	root.mainloop()

if mode==1:
	def run(multiplier):
		plt.cla()
		for i in range(0,number):
			plt.plot([math.cos((radPerNumber*i)),math.cos((radPerNumber*i*multiplier))],[math.sin((radPerNumber*i)),math.sin((radPerNumber*i*multiplier))], color="#ea4d13")
		plt.show()
		if toWrite:
			plt.savefig("images/{}.png".format(multiplier), dpi = 'figure', bbox_inches='tight')


	i=0
	while(i<=100):
		run(i)
		print(i)
		i+=.1
		plt.pause(.01)
		if i == 100:
			i = 0
else:
	print("use 0 to choose the input and 1 for continuious multiplier")

