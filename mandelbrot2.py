import numpy as np
from PIL import Image
import time
import math
height = 10000
width = 10000
max_value= 2
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
itterations=0
for x in range(width+1):
    
    for y in range(height+1):
	
        a=remap(x,0,width,min_value,max_value)
        b=remap(y,0,height,min_value,max_value)
        n=0
        if (a*a+b*b)>4:
            itterations+=1
            n=break_out
        else:
            a0=a
            b0=b
            while(n<break_out):
                itterations+=1
                za=a*a-b*b+a0
                zb=2*a*b+b0
                a=za
                b=zb
                if((a*a+b*b)>4):
                    break
                
                n+=1
            
        #n=math.log(math.log(n+(1/math.log(2))))*255
        n=int(remap(n,0,break_out,255,0))
        
        if n>255:
                n=0
        data[y,x]=[n,n,n]
        
    if x != 0 and (float(x)*100/width)%1==0:
        percent = x*100/float(width)
        cur_time=time.time()
        time_left = (cur_time-start_time)*(100/percent-1) 
        print "{}% of the way done at {}\nEstimated compleation time {}\n---------------".format(int(percent),time.strftime("%H:%M:%S %m %d %Y", time.localtime()), time.strftime("%H:%M:%S %m %d %Y", time.localtime(cur_time+time_left)))
print("Total itterations on a {} by {} board with a max itteration break of {}: {} itterations".format(width,height,break_out,itterations))
print("\n\nYour itterations per second score is {}".format(itterations/(time.time()-start_time)))
img=Image.fromarray(data, 'RGB')
img.save('test.png')
img.show()
