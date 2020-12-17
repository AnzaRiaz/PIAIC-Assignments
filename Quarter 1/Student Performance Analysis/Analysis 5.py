"""
Question
how many students have good in reading (> 75) but not good in writing( < 70)
"""
from Data import *

num = 0

for stuff in data:
    reading_score = int(stuff[4])
    writing_score = int(stuff[5])

    if reading_score > 75 and writing_score < 70:
        num = num + 1

print(f"{num} Students Are Good At Reading But Weak In Writing are")

            
#The Output Was 0 



    

  


