student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score=0

for i in student_scores:
    if highest_score<i:
        highest_score=i

print(f"The highest score in the class is: {highest_score}")

from time import sleep
sleep(10)#to wait 10 seconds before closing
