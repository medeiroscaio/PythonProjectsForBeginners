print("Find out if it's a leap year")
year=int(input("Type the year to find out "))

if (year%4==0 and year%100!=0) or (year%400==0):
     print("Leap year")
else:
     print("Not a leap year")