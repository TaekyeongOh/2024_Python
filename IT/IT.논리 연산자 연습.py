year= int(input("연도: "))
print((year%400==0) or (year%4==0 and year%100!=100))
