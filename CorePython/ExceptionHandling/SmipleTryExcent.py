try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    num3 = num1/num2;
    print("num1/num2 = ",num3)
except ZeroDivisionError as e:
    print("can't divide by zero", e)
else:
    print("Hi I am else block")

finally:
    print("i am finally")