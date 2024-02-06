import random

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(",")# it will split string into array from ","


print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")

#print(f"{random.choice(names)} is going to buy the meal today!")

from time import sleep
sleep(10)#to wait 10 seconds before closing
