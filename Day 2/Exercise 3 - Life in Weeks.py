age = input("What is your current age? ")
age_left=90-int(age)

print(f"You have {365*int(age_left)} days, {52*int(age_left)} weeks, and {12*int(age_left)} months left.")

from time import sleep
sleep(10)
