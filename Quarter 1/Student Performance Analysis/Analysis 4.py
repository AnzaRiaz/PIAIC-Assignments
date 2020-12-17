"""
Question
in a user given score, is the top scorer a female or male?
"""
from Data import *

ScoreColumn = int(input("Enter A Score Column (Maths : 3 , Reading: 4 , Writing: 5 ): "))
Scores_list = []
Male_Female = []

if ScoreColumn >= 3 and ScoreColumn < 6:
    for stuff in data:
            Scores_list.append(stuff[ScoreColumn])
            Male_Female.append(stuff[0])

max_num = max(Scores_list)
print(max_num)
index = Scores_list.index(max_num)

print(f"The Top Scorer In This Subject Is A {Male_Female[index]}")




    

  


