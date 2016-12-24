#! /usr/bin/python3
# _*_ coding:utf-8 _*_

def searchMatrix(matrix,target):
	i,j = 0,len(matrix[0])-1
	m = len(matrix)
	while i < m and j >=0:
		if target == matrix[i][j]:
			return True
		elif target > matrix[i][j]:
			i++
		else:
			j--
	return False



if __name__ == "__main__":
	s=[
		[1,3,5,7],
		[10,11,16,20],
		[23,30,34,50]
	]
	print(searchMatrix(s,3))
