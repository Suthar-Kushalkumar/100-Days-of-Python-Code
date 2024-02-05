print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1l=name1.lower()
name2l=name2.lower()
true=name1l.count('t')+name1l.count('r')+name1l.count('u')+name1l.count('e')+name2l.count('t')+name2l.count('r')+name2l.count('u')+name2l.count('e')

love=name1l.count('l')+name1l.count('o')+name1l.count('v')+name1l.count('e')+name2l.count('l')+name2l.count('o')+name2l.count('v')+name2l.count('e')

love_score=int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>40 and love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

from time import sleep
sleep(10)#to wait 10 seconds before closing
