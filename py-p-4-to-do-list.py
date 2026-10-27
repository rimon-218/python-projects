
tasks=["Study python","Practice dry run"]

tasks.append("Learn git")

complited=["Study python"]

remaining=[task for task in tasks if task not in complited ]


print("All tasks:",tasks)
print("Remaining:",remaining)


"""

dry run:

tasks:
["Study python","Practice dry run"]

append("Learn git")

tasks:
["Study python","Practice dry run","Learn git"]


complited:
["Study python"]

list comprehension checks:

Study python 'n complited 'n bad 'n Practice dry run 'n remaining 'n Learn git 'n remaining

remaining:
["Practice dry run","Learn git"]



trace table:

step    ।       task          ।    complited?   ।            remaining    
--------------------------------------------------------------------------------------
1       ।   Study python      ।     yes         ।           -        
2       ।   Practice dry run  ।     no          ।    Practice dry run         
3       ।   Learn git         ।     no          ।    Practice dry run,  Learn git     


"""