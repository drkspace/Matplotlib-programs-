import numpy as np
from PIL import Image
import math
height = 4000
width = 4000
max_value=2
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
for x in range(width+1):
    #print a
    for y in range(height+1):
        a=remap(x,0,width,min_value,max_value)
        b=remap(y,0,height,min_value,max_value)
        a0=a
        b0=b

        n=0
        while(n<break_out):
            za=a*a*a-3*a*b*b+a0
            zb=3*a*a*b-b*b*b+b0
            a=za
            b=zb
            if((a*a+b*b)>4):
                break
            #print n
            n+=1
        n=int(remap(n,0,break_out,255,0))
       # print y
        data[y,x]=[n,n,n]
        #print n

img=Image.fromarray(data, 'RGB')
img.save('mandelbrot3.png')
img.show()
