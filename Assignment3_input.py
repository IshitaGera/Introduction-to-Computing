#QUESTION1
print('QUESTION1')
input_value=input('enter the string:').lower().split()
if len(input_value)==1:
    input_value=input_value[0]
occurences={}
for i in input_value:
    if i in occurences:
        occurences[i]+=1
    else:
        occurences[i]=1
print('The occurence(s) of:')
for i in occurences:
    print('\t"%s" is/are %d'%(i,occurences[i]))




#QUESTION2
print("QUESTION2")
def is_leap_year(year: int) -> bool:                                                                                #this function is used to check whether the tear is leap or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  #Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 #Condition for number of days in the month February
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      #Setting no. of days in the given month
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                #Syntax for increasing the date
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))




#QUESTION3
print('QUESTION3')
input_list=eval(input('enter the list:'))
output_list=[]
for i in input_list:
    output_list.append((i,i**2))
print('output:',output_list)




#QUESTION4
print("QUESTION 4")
#taking the grade points from the user
grade=int(input('write the grade points scored'))
if grade==10:
    print("Your Grade is'A+' and Outstanding Performance")
elif grade==9:
    print("Your Grade is 'A' and Excellent Performance ")
elif grade==8:
    print("Your Grade is 'B+' and Very Good Performance")
elif grade==7:
    print("Your Grade is 'B' and Good Performance")
elif grade==6:
    print("Your Grade is 'C+' and Average Performance")
elif grade==5:
    print("Your Grade is 'C' and Below Average Performance")
elif grade==4:
    print("Your Grade is 'D' and Poor Performance")
else:
    print("Invalid Grade point")
print("\n")




#QUESTION5
print('QUESTION5')
name='ABCDEFGHIJK'
j=0
while len(name)-j*2>=1:
    print(' '*j+name[0:len(name)-j*2])
    j=j+1




#QUESTION6
print('QUESTION6')
sid=int(input('Enter the SID of the student:'))
name=input('Enter the name of the student:')
students={sid:name}
while True:
    given=input('Do you want to add another student(Y or N):').upper()
    if given=='Y':
        sid=int(input('Enter the SID of the student:'))
        name=input('Enter the name of the student:')
        students[sid]=name
    elif given=='N':
        break
    else:
        print('Something is wrong!')
#part(a) (to print the dictionary)
print("(a)",students)
#part(b)(to sort according to names)
print("(b)",{k:v for k,v in sorted(students.items(),key=lambda x:x[1])})
#part(c)(to sort according to SIDs)
print("(c)",{k:v for k,v in sorted(students.items())})
#part(d)(to search for a student by their SID)
sid=int(input('Find the name by writing the SID:'))
print("(d)",students[sid])




#QUESTION7
print('QUESTION7')
'''a is first number,b is second number and c is the extra variable used for adding and reassign the values'''
a=0
b=1
sum=0
while True:
    num=int(input('Enter the number of terms of the fibonacci sequence you want:'))
    if num<0:
        print('Number of terms must be non negative\nPlease enter again\n')
        continue
    if num==0:
        print('The fibonacci sequence contains 0 terms so the average=0')
        break
    else:
        print('The fibonacci sequence is:')
        print(a,end=' ')
        for i in range(1,num):
            sum=sum+b
            print(b,end=' ')
            c=a+b
            a=b
            b=c
        print('\nThe average of the fibonacci sequence upto %d terms is%0.2f'%(num,sum/num))
        break




#QUESTION8
print('QUESTION8')
#given sets
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#part(a)(subtracting the intersection of set1 and set2 from the union of the two)
part_a_set=Set1.union(Set2)-Set1.intersection(Set2)
print("(a)",part_a_set)
#part(b)(subtracting the intersection of all three sets from the union of all three)
part_b_set=Set1.union(Set2.union(Set3))-Set1.intersection(Set2)-Set2.intersection(Set3)-Set3.intersection(Set1)
print("(b)",part_b_set)
#part(c)(subtracting the intersection of all three sets from the union of sets taken two at a time)
part_c_set=((Set1.intersection(Set2)).union((Set3.intersection(Set1)).union(Set2.intersection(Set3))))-Set1.intersection(Set2.intersection(Set3))
print("(c)",part_c_set)
#part(d)(creating a set which does not contain the elements of set1)
part_d_set=set()
for i in range(1,11):
    if i not in Set1:
        part_d_set.add(i)
print("(d)",part_d_set)
#part(e)(creating a set which does not contain the elements of all three sets)
part_e_set=set()
for i in range(1,11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        part_e_set.add(i)
print("(e)",part_e_set)





