
def is_leap(year):
    
    if ((year % 4 == 0) and (year % 100 != 0)):
        print("True")
    elif   ((year % 400 == 0) and (year % 100 == 0)):
        print("True")
    else:
        print("false")
        print("{0} is not a multiple of 4 hence its not a leap year".format(year))


x=int(input("please ente a year \n"))
is_leap(x)  