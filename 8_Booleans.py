# authored by    >Haden Sangree<    for    >Coding with Character Camp<
# Lesson 8

#  import practice
import math

#  variables practice
num1 = 1
num2 = 10
num3 = 4.5
answer = 0

 #  strings practice
ceil = "The answer rounded up is: "
floor = "The number rounded down is: "

#  operators practice
answer = num1 + num2/2 * num3

print(math.floor(answer))
if (math.floor(answer) % 2) == 0:           # % is a modulus which divides input and return the remainder
    print("It IS divisiable by two yayyyy")
else:
    print("NOT divisiable by two :(")
