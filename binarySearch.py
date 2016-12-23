#! /usr/bin/python3
# _*_ coding:utf-8 _*_

def binary_search(T,target):
	start,end = 0, len(T)-1
	while end >=start:
		if target == T[(start+end)//2]:
			return ((start+end)//2,True)
		elif target > T[(start+end)//2]:
			start = (start+end)//2 + 1
		else:
			end= (start+end)//2 - 1
	return (0,False)

if __name__ =="__main__":
	test_list=[1,2,3,4,5,6,7,8,9]
	print(binary_search(test_list,5))
