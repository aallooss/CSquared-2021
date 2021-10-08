# authored by    >Haden Sangree<    for    >Coding with Character Camp<
# Lesson 10

#for the firt part of our rick paper scissors game we will import randint
#from the random library

from math import radians
from random import randint

#next create an array... name it whatever you like

t = ["Rock", "Paper", "Scissors"]

cpu = t[randint(0,2)]

#print cpu output to test
print(cpu)