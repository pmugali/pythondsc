print("Hi There!")
print(type(12))
print(type(12.121))
print(type("A"))
#var = input("Enter any value: ")
#print("Entered value: ", var, ", is of type:", type(var))
'''
This is a commented section
'''
"""
This is also a commented section
"""
# This is a single line comment
print("Hello "+ "12")
print(5%6)
print((1 == 1) and (not(1==1 or 1 ==0)))

print(5%3, 5//3, 5/3, 6%3, 6//3, 6/3)

var = (int)(input("Enter any value: "))

if (not var%3):
    print(var, "Divided by 3")
if (not var%5):
    print(var, "divisable of 5")
if(not(var%3 or var%5)):
    print(var, "Divisable by both 3 & 5")
if(var%3 and var%5):
    print(var, "Invalid")   

for num in range (0,8,2):
    print("From range is", num)
print("---------------------------")
for num in range (5,0,-1):
    print("From range is", num)    
print("---------------------------")
for num in range (1,5):
    print("From range is", num)  
print("---------------------------")

num = input("Enter Integer Number: ")
val=0
for i in num:
    val += (int)(i)

print("Sum of integers in ", num, "is - ", val)    

int_num = (int)(num)

print(-10<-200)

for num in 23, 45, 50, 65, 76, 90:
    if(num%5!=0):
        continue
    if(num%10==0):
        print(num, end=" ")
        continue
    if(num%3==0):
        print(num, end=" ")
print("---------------------------")
number=28
for num in range(25,30):
    if(number>num):
        print(num)
    else:
        print(num)
        break

def find_square(x):
    return x * x
print("Square of", 4, "is", find_square(4))


def change_val(arg):
    arg.append(arg)

my_list = [10]
print("Mylist", my_list)
change_val(my_list)
print("Mylist", my_list)

msg='infosys'
print(msg[:3])

result=0

def find_sum(num1,num2):
    if(num1!=num2):
        result=num1+num2
    else:
        result=2*(num1+num2)

find_sum(3,4)
print(result)
find_sum(5,5)
print(result)