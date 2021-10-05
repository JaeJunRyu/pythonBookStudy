#날짜 시간 관련 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구하고
#쉽게 사용할 수 있게 월을 변수에 저장합니다.
now = datetime.datetime.now()
month = now.month

#조건문으로 계정을 확인합니다.
if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
else:
    print("겨울")