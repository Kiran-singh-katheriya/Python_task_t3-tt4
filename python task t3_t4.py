"""1. Create a list of 10 elements of four different data types like int, string, complex and float.
solution:
l1=[1,2.05,3,4+1j,"bird",4,"mango",1+0j,7.09,10]


2. Create a list of size 5 and execute the slicing structure .
l1=[2,5,2,1,8]
print(l1[:])


3. Write a program to get the sum and multiply of all the items in a given list
#solution:
l1=[2,3,1,6,7]
sum_num=0
multiple=1

for i in l1:
    sum_num +=i
    multiple *=i
print(sum_num)
print(multiple)
"""

"""   
4. Find the largest and smallest number from a given list
l1=[9,2,44,5,333,8,1,32]
l1.sort()

smallest=l1[0]
largest=l1[-1]
print(smallest)
print(largest)


5.Create a new list which contains the specified numbers after removing the even numbers from a
predefined list. 

#solution
new_list=[]
l1=[2,45,3,24,89,22,7]
for i in l1:
    if i%2 !=0:
        new_list.append(i)
print(new_list)
"""

"""
6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).

n1=1
n2=30

l1=list()
for i in range(n1,n2+1):
    l1.append(i**1)
    first_five=l1[:5]
    last_five=l1[-5:]
print(first_five)
print(last_five)
"""

"""
Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]

l1=[1,3,5,7,9,10]
lst=[2,4,6,8]

l1[-1]=lst
print(list(l1))
"""

'''
8.Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}

solution:
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

"""


"""

9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
sol:

n1=1
n2=5
d={}
for i in range(n1,n2+1):
    d[i]=i*i
print(d)
'''

'''
10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’

sol:
num=input("Enter the num:")
split_num=num.split(",")

new_list=list(split_num)
new_tuple=tuple(split_num)
print(new_list)
print(new_tuple)
'''


#TASK FOUR
'''
1.Write a program to reverse a string.
Sample input: “1234abcd”
Expected output: “dcba4321

s="apple14"
print(s[::-1])
'''

"""2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12


solution:
def str_as_func(name):
    upper=0
    lower=0
    for i in name:
        if i==i.upper():
            upper=upper+1
        elif i==i.lower():
            lower=lower+1
        else:
            print("no match found")

    print("No of upper character are:",upper)
    print("No of upper character are:",lower)

str_as_func('abcSdefPghijQkl')
"""

'''3. Create a function that takes a list and returns a new list with unique elements of the first list. 

solution:
def func(list_elem):
    l1=set(list_elem)
    unique=list(l1)

    for i in unique:
        print(i)

l1=[23,11,22,33,1,2,3,11,2,1,23,54,77]
func(l1)'''


'''
4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabeticall

solution:
s=input("Enter the name contain hyphen-separated:")
items=s.split('-')
for i in items:
    items.sort()

print('-'.join(items))
'''

'''
5 Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

solution:
str_input=input("Enter any sentense that you wants to capitalized")
s=str_input.upper()
print(s)
'''

'''6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console

solution
def sum_of_string(a,b):
    return int(a)+int(b)

x="10"
y="20"

print(sum_of_string(x,y))
'''


'''
7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line

solution
def max_len(str1,str2):

    len1=len(str1)
    len2=len(str2)
    if len1>len2:
        print(str1)
    elif len2>len1:
        print(str2)
    elif len1==len2:
        print("both are same length")


str1=input("Enter the first string character:")
str2=input("Enter the second string character:")
max_len(str1,str2)
''' 

''' 
8.Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).

solution:
def squa_num(n1,n2):
    for i in range(n1,n2+1):
        square_num=i*i
        print(square_num,end=" ")

squa_num(1,20)
'''


'''. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN
1 ODD
2 EVEN
3 ODD

solution:
def showNumbers(limit):
    for i  in range(0,limit):
        if i%2==0:
            print(i,"is EVEN")
        else:
            print(i,"is ODD")

showNumbers(4)
'''  

'''10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)

Solution:
num=[i for i in range(1,21)]
even_number=filter(lambda x:(x%2==0),num)
l1=list(even_number)
print(l1)
'''

'''11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions

#solution:
l1=[1,2,3,4,5,6,7,8,9,10]
even_number=map(lambda x:x**2,filter(lambda x:x%2==0,l1))
print(list(even_number))
'''

'''12. Write a function to compute 5/0 and use try/except to catch the exceptions

solution:
from ast import Try
def divide():
    return 5/0

try:
    divide()

except ZeroDivisionError as z:
    print("Zero divided by any number is infinity")
except:
    print("Is was not useful")
'''


'''13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().



from operator import concat
from functools import reduce
if __name__ == '__main__':
        l1= [1,2,3,4,5,6,7]
        new=reduce(operator.concat,l1)
        print(new)
'''


'''14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions

l1=[i for i in range(1,99) if i%3!=0 and i%7==0]
print(l1)

'''

'''15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.

def square(x):
    return x*x

l1=[i for i in range(1,10)]
sqr_rt=map(square,l1)

for num in sqr_rt:
    print(num,end=" ")
'''

'''16. What is the output of the following codes:

def foo():
    
    try:
        return 1
    finally:
       return 2

output:2

k=foo()
print(k)
'''
def a():
    try:
        f(x,4)
    finally:
        print('after f')
        print('after f?')
a()
output:
NameError