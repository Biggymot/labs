import sys

# f = open("tete", 'w+')
# #f.write(str(1) + "\t" + str(1**2) + "\t" + str(1**3) + "\n")
# i=1
# for i in range(1,11):
# 	f.write("%d\t%d\t%d\n" % (i, i**2, i**3))
# 	i += 1
# f.close()
# f = open("tete", 'a')
# i=1
# for i in range(11,21):
# 	f.write("%d\t%d\t%d\n" % (i, i**2, i**3))
# 	i += 1
# f.close()
# f = open("tete", 'r')
# print f.read()

# while (i<10):
# 	f.write("Dima Bogach \n")
# 	i += 1

# f.write('Dima')
# f.seek(4)
# buffer = f.read()
# f.seek(4)
# f.write('Bogach ')
# f.write(buffer)

# f.close()
# f.write('qwerty')
# read()


# print "word_count"

# word_count = {}

# file = open("Games.txt", 'r')
# file_content = file.read()
# print file_content[:10]
# i=0
# for symbol in file_content:
# 	print symbol
# 	if word_count.has_key(symbol):
# 		word_count[symbol] +=1
# 	else:
# 		word_count[symbol] = 1

# for symbol in sorted(word_count, key=word_count.get):
# 	print "%s: %d" % (symbol, word_count[symbol])
# file.close()

import os

# def print_dir(path, depth_level):
# 	lst = os.listdir(path)
# 	for path_entry in lst:
# 		if (os.path.isfile(path_entry)):
# 			print "\t"*depth_level + path_entry
# 		else:
# 			print path_entry
# 			print_dir(path_entry, depth_level+1)

# print_dir(os.getcwd(), 0)

# for file in os.listdir(cwd):
# 	print file
# words = file_content.split()
# wordcount = len(words)
# print 'Wordcount:', wordcount

file = open('about.txt')
# text = file.read()
# list_of_words = text.split()
# print (len(list_of_words))
# total_lines = 0
# total_words = 0
# for line in file:
#    # total_lines += 1
#     word_boundary = 0 # 0 - "SPACE" state, 1 - "WORD" state
#     for symbol in line:
#         if symbol != ' ' and word_boundary == 0:
#             total_words += 1
#             word_boundary = 1
#         elif symbol == ' ':
#             word_boundary = 0
# print(total_words,'words')
total_words = 0


# for line in file:
# 	word_boundary = 0
# 	for symbol in line:
# 		if symbol != ' ' and word_boundary == 0:
# 			total_words += 1
# 			word_boundary = 1
# 		elif symbol == ' ':
# 			word_boundary = 0


SPACE = 0
WORD = 1

for line in file:
	state_of_words = SPACE
	for symbol in line:
		if state_of_words == SPACE:
			if symbol != ' ':
				state_of_words = WORD

		elif state_of_words == WORD:
			if symbol == ' ':
				total_words += 1
				state_of_words = SPACE
	total_words += 1

print(total_words,'words')


# file = open('about.txt')
# # total_lines = 0
# total_sentences = 0
# for line in file:
#    # total_lines += 1
#     sentence_boundary = 0 # 0 - "SPACE" state, 1 - "WORD" state
#     for symbol in line:
#         if symbol != '.' != '!' != '?' and sentence_boundary == 0:
#             total_sentences += 1
#             sentence_boundary = 1
#         elif symbol == '.' == '!' == '?':
#             sentence_boundary = 0
# print(total_sentences,'sentences')
file.close()


f = open("aaa", 'w+')
for i in range(1,21):
	f.write("a")
f.close()
f = open("aaa", 'r')
print f.read()

f = open("aaa", 'r+')
step = 1
for i in range(1,21):
	f.seek(step)
	buffer = f.read()
	f.seek(step)
	f.write("b")
	f.write(buffer)
	step += 2
f.close()
f = open("aaa", 'r')
print f.read()

f = open("aaa", 'r+')
step = 1
for i in range(1,21):
	f.seek(step)
	buffer = f.read()
	f.seek(step)
	f.write("bb")
	f.write(buffer)
	step += 3
f = open("aaa", 'r')
print f.read()

f = open("aaa", 'r+')
step = 1
for i in range(1,21):
	f.seek(step)
	buffer = f.read()
	f.seek(step)
	f.write("bbbb")
	f.write(buffer)
	step += 5
f = open("aaa", 'r')
print f.read()

f = open("aaa", 'r+')
step = 1
delta = 1
for i in range(1,21):
	f.seek(step)
	buffer = f.read()
	f.seek(step)
	f.write("b"*i)
	f.write(buffer)
	delta += 1
	step += delta
f = open("aaa", 'r')
print f.read()

f = open("aaa", 'r+')
step = 0
delta = 1
for i in range(1,21):
	step += delta
	f.seek(step) #1, 3
	buffer = f.read()
	f.seek(step) #1, 3
	for i in range(1,21):
		f.write("b"*i)
		f.write(buffer)
 	delta =	range(2,21)
 	f = open("aaa", 'r')
print f.read()



f = open("pyramid_a", 'w+')
for i in range(1,21):
	f.write("a"*i)
	print "a"*i
f = open("pyramid_a", 'r')


f = open("pyramid", 'w+')
for i in range(1,21):
	row = ""
	for j in range(1,i+1):
 		row += str(j)+"\t"
 	print row
f = open("pyramid", 'r')

for i in range(1,9):
	row =""
	for j in 'abcdefgh':
 		row += str(i) + j + "\t"
 	print row


for i in range(-9,0):
	print abs(i)

def make_row(length, symbol):
	row = ""
	for j in range(1,length+1):
		row += str(symbol)+"*"
	print row

def pyramid (height, symbol):

	for i in range(1,height):
		make_row(i, symbol)

	make_row(height, symbol)

	for i in range(-(height)+1,0):
		make_row(abs(i), symbol)

for i in range(1,5):
	pyramid (i, '.')

