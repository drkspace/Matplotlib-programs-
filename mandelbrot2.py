import numpy as np
from PIL import Image
import math
height = 100000
width = 100000
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
    NewValue=val*range_ratio+low2
    return NewValue
def magnitude(x,y):
    c2 = x*x+y*y
    c = math.sqrt(c2)
    return c
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
        data[y,x]=[0,n,0]
        #print n

img=Image.fromarray(data, 'RGB')
img.save('mandelbrot2.png')
img.show()
