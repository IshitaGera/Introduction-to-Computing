#Assignment 2
#Name = Ishita
#SID=21103094(CSE)



#question 1

#given- take input as 'Python is a case sensitive language'
#(a)
string = str("Python is a case sensitive language")
print("INPUT STRING = ",string)
print("(Answer of a)")
length=len(string)
print(length)
print

#(b)
print("(Answer of b)")
reverse_string=string[length::-1]
print(reverse_string)

#(c)
print("(Answer of c)")
new_string=string[10:26]
print(new_string)

#(d)
print("(Answer of d)")
#replace 'a case sensitive' with 'oject oriented'
replaced_string=string[0:10]+'object oriented'+string[26:35]
print(replaced_string)

#(e)
print("(Answer of e)")
index_a=string.find('a')
print(index_a)

#(f) first check the index of white spaces and then write the new string by not using those index
print("(Answer of f)")
remove_whitespaces=string.replace(" ","")
print(remove_whitespaces)




#question 2
name='Ishita Gera'
SID=21103094
department_name="CSE"
CGPA='9.9'

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))




# question 3
a = 56
b = 10
#A
print("Answer of A")
print(a & b)
#B
print("Answer of B")
print(a | b)
#C
print("Answer of C")
print(a ^ b)
# D
print("Answer of D")
print(a << 2)
print(b << 2)
# E
print("Answer of E")
print(a >> 2)
print(b >> 4)


#question 4
#this program finds greatest of the three numbers 
num_1=int(input("Give a number:"))
num_2=int(input("Give a number:"))
num_3=int(input("Give a number:"))

if(num_1>num_2):
    if(num_1>num_3):
        print("The greatest number is ",num_1)
    else:
        print("The greatest number is ",num_3)
else:
    if(num_2>num_3):
        print("The greatest number is ",num_2)
    else:
        print("The greatest number is ",num_3)


# question 5
#check whether word name is in the string given by user or not 
string = str(input("Enter the string: "))
if("name" in string):
    print("Yes\n")
else:
    print("No\n")




#question 6
#to check whether the given input lengths can form a triangle or not
side_1_of_triangle=int(input("Give a number:"))
side_2_of_triangle=int(input("Give a number:"))
side_3_of_triangle=int(input("Give a number:"))

if(side_1_of_triangle+side_2_of_triangle>side_3_of_triangle and side_2_of_triangle+side_3_of_triangle>side_1_of_triangle and side_1_of_triangle+side_3_of_triangle>side_2_of_triangle):
    print("The triangle is possible")
else:
    print("The triangle is not possible")