#!/usr/bin/python3
# _*_ coding:utf-8 _*_

def flatten(nestedList):
	result = []
	for i in nestedList:
		if isinstance(i,list):
			yield from flatten(i)
		else:
			yield i
	


if __name__ == "__main__":
	nestedList =  [4,[3,[2,[1]]]]
		
	
	temp = flatten(nestedList)
	result=[]
	for i in temp:
		result.append(i)
	print(result)
