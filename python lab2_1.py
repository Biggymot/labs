import math
import sys


for i in range(1,10):
	row = ""
	for j in range(1,i+1):
 		row += str(i*j)+"\t"
 	print row

for i in range(1,10):
 	print 'a'*i


# 1
# 1
# 1 2
# 1 2
# 1
# 1
# 1 2
# 1 2 3
# 1 2 3
# 1 2
# 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# for i in range(1,5):
# 	print_pyramid(i)


# i = 1
# while i<N:
#     <action>
#     i += 1

# while <condition>:
# 	<body>

# for <elem> in <list>:
# 	<body>