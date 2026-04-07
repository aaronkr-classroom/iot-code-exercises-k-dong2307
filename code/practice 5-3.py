class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def is_leap(self):
        return (self.year & 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def month_days(self):
        days = [31, 28 + self.is_leap(), 31, 30, 31, 30, 31, 31, 30, 31 , 30, 31]
        return days
    
    def days(self):
        md = self.month_days()
        return sum(md[:self.month - 1]) + self.day
    
    def days_left(self):
        total = 366 if self.is_leap() else 365
        return total - self.days()
    
    def weekday(self):
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m += 12
            y -= 1
            
        K = y % 100
        J = y // 100
        h = (d + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
        return h
    
    def weekday_name(self):
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]
    
while True:
    year = int(input("연도 입력: "))
    month = int(input("월 입력: "))
    day = int(input("일 입력: "))
        
    s = SayDays(year, month, day)
        
    print("days:", s.days())
    print("days_left:", s.days_left())
    print("weekday:", s.weekday())
    print("weekday_name:", s.weekday_name())
    print("-" * 30)