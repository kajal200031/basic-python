#if-elif-else
#1 students marks
marks=int(input("enter the marks:"))
if 90<marks<=100:
    print("first grades")
elif 80<marks<=90:
    print("second grades")
elif 70<marks<=80:
    print("third grades")
elif 33<marks<=70:
    print("pass")
else:
    print("fail")
#2 greatest among two number
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if n1>n2:
    print("n1 is greatest")
elif n2>n1:
    print("n2 is greatest")
else:
    print("both number are equal")

#3 greatest among three number
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print("n1 is greatest number")
elif n2>n1 and n2>n3:
    print("n2 is greatest number")
elif n3>n1 and n3>n2:
    print("n3 is greatest number")
else:
    print("both are equal")

#4 type of variable
var1=2+3j
if (type(var1)==int):
    print("type of variable is integer:")
elif (type(var1)==float):
    print("type of variable is float:")
elif (type(var1)==complex):
    print("type of variable is complex:")
elif (type(var1)==bool):
    print("type of variable is bool:")
elif (type(var1)==str):
    print("type of variable is string:")
elif (type(var1)==tuple):
    print("type of variable is tuple:")
elif (type(var1)==list):
    print("type of variable is list:")
elif (type(var1)==dict):
    print("type of variable is dictionary:")
else:
    print("not defined")

#5 print weekdays
n5=int(input("enter the number:"))
if n5==1:
    print("sunday")
elif n5==2:
    print("Monday")
elif n5==3:
    print("Tuesday")
elif n5==3:
    print("wednesday")
elif n5==4:
    print("Thursday")
elif n5==6:
    print("Friday")
elif n5==7:
    print("Saturday")
else:
    print("write a number between 1 to 7")

#atm
print("enter your card")
pin=int(input("please enter your pin:"))
loc=input("enter the location:")
if loc== "withdrawl cash":
        print("please collect your cash")
elif loc=="balance enquiry":
    print("your ammount is 476528")
elif loc=="mini statement":
    print("check your statement")
elif loc=="pin change":
    print("pin changed successfully")
elif loc=="pin generation":
    print("pin generation successfully")
else:
    print("your transaction is invalid 'please collect your card'")


