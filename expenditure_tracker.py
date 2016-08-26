import datetime
# import json
import sys
import time
import pickle
import Functions_for_tracker as ft # 내가 만든 함수 저장소 



#expenditure_tracker.py
#프로젝트 시작 날짜 : 2016-06-18
""" 
컴퓨터 시작 시 자동으로 시작되고, 
그래서 매일의 돈 지출의 기록을 기록, 추적할 수 있도록 하는 것이 핵심이다.
간단하게 매일 쓴 돈을 기록하고, 달별로 계산해주는 것을 목표로 한다.
간단한 통계도 가능하게 한다.
"""


# 비밀번호 설정. 내가 아닌 다른 사람이 입력하는 것을 방지한다.
try:
	input_password = sys.argv[1]

except:
	input_password = raw_input("비밀번호를 입력하셔야 합니다. : ")
	for i in range(2):
		if input_password != "696238":
			input_password = raw_input("틀렸습니다. 다시 입력하세요 : ")

	if input_password != "696238":
		sys.exit()
else:
	for i in range(2):
		if input_password != "696238":
			input_password = raw_input("틀렸습니다. 다시 입력하세요 : ")

	if input_password != "696238":
		sys.exit()



# 오늘에 대한 정보 입력. 이후 각각 파일에 저장될 것임.
today = datetime.date.today()






""" 메뉴 선택 기능 Section """
# 기능은 크게 1. 일일 지출금액 추가기능, 2. 특정 날짜 검색 기능, 3. 지난 월별 합계 및 일일 평균 기능,
# 4. 관리자 기능이 있습니다.

print('\n'+'*' * 90+'\n')
print("반갑습니다. 현재 시각", str(datetime.datetime.now())+"입니다.")
print("본 기능은 당신이 용돈지출을 어떻게 하는지 추적하고 그 활용을 돕고자 하는 데 의의가 있습니다.")
print('\n'+'*' * 90+'\n')


while True:
	print("""\n용돈 지출 입력은 1,
특정 날짜 검색 기능 2,
월별 합계 및 일일 평균 기능은 3,
종료는 9를 입력해주세요.""")
	print('\n'+"↓" * 10+'\n')
	menu_selected = raw_input("원하시는 기능을 입력해주세요. : ")

	while menu_selected not in ["1","2","3","9"]:
		menu_selected = raw_input("4가지의 숫자 중 원하시는 것을 정확히 입력해주세요. : ")

#프로그램 종료 사인.
	if menu_selected == "9":
		print("감사합니다. 프로그램을 종료합니다.")
		for i in range(1,4)[::-1]:
			print("종료까지.. "+str(i))
			time.sleep(1)
		sys.exit()

# 파일 업로드 :
	
	with open('daily_expenditure.txt', 'rb') as money:
		try:
			total_record = pickle.load(money)
		except:
			total_record = []
		
	if total_record == []:
		recent_record = [];
	else:
		recent_record = total_record[-1]
	# print(total_record)  <- 테스트용 코드. 정확하게 자료가 입력되었는지 확인한다.


#####################################
#### menu 1. 지출금액 추가 기능. #########
#####################################
	# 기록되는 자료 형식은 다음과 같다. 기록되는 텍스트는 pickle package를 활용하도록 한다.
	""" data_format =  {'today':str(today), 'weekday':ft.which_day(today), 'year':today.year, 'month':today.month, 'day':today.day, 'money_used':10000}"""
	

#### 1.1 - 만약 오늘 처음 금액 지출을 입력한다면 입력되고, 1.2 - 두 번째 이상일 경우 기존 입력된 금액에 추가한다.
	if menu_selected == "1":
		# 1.1 
		if recent_record == [] or recent_record['today'] != str(today):
			print()
			print("\n오늘의 처음 입력이십니다.")
			money_spent = input("오늘 사용하신 금액을 입력해주세요. : ")
			while not money_spent.isnumeric():
				money_spent = input("숫자를 입력하셔야 합니다. 다시 입력하세요 : ")
			money_spent = int(money_spent)

			record = {'today':str(today), 'weekday':ft.which_day(today), 'year':today.year, 'month':today.month, 'day':today.day, 'money_used':money_spent}
			total_record.append(record)
			with open('daily_expenditure.txt', 'wb') as money:
				pickle.dump(total_record, money)

			print('\n')
			# print("현재 시각",datetime.datetime.now()," 오늘 하루 사용하신 금액은 *"+ ft.numberSeparator(record['money_used']),"*원 입력 받았습니다.")
			print("현재 시각",datetime.datetime.now()," 오늘 하루 사용하신 금액은 *{:,}*원 입력 받았습니다.".format(record['money_used']))


		# 1.2
		elif recent_record['today'] == str(today):
			print()
			print("오늘 이미 입력하셨습니다. 이전 지출에 추가됩니다.")
			money_spent = input("오늘 사용하신 금액을 입력해주세요. : ")
			while not money_spent.isnumeric():
				input("숫자를 입력하셔야 합니다. 다시 입력하세요 : ")
			money_spent = int(money_spent)
			recent_record['money_used'] += money_spent
			print("현재 시각",datetime.datetime.now()," 오늘 하루 사용하신 금액은 *{:,}*원 입력 받았습니다.".format(record['money_used']))
			print("*" * 80,'\n')
			
			total_record[-1] = recent_record
			with open('daily_expenditure.txt', 'wb') as money:
				pickle.dump(total_record, money)


#####################################
#### menu 2. 특정 날짜 검색기능.  ########
#####################################
	# 연도, 월, 날짜를 기록하면 그 날에 사용한 금액을 반환한다. 만약 입력값이 없는 곳이라면 '없다'고 반환한다.(0원이 아니다.) 

	# 2.1 정확한 날짜 입력 받기.
	if menu_selected == "2":
		print()
		print("특정 날짜 검색 기능입니다. 원하시는 날짜를 입력해주시면 그 날의 지출액을 알려드립니다.")
		day_input = input("'2016-04-01'과 같은 형식으로 날짜를 입력해주세요 : ")
 
		while not ft.checkRightFormat(day_input):
			# 형식이 맞는지 조사. 하나의 조건이라도 안 맞으면 no way..

			if day_input == '오늘' or day_input == 'today':
				day_input = str(today)
				break
			elif day_input =="어제" or day_input == 'yesterday':
				day_input = str(datetime.date(today.year, today.month, today.day - 1))
				break
			day_input = input("형식을 지켜 다시 입력해주세요 : ")

	# 2.2 json 파일에서 해당 날짜 있는지 검사.
		input_year = int(day_input[:4])
		input_month = int(day_input[5:7])
		input_day = int(day_input[-2:]) # 이 값들은 입력받은 값으로 문자열이다. 반면 내가 갖고 있는 정보는 숫자. 통일이 필요.
		asked_record = None
	
	# 맞는 값을 찾았음.
		for record in total_record:
			if record['year'] == input_year and record['month'] == input_month  \
			and record['day'] == input_day:
				asked_record = record
				break

		if asked_record is None:
			print("이 날은 기록이 남아있지 않습니다.")
			print("\n________________________________")
		else:
			print("\n##############################")
			print("요청하신",asked_record['today']+"일은 *"+asked_record['weekday']+"*이고 지출하신 금액은 *\
{:,}*원입니다.".format(asked_record['money_used']))
			print("\n##############################\n")


#####################################
### menu 3. 월별 합계 및 일일 평균 기능. ###
#####################################
	# 3.1 월별 합계 및 평균, 3.2 요일별 평균. 
		"""
		monthly_total = {
							'2016' : {'1' : [0,0], '2': [0,0], '3': [0,0], '4': [0,0], '5':[0,0]\
							'6':[0,0], '7':[0,0], '8':[0,0], '9':[0,0], '10':[0,0], '11':[0,0], '12':[0,0]},
							
						}
		years = ['2016', '2017', '2018']
		위와 같은 형식. 월의 첫번째 인자는 금액, 두 번째 인자는 입력된 날짜이다.				 
		""" 

	# 만약 3번 기능을 요청 받았다면,
	if menu_selected == "3":



		# 3.0 자료 셋 만들기
		monthly_total = {}
		years = []

		for i, record in enumerate(total_record):
			if i == 0:
				year = str(record['year'])
				monthly_total[year] = ft.makeYearDict()
				monthly_total[year][str(record['month'])][0] += record['money_used']
				monthly_total[year][str(record['month'])][1] += 1
				if str(record['year']) not in years:
					years.append(str(record['year']))

			elif total_record[i]['year'] != total_record[i-1]['year']:
				year = str(record['year'])
				monthly_total[year] = ft.makeYearDict()
				monthly_total[year][str(record['month'])][0] += record['money_used']
				monthly_total[year][str(record['month'])][1] += 1
				if str(record['year']) not in years:
					years.append(str(record['year']))
			else:
				monthly_total[year][str(record['month'])][0] += record['money_used']
				monthly_total[year][str(record['month'])][1] += 1
				if str(record['year']) not in years:
					years.append(str(record['year']))
		print(monthly_total)
		print(years)


		# 3.1 월별 합계 및 평균
		for year in years:
			print("\n"+year +"연도의 월별 지출액, 입력일수, 하루 평균 지출액을 말씀드리겠습니다.\n")
			for month in range(1,13):
				if monthly_total[year][str(month)][0] == 0:
					pass
				else:
					print("  "+str(month) + "월별의 총 지출액은 *{:,}*원이고 입력해주신 날 수는 *".format(monthly_total[year][str(month)][0])  \
									+ str(monthly_total[year][str(month)][1])+"*일입니다. 일일 평균 *{:,}\
									*원 사용하셨습니다.".format(int(str(int(monthly_total[year][str(month)][0]) // int(monthly_total[year][str(month)][1])))))
			print("\n")					

		
		# 3.2 요일 별 평균 내기.
		weekday_total = {'월요일':[0,0], '화요일': [0,0], '수요일': [0,0], '목요일': [0,0],\
		 '금요일': [0,0], '토요일': [0,0], '일요일': [0,0]}
		weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
		# 요일 별로 저장할 변수 지정. 요일의 value 값은 첫번째는 총 사용한 금액, 두 번째는 평균을 내기 위해 사용할 일수이다.

		for record in total_record:
			weekday_total[record['weekday']][0] += record['money_used']
			weekday_total[record['weekday']][1] += 1

		print("\t요일별 사용한 금액을 말씀드리겠습니다.")
		for i, weekday in enumerate(weekday_total):
			try:
				print(weekdays[i], "-"*4+"> 총금액 : *{:,}*원, ".format(weekday_total[weekdays[i]][0]) \
					+"평균 : {:,}원".format(weekday_total[weekdays[i]][0] // weekday_total[weekdays[i]][1]))
			except ZeroDivisionError:
				print(weekdays[i], "-"*4+"> 총금액 : "+ "0원, " +"평균 :", "0원")
		print('\n')




#####################################
### menu 4. 관리자 기능. ###
#####################################

