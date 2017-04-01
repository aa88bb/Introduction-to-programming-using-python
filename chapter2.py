radius = 20
area = radius * radius * 3.14159
print("the area for the circle of radius",radius,"is",area)

# radius = eval(input("enter a value for radius:"))
# area = radius * radius * 3.14159
# print("the area for the circle of radius",radius,"is",area)

count = int()
count += 9
print(count)

# n1,n2 = eval(input("enter 2 numbers seperated by commas:"))
# average = (n1+n2)/2
# print("average is:",average)

print(2.3 ** 3.5)

import time
currentTime = time.time()
print(currentTime)
totalSeconds = int(currentTime)
print(totalSeconds)
currentSecond = totalSeconds % 60
print(currentSecond)
currentMinute = totalSeconds // 60 % 60
print(currentMinute)


x1,y1 = eval(input("enter point 1:"))
x2,y2 = eval(input("enter point 2:"))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
print(distance)