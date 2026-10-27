name="Rahim"
marks={
    "Math":85,
    "English":75,
    "Science":90
}

subjects=("Math","English","Science")

passed=set()

for subject in subjects:
    if marks[subject]>=40:
        passed.add(subject)

total=sum(marks.values())
average=total / len(marks)

print("Name:",name)
print("Total:",total)
print("Average:",average)
print("Passed:",passed)


"""

dry run:

name=Rahim
marks={
    Math=85
    English=75
    Science=90
}

Math:
85>=40'true
passed={Math}

English:
75>=40'true
passed={Math,English}

Science:
90>=40'true
passed={Math,English,Science}

total=85+75+90
total=250

average=250 / 3
average=83.33



trace table:

step    ।   subject   ।   marks   ।   condition  ।     passed
-----------------------------------------------------------------
1       ।   Math      ।      85   ।     true     ।     Math
2       ।   English   ।      75   ।     true     ।     English
3       ।   Science   ।      90   ।     true     ।     Science


"""

