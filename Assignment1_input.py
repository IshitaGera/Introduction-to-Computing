#assignment1
#ques 1
#to find the average of three numbers
a=int(input('enter first num:'))
b=int(input('enter second num:'))
c=int(input('enter third num:'))
avg=(a+b+c)/3
print('average is:',avg)



#ques 2
#to compute a person's income tax(in $)
GI=float(input('gross income is:'))
num_dependents=int(input('number of dependents are:'))
sd=10000
dd=3000
taxable_income=GI-sd-(num_dependents*dd)
print('taxable income is:',taxable_income)
tax_rate_percent=20
tax=(taxable_income*tax_rate_percent)/100
print('tax to be paid:',tax)



#ques 3
#to make a list of student's information
SID=int(input('SID of the student:'))
name=input('name of the student:')
gender=input('gender of the student(F/M/U)(U for unknown):')
course=input('course enrolled by the student:')
cgpa=float(input('cgpa obtained by the student:'))
student_list=[SID,name,gender,course,cgpa]
print(student_list)



#ques 4
#list of marks of 5 students
a=float(input('marks obtained by student 1:'))
b=float(input('marks obtained by student 2:'))
c=float(input('marks obtained by student 3:'))
d=float(input('marks obtained by student 4:'))
e=float(input('marks obtained by student 5:'))
marks_list=[a,b,c,d,e]
marks_list.sort()
print(marks_list)



#ques 5
#to make a list of colors 
#5(a) to remove black color
colors=['red','green','white','black','pink','yellow']
print(colors)
del colors[3]
print(colors)
#5(b) to remove black and pink and to add purple color
colors=['red','green','white','black','pink','yellow']
colors[3:5]=['purple']
print(colors)