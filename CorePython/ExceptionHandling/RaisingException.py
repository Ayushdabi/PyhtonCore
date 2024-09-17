number   = int(input("Enter your  Number :"))
if number  > 10:
    raise Exception('x should not exceed 10. The value of number  was: {}'.format(number))