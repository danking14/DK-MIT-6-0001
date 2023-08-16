import math
import numpy

x = input("Enter number x: ")
y = input("Enter number y: ")

int_x = int(x)
int_y = int(y)

power = int_x**int_y
log = numpy.log2(int_x)
print("X**y =", power)
print("log(x) = ", log)
