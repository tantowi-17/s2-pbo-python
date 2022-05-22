# PBO with python
# author tantowi
# chapter 6

# FIGURE 6-1
print("-------------FIGURE 6-1-----------------")
myVar = 5
print(myVar)

# FIGURE 6-2
print("-------------FIGURE 6-2-----------------")
Test = 0b100
print("100 binary : ", Test)

Test = 0o100
print("100 octal : ", Test)

Test = 100
print("100 decimal : ", Test)

Test = 0x100
print("100 hexadecimal : ", Test)

print(bin(Test))
print(oct(Test))
print(hex(Test))

# FIGURE 6-3
print("-------------FIGURE 6-3-----------------")
Test = 255.0
print("direct assignment : ", Test)

Test = 2.55e2
print("scientific notation : ", Test)

Test = 2.55e-2
print("negative exponent : ", Test)

# FIGURE 6-4
print("-------------FIGURE 6-4-----------------")
print(ord("A"))

myInt = int("123")
print(myInt)
print(type(myInt))

# FIGURE 6-5
print("-------------FIGURE 6-5-----------------")
myStr = str(1234.56)
print(myStr)
print(type(myStr))

# FIGURE 6-6
print("-------------FIGURE 6-6-----------------")
import datetime as dt
print(dt.datetime.now())

# FIGURE 6-7
print("-------------FIGURE 6-7-----------------")
print(dt.datetime.now().date())


