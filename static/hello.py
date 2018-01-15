#!/usr/bin/python
a = input("num1:")
b = input("num2:")
c = input("num3:")
max_num = 0;
if a > b:
    max_num = a;
    if max_num > c:
        print("max_num"+max_num)
    else:
        print("max_num"+c)
else:
    max_num = b;
    if max_num > c:
        print("max_num"+max_num)
    else:
        print("max_num"+c)

