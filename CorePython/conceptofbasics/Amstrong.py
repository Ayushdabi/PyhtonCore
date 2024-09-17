num = 153
temp = 0
num2 = num

while num2 != 0:
    r = num2 % 10
    temp += r*r*r
    num2 //= 10

if temp == num:
    print("ArmStrongNo")
else:
    print("Not ArmStrongNo")