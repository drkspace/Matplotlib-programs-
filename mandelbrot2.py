import numpy as np
from PIL import Image
import time
import math
height = 5000
width = 5000
max_value= 1
min_value= -2
break_out=100
data = np.zeros((height+1, width+1, 3), dtype=np.uint8)
#print data
def remap(val, low1, upper1, low2, upper2):
    old_range=upper1-low1
    new_range=upper2-low2
    range_ratio=float(new_range)/old_range
    val-=low1
    return val*range_ratio+low2
def magnitude(x,y):
    return math.sqrt(x*x+y*y)
start_time=time.time()
for x in range(width+1):
    #print a
    for y in range(height+1):
        a=remap(x,0,width,min_value,max_value)
        b=remap(y,0,height,min_value,max_value)
        a0=a
        b0=b
        n=0
        if magnitude(a,b)>2:
            n=break_out
        else:
            while(n<=break_out):
                za=a*a-b*b+a0
                zb=2*a*b+b0
                a=za
                b=zb
                if(magnitude(a,b)>=2):
                    break
                #print n
                n+=1
            
        n=math.log(math.log(n+(1/math.log(2))))*255
        if n>254:
                n=0
        data[y,x]=[0,n,100]
        #print n
    if x != 0 and (float(x)*100/width)%1==0:
        percent = x*100/float(width)
        time_left = (time.time()-start_time)*100/percent 
        print "{}% of the way done at {}\nEstimated compleation time {}\n---------------".format(int(percent),time.strftime("%H:%M:%S %m %d %Y", time.localtime()), time.strftime("%H:%M:%S %m %d %Y", time.localtime(time.time()+time_left)))
img=Image.fromarray(data, 'RGB')
img.save('mandelbrot2.png')
img.show()
