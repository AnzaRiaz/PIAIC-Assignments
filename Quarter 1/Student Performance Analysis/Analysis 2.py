"""
Question
Is there any difference in student score if parents have Bachler level education in a specified score (we will take user input for choosing the score column)

"""
from Data import *

ScoreColumn = int(input("Enter A Score Column (Maths : 3 , Reading: 4 , Writing: 5 ): "))
Student_Score = 0

yes = 0
no = 0

if ScoreColumn >= 3 and ScoreColumn < 6:
    for stuff in data:

        Student_Score = Student_Score + int(stuff[ScoreColumn])

        if "bachelor's" in stuff[1] and Student_Score > 70:
            yes = yes + 1

        elif "bachelor's" not in stuff[1] and Student_Score > 70:
            no = no + 1




if no > yes:
    print("No Parental Level Of Education Does Not Affect The Students Grades In This Subject")

elif yes > no:
    print("Yes Parental Level Of Education Does Affect The Students Grades In This Subject")

else:
    print('Its A Tie')


