import sys


lst=[1,2,-5,6,-4,-7,7,-9,-5,4]
lst2=[1,2,-5,6,-4,-7,7,-9,-5,4,0]
lst3=[1,2,-5,6,-4,-7,7,-9,-5,4,'a']
lst4=[1,2,-5,6,-4,-7,7,-9,-5,4,{'vanya' : 23323, 'smith' : 6565}]
lst5=[1,2,-5,6,-4,-7,7,-9,-5,4,[1,2,5]]
lst6=[1,2,-5,6,-4,-7,7,-9,-5,4,1.2]
lst7=[1,2,5,6,4,4]
lst8=[-1,-2,-5,-6,-4,-4]
lst9=[0,0,0]
lst10=[]

test_input_list = [
	{"test_list" : lst, "expected_result" : -10},
	{"test_list" : lst2, "expected_result" : -10},
	{"test_list" : lst3, "expected_result" : -10},
	# {"test_list" : lst4, "expected_result" : -10},
	# {"test_list" : lst5, "expected_result" : -10},
	{"test_list" : lst6, "expected_result" : -8.8},
	{"test_list" : lst7, "expected_result" : 22},
	{"test_list" : lst8, "expected_result" : -22},
	{"test_list" : lst9, "expected_result" : 0},
	{"test_list" : lst10, "expected_result" : 0}
]


def calc_diff(lst):
	negative = 0
	positive = 0
	for i in lst:
		if i<0:
			negative += i
		if i>0:
			positive += i
	difference = positive + negative
	return difference
print calc_diff(lst)


for test_dic in test_input_list:
	exp_result = test_dic.get('expected_result')
	test_list  = test_dic.get('test_list')
	if calc_diff(test_list) == exp_result:
		print "TEST PASSED"
	else:
		print "TEST FAILED for " + str(test_list)