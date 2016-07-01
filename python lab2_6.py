import math
import sys

def myAbs(number):
	if number<0:
		return number*(-1)
	else:
		return number

a=float(sys.argv[1])
b=float(sys.argv[2])
x = True
if a==6 or b==6 or (a+b)==6 or myAbs(a-b)==6:
    x = True
else:
    x = False
print x

a=float(sys.argv[1])
b=float(sys.argv[2])
x=''
if (a+b)>10 and (a+b)<19:
	x = 20
else:
	x = (a+b)
print x

a = 1
b = 2
print str(a)+'+'+str(b)+'='+str(a + b)



