num1 = int(input("hour1"))
num2 = int(input("min1"))
num3 = int(input("sec1"))
num4 = int(input("hour2"))
num5 = int(input("min2"))
num6 = int(input("sec2"))

result = (((num1 - num4) * 3600) + ((num2 - num4) * 60) + (num3 - num6))

print(abs(result))