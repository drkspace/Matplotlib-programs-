from matplotlib import pyplot as plt
from Tkinter import *
root = Tk()
root.geometry("200x200")
e=Entry(root)
e.pack()
def run():
	plt.cla()
	sideLength=int(e.get())
	for i in range(0,sideLength):
		plt.plot([0,i],[sideLength-i,0])
	for i in range(0,sideLength):
		plt.plot([0,i],[i,sideLength])
	for i in range(0,sideLength):
		plt.plot([i,sideLength],[sideLength,sideLength-i])
	for i in range(0,sideLength):
		plt.plot([sideLength,sideLength-i],[sideLength-i,0])
	plt.show()
button=Button(root, text="submit", command=run)
button.pack()

root.mainloop()
