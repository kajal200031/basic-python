a=input("enter a name:")
b=input("enter a father name:")
c=input("enter a mother name:")
import datetime 
x=datetime.datetime(year=int(input("enter the birth year:")),month=int(input("enter the birth month:")),day=int(input("enter the birth day:")))
print(x.year)
print(x.strftime("%A"))#weekday for long
print(x.strftime("%a"))#weekday for short
print(x.strftime("%w"))#weekday as a number
print(x.strftime("%d"))#day of month
print(x.strftime("%b"))#month name short version
print(x.strftime("%B"))#month name long version

