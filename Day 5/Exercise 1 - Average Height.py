student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

lenght=0
sum_height=0

for height in student_heights:
    sum_height=sum_height+height
    lenght+=1

print("Average height: ",round(sum_height/lenght))   

from time import sleep
sleep(10)#to wait 10 seconds before closing
