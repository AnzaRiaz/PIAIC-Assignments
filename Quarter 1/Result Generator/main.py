"""
Written By Shaharyar Ahmed
"""

from os import system # A few modules I need 
from time import sleep

#Taking input from the user
name = input("Please Enter Your Name: ").title()
school_name = input("Please Enter Your School Name: ").title()
report_card = "Report Card"

while True:
    #Exception handling 
    try:
        math_marks = int(input("Please Enter Your Maths Marks: "))
        engl_marks = int(input("Please Enter Your English Marks: "))
        addm_marks = int(input("Please Enter Your Add Maths Marks: "))
        comp_marks = int(input("Please Enter Your Computer Science Marks: "))
        paki_marks = int(input("Please Enter Your PST Marks: "))


    except Exception as e:
        print("Please Enter A Valid Number")

    proceed = True

    if math_marks > 100 or engl_marks > 100 or addm_marks > 100 or comp_marks > 100 or paki_marks > 100:
        system("cls")
        print("Invalid Values Your Marks Cannot Be Above 100!")
        
    else:
        break

#Calculating the result
system("cls")
print("Generating Your Report Card Please Wait......")
sleep(2)
system("cls")
name = name.center(120) #Place the name and the school name in the center of the screen
school_name = school_name.center(120)
report_card = report_card.center(120)


def grade_checker(marks):
    if marks >= 80:
        return "A"
        
    elif marks < 80 and marks >= 70:
        return "B"

    elif marks >= 60 and marks <= 69:
        return "C"
        
    elif marks >= 50 and marks <= 59:
        return "D"

    else:
        return 'F'

total = math_marks + engl_marks + addm_marks + comp_marks + paki_marks
average_marks = total/5
average = total/500 * 100

#Displaying The Result
print(report_card)
print(name)
print(school_name)
print("")
print(f"      Mathematics Marks:      {math_marks}                        {grade_checker(math_marks)}")
print(f"      English Marks:          {engl_marks}                        {grade_checker(engl_marks)}")
print(f"      Add Math Marks:         {addm_marks}                        {grade_checker(addm_marks)}")
print(f"      Computer Science Marks: {comp_marks}                        {grade_checker(comp_marks)}")
print(f"      Pakistan Studies Marks: {paki_marks}                        {grade_checker(paki_marks)}")
print("")
print(f"      Average Grade: {grade_checker(average_marks)}               Percentage = {average}")

if average >= 60:
    print("")
    print("      Promoted To Next Class Congratulations!")

else:
     print("")
     print("      Not Promoted To Next Class!")


