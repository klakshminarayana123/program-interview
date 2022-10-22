#!/usr/bin/env python
# coding: utf-8

# 
# 1) What is the difference between list and tuples in Python?

# In[ ]:


LIST vs TUPLES
Lists are mutable i.e they can be edited.	Tuples are immutable (tuples are lists which can’t be edited).
Lists are slower than tuples.	Tuples are faster than list.
Syntax: list_1 = [10, ‘Chelsea’, 20]	Syntax: tup_1 = (10, ‘Chelsea’ , 20)



# In[ ]:


get_ipython().set_next_input('2) What are Dict and List comprehensions');get_ipython().run_line_magic('pinfo', 'comprehensions')

Dictionary and list comprehensions are just another concise way to define dictionaries and lists.

Example of list comprehension is-

1
x=[i for i in range(5)]
The above code creates a list as below-

1
2
4
[0,1,2,3,4]
Example of dictionary comprehension is-

1
x=[i : i+2 for i in range(5)]
The above code creates a list as below-

1
[0: 2, 1: 3, 2: 4, 3: 5, 4: 6]
# In[ ]:


get_ipython().set_next_input('3)What is the difference between .py and .pyc files');get_ipython().run_line_magic('pinfo', 'files')


# In[ ]:


Ans: The .py files are the python source code files. While the .pyc files contain the bytecode of the python files. .pyc files are created when the code is imported from some other source. The interpreter converts the source .py files to .pyc files which helps by saving time.


# In[ ]:


get_ipython().set_next_input('4) What are local variables and global variables in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Local Variables:2) Global Variables:Example:

1
2
3
4
5
6
a=2
def add():
b=3
c=a+b
print(c)
add()


# In[ ]:


get_ipython().set_next_input('5) Is python case sensitive');get_ipython().run_line_magic('pinfo', 'sensitive')


# In[ ]:


Yes. Python is a case sensitive language


# In[ ]:


get_ipython().set_next_input('6)What is type conversion in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


int() – converts any data type into integer type

float() – converts any data type into float type

ord() –converts characters into integer


# In[ ]:


get_ipython().set_next_input('7) What is the difference between Python Arrays and lists');get_ipython().run_line_magic('pinfo', 'lists')


# In[ ]:


Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

Example:1
2
3
4
5
import array as arr
My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array)
print(My_list)




# In[ ]:


get_ipython().set_next_input('8) what are the functions in pyton');get_ipython().run_line_magic('pinfo', 'pyton')
A)A function is a block of code which is executed only when it is called. To define a Python function, the def keyword is used.

Example:

1
2
3
def Newfunc():
print("Hi, Welcome to Edureka")
Newfunc(); #calling the function



# In[ ]:


get_ipython().set_next_input('9) What is __init__');get_ipython().run_line_magic('pinfo', '__init__')


# In[ ]:


init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ meth
Here is an example of how to use it.
class Employee:
def __init__(self, name, age,salary):
self.name = name
self.age = age
self.salary = 20000
E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1. 
print(E1.name)
print(E1.age)
print(E1.salary)






# In[ ]:


get_ipython().set_next_input('10) What is self in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:



Self is an instance or an object of a class. In Python, this is explicitly included as the first parameter. However, this is not the case in Java where it’s optional.  It helps to differentiate between the methods and attributes of a class with local variables.

The self variable in the init method refers to the newly created object while in other methods, it


# In[ ]:


get_ipython().set_next_input('11)What is a lambda function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.

Example:

1
2
a = lambda x,y : x+y
print(a(5, 6))
Output: 11


# In[ ]:


get_ipython().set_next_input('12) What does [::-1} do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


[::-1] is used to reverse the order of an array or a sequence.
For example:
1
2
3
import array as arr
My_Array=arr.array('i',[1,2,3,4,5])
My_Array[::-1]
Output: array(‘i’, [5, 4, 3, 2, 1])


# In[ ]:


get_ipython().set_next_input('13)How can you randomize the items of a list in place in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Consider the example shown below:

1
2
3
4
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x


# In[ ]:


get_ipython().set_next_input('14)What are python iterators');get_ipython().run_line_magic('pinfo', 'iterators')


# In[ ]:


Iterators are objects which can be traversed though or iterated upon.


# In[ ]:


get_ipython().set_next_input('15) How can you generate random numbers in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Random module is the standard module that is used to generate a random number. The method is defined as:

1
2
import random
random.random


# In[ ]:


get_ipython().set_next_input('16)How do you write comments in python');get_ipython().run_line_magic('pinfo', 'python')


# In[ ]:


Comments in Python start with a # character. However, alternatively at times, commenting is done using docstrings(strings enclosed within triple quotes).

Example:

1
2
3
<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_end"></span>
&lt;pre&gt;&lt;span&gt;#Comments in Python start like this
print("Comments in Python start with a #")


# In[ ]:


get_ipython().set_next_input('17)  What is pickling and unpickling');get_ipython().run_line_magic('pinfo', 'unpickling')


# In[ ]:


Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.


# In[ ]:


get_ipython().set_next_input('18) How will you convert a string to all lowercase');get_ipython().run_line_magic('pinfo', 'lowercase')


# In[ ]:


To convert a string to lowercase, lower() function can be used.

Example:

1
2
stg='ABCD'
print(stg.lower())
Output: abcd


# In[ ]:


get_ipython().set_next_input('19)What are docstrings in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.

Example:

1
2
3
4
5
6
7
8
"""
Using docstring as a comment.
This code divides 2 numbers
"""
x=8
y=4
z=x/y
print(z)
Output: 2.0


# In[ ]:


get_ipython().set_next_input('20) What is the purpose of ‘is’, ‘not’ and ‘in’ operators');get_ipython().run_line_magic('pinfo', 'operators')


# In[ ]:


Operators are special functions. They take one or more values and produce a corresponding result.

is: returns true when 2 operands are true  (Example: “a” is ‘a’)

not: returns the inverse of the boolean value

in: checks if some element is present in some sequence


# In[ ]:


get_ipython().set_next_input('21) What is the usage of help() and dir() function in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions. 

Help() function: The help() function is used to display the documentation string and also facilitates you to see the help related to modules, keywords, attributes, etc.
Dir() function: The dir() function is used to display the defined symbols.
    


# In[ ]:


get_ipython().set_next_input('22) How can the ternary operators be used in python');get_ipython().run_line_magic('pinfo', 'python')


# In[ ]:


rator is the operator that is used to show the conditional statements. This consists of the true or false values with a statement that has to be evaluated for it.

Syntax:[on_true] if [expression] else [on_false]x, y = 25, 50big = x if x < y else y


# In[ ]:


get_ipython().set_next_input('23)What does len() do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


It is used to determine the length of a string, a list, an array, etc.

Example:

1
2
stg='ABCD'
len(stg)


# In[ ]:


get_ipython().set_next_input('24)What are Python packages');get_ipython().run_line_magic('pinfo', 'packages')


# In[ ]:


Python packages are namespaces containing multiple modules.


# In[ ]:


get_ipython().set_next_input('25)How can files be deleted in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


To delete a file in Python, you need to import the OS Module. After that, you need to use the os.remove() function.

Example:

1
2
import os
os.remove("xyz.txt")


# In[ ]:


get_ipython().set_next_input('26)What are the built-in types of python');get_ipython().run_line_magic('pinfo', 'python')


# In[ ]:


Built-in types in Python are as follows –

Integers
Floating-point
Complex numbers
Strings
Boolean


# In[ ]:


get_ipython().set_next_input('27)How to add values to a python array');get_ipython().run_line_magic('pinfo', 'array')


# In[ ]:


Elements can be added to an array using the append(), extend() and the insert (i,x) functions.

Example:

1
2
3
4
5
6
7
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)
a.extend([4.5,6.3,6.8])
print(a)
a.insert(2,3.8)
print(a)


# In[ ]:


get_ipython().set_next_input('28) How to remove values to a python array');get_ipython().run_line_magic('pinfo', 'array')


# In[ ]:


Ans: Array elements can be removed using pop() or remove() method. The difference between these two functions is that the former returns the deleted value whereas the latter does not.

Example:

1
2
3
4
5
a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print(a.pop())
print(a.pop(3))
a.remove(1.1)
print(a)
Output:

4.6

3.1

array(‘d’, [2.2, 3.8, 3.7, 1.2])


# In[ ]:


29) What are Python libraries? Name a few of them.


# In[ ]:


Python libraries are a collection of Python packages. Some of the majorly used python libraries are – Numpy, Pandas, Matplotlib, Scikit-learn and many more.


# In[ ]:


get_ipython().set_next_input('30) What is split used for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


The split() method is used to separate a given String in Python.

Example:

1
2
a="lucky pyton"
print(a.split()


# In[ ]:


get_ipython().set_next_input('31) How to import modules in python');get_ipython().run_line_magic('pinfo', 'python')


# In[ ]:


Modules can be imported using the import keyword.  You can import modules in three ways-

Example:

1
2
3
import array           #importing using the original module name
import array as arr    # importing using an alias name
from array import *    #imports everything present in the array module


# In[ ]:


32)How are classes created in Python? 


# In[ ]:


Class in Python is created using the class keyword.

Example:

1
2
3
4
5
class Employee:
def __init__(self, name):
self.name = name
E1=Employee("abc")
print(E1.name)


# In[ ]:


get_ipython().set_next_input('33)What is monkey patching in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.

Consider the below example:

1
2
3
4
# m.py
class MyClass:
def f(self):
print "f()"


# In[ ]:


34) How to create an empty class in Python? 


# In[ ]:


For example- empty class
1
2
3
4
5
class a:
  pass
obj=a()
obj.name="xyz"
print("Name = ",obj.name)


# In[ ]:


35)Write a program in Python to produce Star triangle.


# In[ ]:


1
2
3
4
def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)   *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************


# In[ ]:


36) Write a program to produce Fibonacci series in Python.


# In[ ]:


1
2
3  
Output: Enter the terms 5 0 1 1 2 3
4
5
6
7
8
9
10
11
12
# Enter number of terms needednbsp;#0,1,1,2,3,5....
a=int(input("Enter the terms"))
f=0;#first element of series
s=1#second element of series
if a=0:
   print("The requested series is",f)
else:
  print(f,s,end=" ")
   for x in range(2,a): 
         print(next,end=" ")
         f=s
         s=next


# In[ ]:


37) Write a program in Python to check if a number is prime.


# In[ ]:


a=int(input("enter number"))
if a=1:
   for x in range(2,a):
         if(a%x)==0:
          print("not prime")
   break
   else:
      print("Prime")
else:
   print("not prime")
Output:

enter number 3

Prime


# In[ ]:


38)Write a program in Python to check if a sequence is a Palindrome.


# In[ ]:


1
2
3
4
5
6
a=input("enter sequence")
b=a[::-1]
if a==b:
  print("palindrome")
else:
  print("Not a Palindrome")
Output:

enter sequence 323 palindrome


# In[ ]:


get_ipython().set_next_input('39) Write a sorting algorithm for a numerical dataset in Python');get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


The following code can be used to sort a list in Python:

1
2
3
4
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list) 


# In[ ]:


get_ipython().set_next_input('40)  How To Save An Image Locally Using Python Whose URL Address I Already Know');get_ipython().run_line_magic('pinfo', 'Know')


# In[ ]:


We will use the following code to save an image locally from an URL address

1
2
import urllib.request
urllib.request.urlretrieve("URL", "local-filename.jpg")

