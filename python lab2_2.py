
import math
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])

tail = ''

if z==1:
    tail = '!'
else:
    tail = '.'

couplet = ''

if x==1:
    couplet = 'la'
elif x>1:
    couplet = 'la' + ('-la'*(x-1))

song = ''
#####song = (y-1) * (couplet + ' ') + couplet

song = y * (couplet + ' ') 
song = song[:-1]

print 'Everybody sing a song:' + ' ' + song + tail




