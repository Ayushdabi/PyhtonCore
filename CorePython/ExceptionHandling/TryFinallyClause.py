def hello():
    try:
        c = 100
        return (print(c))
    finally:
        return 2
k = hello()
print(k)