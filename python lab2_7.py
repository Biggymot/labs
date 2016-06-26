import math
import sys

# lst = ['Dima', 'Inna', 'Masha', 'Papa']
# Y=len(lst)
# i=1
# for a in lst:
# 	if (Y-2)==i or (Y-1)==i or Y==i:
# 		print str(i)+' '+'from'+' '+str(len(lst))+' '+'is'+' '+a+' '+\
# 		'(elem length is'+' '+str(len(a))+')' 
	# i += 1


# def get_last_elems_of_list(lst, x):
# 	n=len(lst)
# y=x
# i=1
# for a in lst:
# 	if y!=0:
# 		if n==i or n==(i-y):
# 			print str(i)+' '+'from'+' '+str(len(lst))+' '+'is'+' '+a+' '+\
# 			'(elem length is'+' '+str(len(a))+')'
# 	i+=1
# 	y-=1

# get_last_elems_of_list(['Dima', 'Inna', 'Masha', 'Papa'], 2)



# def combo_string(string1, string2, value):
# 	if len(string1)>len(string2):
# 		print string2+string1+string2
# 	if len(string1)<len(string2):
# 		print string1+string2+string1

# combo_string('Hello', 'hi', False)# 'hiHellohi'
# combo_string('hi', 'Hello', True)# 'hiHellohi'
# combo_string('aaa', 'b', True)# 'baaab'

# def <name_of_function>(<name_of_1st_param>, <name_of_2nd_param>, ... <name_of_Nth_param>):
# 	<function_body_line_1>
# 	<function_body_line_2>
# 	...
# 	<function_body_line_N>

# def myAbs(number):
# 	if number<0:
# 		return number*(-1)
# 	else:
# 		return number

# print myAbs(-1)*3
# 1 from 4 is Dima (elem length is 4)
# 2 from 4 is Inna (elem length is 4)
# 3 from 4 is Masha (elem length is 5)

# def in1to10 (n, outside_mode):
# 	if outside_mode == True:
# 		if n in range (1,11):
# 			return False
# 		else:
# 			return True
# 	if outside_mode == False:		
# 		if n in range (1,11):
# 			return True
# 		else:
# 			return False	
# print in1to10(5, False)

# in1to10(5, False) # True
# in1to10(11, False) # False
# in1to10(11, True) # True
# in1to10(5, True) # False

# def cigar_party(cigars, is_weekend):
# 	if is_weekend == True:
# 		if cigars>40:
# 			return True
# 		else:
# 			return False
# 	if is_weekend == False:
# 		if cigars in range (40,61):
# 			return True
# 		else:
# 			return False
# print cigar_party (30, False) #False
# print cigar_party(50, False) # True
# print cigar_party(70, True) # True		


# def squirrel_play(temp, is_summer):
# 	if is_summer == False:
# 		if temp in range (60,91):
# 			return True
# 		else:
# 			return False
# 	if is_summer == True:
# 		if temp in range (60,101):
# 			return True
# 		else:
# 			return False
# print squirrel_play(70, False) # True
# print squirrel_play(95, False) # False
# print squirrel_play(95, True) # True

# def alarm_clock(day, vacation):
# 	if vacation == True:
# 		if day in range (1,6):
# 			return '10:00'
# 		else:
# 			return 'off'
# 	if vacation == False:
# 		if day in range (1,6):
# 			return '7:00'
# 		else:
# 			return '10:00'	
# print alarm_clock(1, False) # '7:00'
# print alarm_clock(5, False) # '7:00'
# print alarm_clock(0, False) # '10:00'

# def caught_speeding(speed, is_birthday):
# 	if is_birthday == True:
# 		if speed in range(0,66):
# 			return '0'
# 		if speed in range(66,86):
# 			return '1'
# 		if speed>86:
# 			return '2'
# 	if is_birthday == False:
# 		if speed in range(0,61):
# 			return '0'
# 		if speed in range(61,81):
# 			return '1'
# 		if speed>81:
# 			return '2'
# print caught_speeding(60, False) # 0
# print caught_speeding(65, False) # 1
# print caught_speeding(65, True) # 0

# def lone_sum(a, b, c):
# 	if a!=b and a!=c and b!=c:
# 		return a+b+c
# 	if a==b and a==c:
# 		return 0
# 	if a==b and a!=c:
# 		return c
# 	if a!=b and a==c:
# 		return b
# 	if a!=b and b==c:
# 		return a

# print lone_sum(1, 2, 3) # 6
# print lone_sum(3, 2, 3) # 2
# print lone_sum(3, 3, 3) # 0

# def close_far(a, b, c):
#   cond1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
#   cond2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
#   return cond1 or cond2

# print close_far(1, 2, 10) # True
# print close_far(1, 2, 3) # False
# print close_far(4, 1, 3) # True

# def first_half(str):
# 	x=len(str)/2
# 	return str[:x]
# print first_half('WooHoo') # 'Woo'
# print first_half('HelloThere') # 'Hello'
# print first_half('abcdef') # 'abc'

# def make_out_word(out, word):
# 	x=len(out)/2
# 	return out[:x]+word+out[x:]
# print make_out_word('<<>>', 'Yay') # '<<Yay>>'
# print make_out_word('<<>>', 'WooHoo') # '<<WooHoo>>'
# print make_out_word('[[]]', 'word') # '[[word]]'

# def reverse3(nums):
# 	return list(reversed(nums))
# print reverse3([1, 2, 3]) # [3, 2, 1]
# print reverse3([5, 11, 9]) # [9, 11, 5]
# print reverse3([7, 0, 0]) # [0, 0, 7]

# def count_evens(nums):
# 	list1=[]
# 	for x in nums:
# 		if x % 2 ==0:
# 			list1.append(x)
# 	return len(list1)
# print count_evens([2, 1, 2, 3, 4]) # 3
# print count_evens([2, 2, 0]) # 3
# print count_evens([1, 3, 5]) # 0

# def count_evens(nums):
# 	i=0
# 	for x in nums:
# 		if x % 2 ==0:
# 			i+=1
# 	return i
# print count_evens([2, 1, 2, 3, 4]) # 3
# print count_evens([2, 2, 0]) # 3
# print count_evens([1, 3, 5]) # 0

# def lucky_sum(a, b, c):
# 	list = [a,b,c]
# 	sum=0
# 	for x in list:
# 		if x == 13:
# 			return sum
# 		else:
# 			sum +=x 
# 	return sum
# print lucky_sum(13, 1, 3) # 0
# print lucky_sum(1, 2, 3) # 6
# print lucky_sum(1, 2, 13) # 3
# print lucky_sum(1, 13, 3) # 1

# def lucky_sum(a, b, c):
# 	if a==b==c==13:
# 		return 0
# 	if a==13:
# 		return 0
# 	if b==13:
# 		return a
# 	if c==13:
# 		return a+b
# 	else:
# 		return a+b+c
# print lucky_sum(13, 1, 3)
# print lucky_sum(1, 2, 3) # 6
# print lucky_sum(1, 2, 13) # 3
# print lucky_sum(1, 13, 3) # 1

# def extra_end(str):
# 	return str[-2:]*3
# print extra_end('Hello') # 'lololo'
# print extra_end('ab') # 'ababab'
# print extra_end('Hi') # 'HiHiHi'

# def date_fashion(you, date):
# 	if you<=2 or date<=2:
# 		return 0
# 	if you>=8 or date>=8:
# 		return 2
# 	else:
# 		return 1
# print date_fashion(5, 10) # 2
# print date_fashion(5, 2) # 0
# print date_fashion(5, 5) # 1



[1,2,3,4]
["a","b"]
[[1,2,3], ["a","b"], "z", {"a":"b"}]

{
	"Name" : "Dmytro",
	"Surname" : "Bogach",
	"Phones" : ["+38067...", "+093..."],
	"Wife" : {
				"Name" : "Inna",
				"":""
			 }
}


{} => curly brackets
[] => square brackets
#  => sharp
:  => colon
;  => semicolon
_  => underscore
...=> elipsis
() => paranthesis, round brackets
"" => double qoutes
'' => single qoutes


def my_sum(lst):
	sum=0
	for a in lst:
 		sum += a
 	return sum

def sum2(nums):
	return sum(nums[:2])

	# sum=0
	# i=1
	# for a in nums:
 # 		if i==1 or i==2: 
 # 			sum += a
 # 		# else:
 # 		# 	break
 # 		# print str(i) + "th elem is " + str(a)
	# 	i+=1
	# return sum

print sum2([1, 2, 3]) # 3
print sum2([1, 1]) # 2
print sum2([1, 1, 1, 1]) # 2
