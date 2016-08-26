# -*- coding: utf-8 -*-
# Function for expenditure_tracker.py


# 해당 날짜가 어떤 요일인지 출력한다.
def which_day(date): 						# 입력한 날짜가 무슨 요일인지 반환하는 함수.
	try:
		return ['월요일', '화요일','수요일','목요일','금요일','토요일','일요일'][date.weekday()]
	except:
		return -1


# 입력 받은 날짜가 올바른 형식인지 조사한다.
# 2016-04-01 -> 총 10개의 글자수
def checkRightFormat(str):
# 	try:
# 		if str[0:4].isnumeric() and str[4] == '-' and str[5:7].isnumeric() \
# and str[7] == '-' and str[-2:].isnumeric() and len(str) == 10:
# 			return True
# 		else:
# 			return False
# 	except:
# 		return False
	try:
		if str[0:4].isnumeric() and str[4] == '-' and str[5:7].isnumeric() and str[7] == '-' and str[-2:].isnumeric() and len(str) == 10:
			return True
		else:
			return False
	except IndexError:
		print("제대로 된 형식으로 입력하지 않으셨습니다.")
		return False
	except:
		print("문제가 있습니다.")
		return False






# 받은 숫자값에 천 자리마다 ','를 붙여서 반환한다.
def numberSeparator(number):
	if isinstance(number,int):
		number = str(number)
	elif number.isnumeric():
		pass
	else:
		return -1

	# 일단 처음 나눈다.
	try:
		number = number[:-3] + ',' + number[-3:]
	except:
		return number


	while True:
		testSet = number.split(',')
		# 만약 모두가 조건을 만족한다면
		if all( map(lambda x: len(x) < 4, testSet)):
			return number
		else:
			location = number.find(',')
			number = number[:location-3] + ',' + number[location-3:]

"""
형식 ->  '2016' : {'1' : [0,0], '2': [0,0], '3': [0,0], '4': [0,0], '5':[0,0]\
							'6':[0,0], '7':[0,0], '8':[0,0], '9':[0,0], '10':[0,0], '11':[0,0], '12':[0,0]},
"""

def makeYearDict():
	format = {'1':[0,0], '2':[0,0], '3':[0,0], '4':[0,0], '5':[0,0], '6':[0,0], '7':[0,0], '8':[0,0], '9':[0,0], '10':[0,0], '11':[0,0], '12':[0,0]}
	return format
