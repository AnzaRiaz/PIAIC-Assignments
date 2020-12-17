"""
Question
How many parents have bachelors education, master education, or some college degrees level education?
"""
from Data import *

bachelor = 0
master = 0
some_college = 0
associates_degree = 0
high_school = 0
some_highschool = 0

for stuff in data:

    if "bachelor's" in stuff[1]:
            bachelor = bachelor + 1

    elif "master's" in stuff[1]:
            master = master + 1

    elif "some college" in stuff[1]:
            some_college = some_college + 1

    elif "associate's" in stuff[1]:
            associates_degree = associates_degree + 1

    elif "high school" == stuff[1]:
            high_school = high_school + 1
    
    elif "some high school" == stuff[1]:
            some_highschool = some_highschool + 1

print(f"bachelors's Degree: {bachelor} , Master's Degree: {master} , Some College: {some_college} , associate's Degree: {associates_degree} , High School: {high_school}, Some High School: {some_highschool}")

    

  


