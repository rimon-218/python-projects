class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def show_info(self):
        print("Name :",self.name)
        print("Roll:",self.roll)

student1=student("Ruman","101")

student1.show_info()



"""

dry run:

student=("Rahim,101")

__init__()runs:

self.name=name
self.roll=roll

student1 now contains:
name=Rahim
roll=101

show_info:

'n Name:Rahim
'n Roll:101



trace table:


step    ।   Object      ।    Name   ।   Roll  
--------------------------------------------------------------
1       ।   student1    ।    Rahim  ।     101
2       ।   student1    ।    Rahim  ।     101 'n show_info



"""