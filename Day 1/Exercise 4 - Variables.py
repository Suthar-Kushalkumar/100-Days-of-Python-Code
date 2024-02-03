a = input("a: ")
b = input("b: ")

####################################

c=b
b=a
a=c

####################################

print("a: " + a)
print("b: " + b)

from time import sleep#to wait before close
sleep(10)#to wait 10 seconds before closing
