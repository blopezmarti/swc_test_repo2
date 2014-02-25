# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ---
# 
# #Intro to Python
# 
# ---

# <markdowncell>

# ###Why Python?  
# 1.  Readibility  
# 2.  Built with coder psychology in mind
# 3.  Language interoperability  
# 4.  Object Oriented  
# 5.  It does EVERYTHING  

# <markdowncell>

# ![alt text](http://imgs.xkcd.com/comics/python.png "Title")

# <markdowncell>

# ## And simply diving in:  
# Let's quick look at an example of python showing  
# 
#  *  using libraries  
#  *  using comments  
#  *  variable assignment  
#  *  using functions  
#  *  printing results  
#   
# Then we'll go through things more slowly

# <markdowncell>

#   
# ---
#   
# # Variables  
#   
# ---  
#   
# *  No need to declare variable types  
# *  ANYTHING can be put in a variable  
#     +  numbers  
#     +  strings  
#     +  functions  
#     +  file-handles
#     +  etc, etc  
# 
# Variables are just containers to put stuff in, they don't much care what!

# <codecell>

1+2

# <codecell>

import math
print math.cos(5)

# <codecell>

y = 'abc'
print y

# <codecell>

z = math.cos
print z

# <codecell>

x = 4
print x

# <codecell>

print z(x)

# <codecell>

a = [5, 4, 3, 2]
print a

# <codecell>


# <markdowncell>

# ### Numbers: ints and floats

# <codecell>

4 + 5

# <codecell>

4 + 5.0

# <codecell>

6/4

# <codecell>

6.0/4

# <codecell>

6.0//4

# <markdowncell>

# ## *Excercise:*  
# 
# Do some basic arithmetic with floats and integers.  
# 
# *  addition:        +  
# *  subtraction:     -  
# *  multiplication:  *  
# *  division:        /  
# *  exponentiataion: **
# *  modulo:          %

# <codecell>

5.6 + 3

# <codecell>

5.6 - 3

# <codecell>

5.6 / 3

# <codecell>

5.6 // 3

# <codecell>

5.6 / 3.0

# <codecell>

5.6 // 3.0

# <codecell>

5%3

# <codecell>

5.0%3.0

# <codecell>

5.0/3

# <markdowncell>

# ### Strings

# <codecell>

d = 'abcdefg'
print d[0:3], d[3:5]
print d[-3:-1]
print d.find('b')
print d[d.find('b'):]

# <codecell>

f = 'abababcbdb'
print f.split('b')

# <markdowncell>

# ### Lists
# 
# This is NOT the python equivalent to an IDL array.  
# This is a list, which serves a different purpose.

# <codecell>

my_list = ['a' , 'b' , 'c']
type(my_list)
print my_list

# <codecell>

my_list = [1, 2, 3]
print my_list + my_list

# <markdowncell>

# ---
# 
# # Operations...but not only with numbers?
# 
# ---

# <markdowncell>

# ##Exercise:
# 
# 1. Try different operations on different data types: use addition to "add" integers, floats, strings, and lists. Does addition behave the same when acting on a string vs a float?
# 
# 2. Now try with multiplication, division, and subtraction. Do these operations work on all data types?

# <codecell>

3 + 5.5

# <codecell>

3 + 'Juan'

# <codecell>

'3' + 'Juan'

# <codecell>

'3Juan' - '3'

# <codecell>

pepe = ['p', 'e', 'p', 'e']
pepe + pepe

# <codecell>

pep = 'pep'
pepe + pep

# <codecell>

pep + pep

# <codecell>

my_list = [1, 2, 3, 4]
my_str = 'abcd'
my_int = 4
my_float = 5.0

# <codecell>

print my_list*3
print my_str*3
print my_int*3

# <codecell>

print my_list/3

# <codecell>

print my_string/3

# <codecell>

print my_int/3.

# <markdowncell>

# # If you finish early, take a break

# <markdowncell>

# ## *Excercise:*  
# 
# Make a string containing "luminiferous ether" 10 times.
# 
# Then make a list of that string 100 times.

# <codecell>

string1 = 'luminiferous ether '
print string1

# <codecell>

string2 = string1*10
print string2

# <codecell>

list1 = [string2]
print list1

# <codecell>

list2 = list1*10
print list2

# <codecell>

list3 = ['luminiferous ether']*100
print list3

# <markdowncell>

# # More datatypes

# <markdowncell>

# ###Tuple

# <codecell>

my_tuple = (1, 2, 3)
print type(my_tuple)
my_list = [1, 2, 3]
print type(my_list)

# <codecell>

my_tuple[1] = 5

# <codecell>

print my_tuple

# <codecell>

my_list[1] = 5
print my_list

# <markdowncell>

# ###Dictionary

# <codecell>

my_dict = {'apple':3, 'banana':2, 'carrot':5}
print my_dict.keys()
print my_dict['apple']

# <codecell>

#Also, an example of using dictionaries
fruit = 'apple'
#Option 1:
if fruit == 'banana':
    quantity = 2
elif fruit == 'carrot':
    quantity = 5
elif fruit == 'apple':
    quantity = 3
else:
    print 'I do not know how much fruit to by for the fruit you specified'
    
#Option 2:
    quantity = my_dict[fruit]

# <markdowncell>

# ### Numpy Array

# <codecell>

import numpy as np

# <codecell>

one_array = np.ones((5, 4))
print one_array*5
print type(one_array)

# <codecell>

print np.arange(3, 50, 10)

# <codecell>

#List
print range(10)

# <codecell>

my_array = np.array([1, 2, 3, 4])
print type(my_array)

# <codecell>

my_list = [1, 'a', 'apple', [1,2,3]]
np.array(my_list)

# <markdowncell>

# ----------------
# #Control Statements
# 
# -----------------

# <markdowncell>

# All control statements use : followed by indentation to denote that a given statement is acting on everything indented below. This improve readability by forcing you to write good code and remove the chance of forgetting to end your statement 

# <markdowncell>

# ###For loop

# <codecell>

my_list = [12, 24, 37, 49]
for number in my_list:
    print number*5
    print number + 4
print 'end'

# <codecell>

my_funct_list = [math.cos, math.sin, math.tan]
for function in my_funct_list:
    print function(3)

# <codecell>

my_list1 = [2, 3, 4]
my_list2 = ['a', 'b', 'c']
for number, string in zip(my_list1, my_list2):
    print number, string

# <markdowncell>

# ###If Statements

# <codecell>

#From above:
if fruit == 'banana':
    quantity = 2
elif fruit == 'carrot':
    quantity = 5
elif fruit == 'apple':
    quantity = 3
else:
    print 'I do not know how much fruit to by for the fruit you specified'

# <codecell>

number = 5
if number > 0:
    print 'positive'
elif number < 0:
    print 'negative'
else:
    print 'zero'

# <markdowncell>

# ###Other useful statements:
# 
# * while condition:
# * break - stop iterating
# * continue - go to next interation

# <markdowncell>

# ---
# 
# # Everything is an object
# 
# ---
# 
# **Everthing** really is an object in python.  Lists, functions, strings, even numbers.
# 
# This is important as we start to manipulate these data types.
# 
# We can get information about objects and ask them to do things 

# <markdowncell>

# ###Attributes: describing an object

# <codecell>

my_array = np.ones((4,3))
print my_array

# <codecell>

print my_array.T
print my_array.shape
print my_array.T.shape

# <codecell>

x = 4
print x.real
print x.imag

# <markdowncell>

# ###Methods: Doing something with or to an object

# <codecell>

print my_array.mean()
my_array = np.arange(10)
print my_array
print my_array.mean()

# <codecell>

print my_dict.keys()

# <codecell>

dir(my_dict)

# <codecell>

my_dict.values()

# <markdowncell>

# ###What else can you do with an object?

# <codecell>

help(my_dict.keys)

# <markdowncell>

# -----------------
# #Getting Help
# 
# -----------------

# <codecell>

help(my_array.mean)

# <codecell>

help(math.cos)

# <markdowncell>

# ## *Excercise:*  
# 
# 1.  Put your favorite astronomical target in a variable  (e.g. astro_obj = 'supernovae')
# 2.  Use the dir() function to find out how to:  
#     *  make everything in caps
#     *  count the occurance of each vowel, 'a','e','i','o','u'

# <codecell>

help(dir)

# <codecell>

astro_obj = 'brown dwarfs'
dir(astro_obj)

# <codecell>

print astro_obj.capitalize()

# <codecell>

print astro_obj.swapcase()
print astro_obj.upper()

# <codecell>

help(astro_obj.count)

# <codecell>

print "a:", astro_obj.count("a")
print "e:", astro_obj.count("e")
print "i:", astro_obj.count("i")
print "o:", astro_obj.count("o")
print "u:", astro_obj.count("u")

# <markdowncell>

# ---
# 
# # Errors and the Traceback
# 
# ---
# 
# It may look scary, but it is **EXTREMELY** helpful.
# 
# When you execute code or run a script, python executes the  
# instructions line by line until it reaches an error or the end of the code.
# 
# This means that the interpreter knows exactly where it was when it   
# encountered something that caused a crash, and will tell you exactly which  
# line of code caused the problem.
# 
# It also throws useful error messages, which can be useful for de-bugging.

# <codecell>

my_tuple = (1, 4, 5, 'a')
print my_tuple
print my_tuple[1]
my_tuple[1] = 8

# <markdowncell>

# This doesn't just work for math, it also works for incorrect syntax, missing variables, etc

# <markdowncell>

# ## *Exercise*
# 
# * Find and correct the errors in the cell below until the code runs all the way through without errors

# <codecell>

#ORIGINAL:
#
#first_name = 'justin
#last_name = 'ely'
#
#print first_name, ' ', middle_name, ' ', last_name
#
#age = 25 + 0j
#print 'And I am ', age.real_part, ' old'

##CORRECTED:

first_name = 'justin'
middle_name = ''
last_name = 'ely'

print first_name, ' ', middle_name, ' ', last_name

age = 25 + 0j
print 'And I am ', age.real, ' old'

# <codecell>

dir(age)

# <markdowncell>

# Remember: the traceback is your friend!  
#   
#   

# <markdowncell>

# ---------------------
# #Functions
# 
# ---------------------

# <markdowncell>

# Functions should be:
# 
# * *SMALL* When you write code, you should write short functions centered on a single task. Think of your code as an essay and each function as a paragraph. It is overwhelming to read an essay (or book) without paragraphs and you are likely to miss errors you would have otherwise caught. Small functions:
# 
#     * Improve readability
#     * Easy to reuse
#     * avoid repeating code with different variables
#     * avoid changing code in multiple places
# 
# * *WELL NAMED* Your function calls (and variable names) should describe exactly what you are doing. This makes your code very readable
# 
# Let's write a program to read a 2 column text file with number of UFO sightings for each month of a given year (data from: http://www.nuforc.org/webreports/ndxevent.html)

# <codecell>

def read_file(filename):
    ofile = open(filename, 'r')
    all_lines = ofile.readlines()
    return all_lines
def parse_line(iline):
    split_line = iline.split()
    split_line[1] = float(split_line[1])
    return split_line[0], split_line[1]

# <codecell>

all_lines = read_file('ufo_sightings_2011.txt')
date_list = []
ufo_num = []
for iline in all_lines:
    date, number_of_ufos = parse_line(iline)
    date_list.append(date)
    ufo_num.append(number_of_ufos)

# <codecell>

print date_list
print ufo_num

# <codecell>

dir(ufo_num)

# <codecell>


# <codecell>


# <markdowncell>

# ## *Exercise*
# 
# 1. Write a function to find the mean of a list of numbers
# 2. Use read_file, parse_file, and the mean function you just wrote to find the average number of UFO sightings per month in 2013

# <codecell>


# <codecell>



# <markdowncell>

# ##Move to text file
# 
# * part 1: copy and paste everything in, show that it runs the same from the command line and importing
# * part 2: add if __name__ == "__main__": show that it runs from the command line but not when imported. Talk about module
# * part 3: add in sys.argv to take filename
#     * discuss argument order of sys.argv
#     * import sys
#     * try different files

# <codecell>


