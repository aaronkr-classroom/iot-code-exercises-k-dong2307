month = int(input("월 입력: "))
day = int(input("일 입력: "))

if (month == 8 and day == 15):
    print("광복절")
elif (month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")

