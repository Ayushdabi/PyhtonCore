while True:
     try:
         x = int(input("Please enter a number: "))
         print("%s squared is %s"% (x,x*5))
     except ValueError:
         print()
