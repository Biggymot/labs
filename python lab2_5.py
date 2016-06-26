# i=1
# for a in range(0,43):
# 	if a>10:	
# 		print a
# 	i += 1

# for <var> in <list>:
# 	<body_of_loop_1>
# 	<body_of_loop_2>
# 	...
# 	<body_of_loop_N>

# while <condition>:
# 	<body_of_loop_1>
# 	<body_of_loop_2>
# 	...
# 	<body_of_loop_N>

# <condition> = x<5
# 			x<5 and (x>10 or z<10)
# 			(y<10 or y>20) and (x<10)
# 			True

# True 


# for a in range(0,15):
# 	print a
	

# print range(0,15)
# i=1
# for a in range(0,43):
# 	if a<15:	
# 		print a
# 	i += 1

# i=1
# for a in range(16,20):
# 	if a % 2 ==0:
# 		print a
# 	i += 1

# i=1
# for a in range(16,20):
# 	if a % 2 ==0:	
# 		print a
# 	i += 1

# i=1
# for a in range(5,26):
# 	if a % 2 ==0:	
# 		print a
# 	i += 1

# i=1
# for a in range(2,103):
# 	if a % 2 !=0:	
# 		print a
# 	i += 1

# i=1
# for a in range(0,43):
# 	if a % 5 ==0:	
# 		print a
# 	i += 1

# i=1
# while a in range(15,21):
# 	# if a % 3 ==0:	
# 	print a
# 	i += 1

# i=1
# for a in range(5,21):
# 	if not a in range(10,15):
# 		print a
# 	i += 1


# a='Hi'
# b='Bye'
# print a+b+b+a

# a='Yo'
# b='Alice'
# print str(a+b+b+a)

# a='What'
# b='Up'
# print str(a+b+b+a)

# a='Hello'
# print a[1:-1]

# a='java'
# print a[1:-1]

# a='coding'
# print a[1:-1]

# i=1
# #lst = ['Dima', 'Inna', 'Masha', 'Papa']
# lst = ['']
# # if lst:
# #if lst!=[]:
# if len(lst)!=0:
# 	print 'not Empty'
# else:
# 	print 'Empty'

# str = 'a'
# # if str!='':
# # if str:
# if len(str)!=0:
# 	print 'not Empty'
# else:
# 	print 'Empty'

# lst = ['Dima', 'Inna', 'Masha', 'Papa']
# i = 1
# for a in lst:
# 	if lst[1:]:
#  		print ( 'Family number' + ': ' + a)
# 	i += 1

lst = ['Dima', 'Inna', 'Masha', 'Papa', 'Grandmother']
N=len(lst)
i=1
for a in lst:
	if (N-1)==i or N==i:
		if len(a)>4:
			print str(i)+' '+'from'+' '+str(len(lst))+' '+'is'+' '+a+' '+\
			'(elem length is'+' '+	(len(a))+')' 
 	i += 1

# [a,b,c,d,...]
#  1,2,3,4,...

# N=len(lst)
# i=1
# for a in lst:
# 	if len(a)>4:
# 		print str(i)+' '+'from'+' '+str(len(lst))+' '+'is'+' '+a+' '+\
# 		'(elem length is'+' '+str(len(a))+')' 
# 	i += 1

i=1
for a in lst:
	if i in range (1,4):
		if len(a)==4:
			print str(i)+' '+'from'+' '+str(len(lst))+' '+'is'+' '+a+' '+\
			'(elem length is'+' '+str(len(a))+')' 
	i += 1

