import math
#Fundamental Data types
int
float
str
bool
list
tuple
set
dict  #dictonary

#Classes   -> custom types


#Specialized Data types

None


# int # float
print(2+4)
print(2-4)
print(2*4)
print(2/4)

print(2**4)
print(2//4)  #-> return integer example 0 
print(5 % 4) # => 1
print(5 % 3) # => 2


print(3+1.1)
print(int(9.9+1.1))

print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4))
print(type(2**4))
print(type(3+1.1))
print(type(9.9+1.1))

#Math functions
# round
print(round(3.1))
print(round(3.9))

#abs (absolute)

print(abs(-20))

# ceil(x)
print(math.ceil(4.2))  # Output: 5
print(math.ceil(-4.2)) # Output: -4


# copysign(x, y)
print(math.copysign(3, -5))  # Output: -3.0
print(math.copysign(-3, 5))  # Output: 3.0

# fabs(x)
print(math.fabs(-3.5))  # Output: 3.5
print(math.fabs(3.5))   # Output: 3.5


# factorial(x)
print(math.factorial(5))  # Output: 120
print(math.factorial(0))  # Output: 1


# floor(x)
print(math.floor(4.7))  # Output: 4
print(math.floor(-4.7)) # Output: -5


# fmod(x, y)
print(math.fmod(20, 3))  # Output: 2.0
print(math.fmod(20, 4))  # Output: 0.0


# frexp(x)
print(math.frexp(8))  # Output: (0.5, 4)


# fsum(iterable)
print(math.fsum([0.1, 0.2, 0.3]))  # Output: 0.6



# isfinite(x)
print(math.isfinite(10))  # Output: True
print(math.isfinite(float('inf')))  # Output: False


# isinf(x)
print(math.isinf(float('inf')))   # Output: True
print(math.isinf(float('-inf')))  # Output: True
print(math.isinf(10))             # Output: False



# isnan(x)
print(math.isnan(float('nan')))  # Output: True
print(math.isnan(10))            # Output: False


# ldexp(x, i)
print(math.ldexp(2, 3))  # Output: 16.0


# modf(x)
print(math.modf(4.5))  # Output: (0.5, 4.0)


# trunc(x)
print(math.trunc(4.9))  # Output: 4
print(math.trunc(-4.9)) # Output: -4 


# exp(x)
print(math.exp(1))  # Output: 2.718281828459045
print(math.exp(2))  # Output: 7.389056098930649



# expm1(x)
print(math.expm1(1))  # Output: 1.718281828459045
print(math.expm1(2))  # Output: 6.389056098930649


# log(x[, b])
print(math.log(10))       # Output: 2.302585092994046 (natural log)
print(math.log(100, 10))  # Output: 2.0 (log base 10)



# log1p(x)
print(math.log1p(1))  # Output: 0.6931471805599453


# log2(x)
print(math.log2(8))  # Output: 3.0


# log10(x)
print(math.log10(100))  # Output: 2.0


# pow(x, y)
print(math.pow(2, 3))  # Output: 8.0


# sqrt(x)
print(math.sqrt(16))  # Output: 4.0


# acos(x)
print(math.acos(1))  # Output: 0.0


# asin(x)
print(math.asin(1))  # Output: 1.5707963267948966


# atan(x)
print(math.atan(1))  # Output: 0.7853981633974483


# atan2(y, x)
print(math.atan2(1, 1))  # Output: 0.7853981633974483


# cos(x)
print(math.cos(math.pi))  # Output: -1.0


# hypot(x, y)
print(math.hypot(3, 4))  # Output: 5.0


# sin(x)
print(math.sin(math.pi/2))  # Output: 1.0


# tan(x)
print(math.tan(math.pi/4))  # Output: 0.9999999999999999 (approximately 1.0)


# degrees(x)
print(math.degrees(math.pi))  # Output: 180.0


# radians(x)
print(math.radians(180))  # Output: 3.141592653589793


# acosh(x)
print(math.acosh(1))  # Output: 0.0


# asinh(x)
print(math.asinh(1))  # Output: 0.881373587019543


# atanh(x)
print(math.atanh(0.5))  # Output: 0.5493061443340548


# cosh(x)
print(math.cosh(0))  # Output: 1.0


# sinh(x)
print(math.sinh(0))  # Output: 0.0


# tanh(x)
print(math.tanh(0))  # Output: 0.0


# erf(x)
print(math.erf(1))  # Output: 0.8427007929497149


# erfc(x)
print(math.erfc(1))  # Output: 0.1572992070502851


# gamma(x)
print(math.gamma(5))  # Output: 24.0


# lgamma(x)
print(math.lgamma(5))  # Output: 3.178053830347945


# pi
print(math.pi)  # Output: 3.


# operator precedence

print(20 + 3 * 4)
print(20 - 3 * 4) 
print((20 - 3) + 2 ** 2)

# BODMAS Rule
# ()
# **
# *
# /
# +
# -



# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)

print(((5 + 4) * 10) / 2)

print((5 + 4) * (10 / 2))

print(5 + (4 * 10) / 2)

print(5 + 4 * 10 // 2)

# complex datatypes

# In Python, the complex data type is used to represent complex numbers. A complex number is composed of a real part and an imaginary part. The imaginary part is denoted by the suffix 'j'.
# Here are some examples of how to work with complex numbers in Python:

# Creating Complex Numbers
# You can create a complex number by directly specifying its real and imaginary parts:


z1 = 3 + 4j
z2 = complex(5, -6)

print(z1)  # Output: (3+4j)
print(z2)  # Output: (5-6j)


# Accessing Real and Imaginary Parts
# You can access the real and imaginary parts of a complex number using the .real and .imag attributes:


z = 3 + 4j

print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0

# Complex Number Operations
# You can perform arithmetic operations with complex numbers, just like with other numeric types:


z1 = 3 + 4j
z2 = 1 - 2j

# Addition
print(z1 + z2)  # Output: (4+2j)

# Subtraction
print(z1 - z2)  # Output: (2+6j)

# Multiplication
print(z1 * z2)  # Output: (11-2j)

# Division
print(z1 / z2)  # Output: (-1+2j)


# Conjugate of a Complex Number
# The conjugate of a complex number is obtained by changing the sign of the imaginary part. You can use the .conjugate() method to get the conjugate:


z = 3 + 4j

print(z.conjugate())  # Output: (3-4j)


# Magnitude of a Complex Number
# The magnitude (or absolute value) of a complex number is its distance from the origin in the complex plane. You can use the abs() function to get the magnitude:

z = 3 + 4j

print(abs(z))  # Output: 5.0 (since sqrt(3^2 + 4^2) = 5)


# Example: Solving a Quadratic Equation with Complex Roots
# Consider solving the quadratic equation 
# 𝑎
# 𝑥
# 2
# +
# 𝑏
# 𝑥
# +
# 𝑐
# =
# 0
# ax 
# 2
#  +bx+c=0. The roots can be found using the quadratic formula:

# 𝑥
# =
# −
# 𝑏
# ±
# 𝑏
# 2
# −
# 4
# 𝑎
# 𝑐
# 2
# 𝑎


import cmath  # cmath module provides mathematical functions for complex numbers

a = 1
b = 2
c = 5

# Calculate the discriminant
d = b**2 - 4*a*c

# Find two solutions
sol1 = (-b + cmath.sqrt(d)) / (2*a)
sol2 = (-b - cmath.sqrt(d)) / (2*a)

print("The solutions are {} and {}".format(sol1, sol2))
# Output: The solutions are (-1+2j) and (-1-2j)


# Summary
# Python's complex data type and the cmath module make it easy to work with complex numbers, providing attributes and functions for various operations and mathematical computations.


# Bin Datatypes
# In Python, the bin function is used to convert an integer number to a binary string. The binary string is prefixed with '0b'.
# Here are some examples and explanations on how to use the bin function and work with binary data in Python:

# Converting an Integer to a Binary String

number = 10
binary_representation = bin(number)
print(binary_representation)  # Output: '0b1010'


# Removing the '0b' Prefix
number = 10
binary_representation = bin(number)[2:]
print(binary_representation)  # Output: '1010'


#Converting a Binary String to an Integer
binary_string = '1010'
number = int(binary_string, 2)
print(number)  # Output: 10


# Working with Binary Literals
binary_literal = 0b1010
print(binary_literal)  # Output: 10

#Example: Bitwise Operations

a = 0b1010  # 10 in binary
b = 0b1100  # 12 in binary

# Bitwise AND
result_and = a & b
print(bin(result_and))  # Output: '0b1000' (8 in decimal)

# Bitwise OR
result_or = a | b
print(bin(result_or))  # Output: '0b1110' (14 in decimal)

# Bitwise XOR
result_xor = a ^ b
print(bin(result_xor))  # Output: '0b0110' (6 in decimal)

# Bitwise NOT
result_not = ~a
print(bin(result_not))  # Output: '-0b1011' (-11 in decimal, in two's complement form)


#Example: Shifting Bits

a = 0b1010  # 10 in binary

# Left shift by 2 bits
left_shift = a << 2
print(bin(left_shift))  # Output: '0b101000' (40 in decimal)

# Right shift by 2 bits
right_shift = a >> 2
print(bin(right_shift))  # Output: '0b10' (2 in decimal)

# int to bin and vice-versa 
print(bin(5)) # 0b101
print(int('0b101',2))

#Summary
#The bin function and binary literals in Python allow you to easily convert integers to binary strings and perform bitwise operations. These capabilities are particularly useful in fields like cryptography, data compression, and low-level programming where binary data manipulation is common.


# Python Keywords
# Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:

# Keyword	Description
# and	A logical operator
# as	To create an alias
# assert	For debugging
# break	To break out of a loop
# class	To define a class
# continue	To continue to the next iteration of a loop
# def	To define a function
# del	To delete an object
# elif	Used in conditional statements, same as else if
# else	Used in conditional statements
# except	Used with exceptions, what to do when an exception occurs
# False	Boolean value, result of comparison operations
# finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	To create a for loop
# from	To import specific parts of a module
# global	To declare a global variable
# if	To make a conditional statement
# import	To import a module
# in	To check if a value is present in a list, tuple, etc.
# is	To test if two variables are equal
# lambda	To create an anonymous function
# None	Represents a null value
# nonlocal	To declare a non-local variable
# not	A logical operator
# or	A logical operator
# pass	A null statement, a statement that will do nothing
# raise	To raise an exception
# return	- To exit a function and return a value
# True -	Boolean value, result of comparison operations
# try -	To make a try...except statement
# while	- To create a while loop
# with	- Used to simplify exception handling
# yield -	To return a list of values from a generator




# variable

a = 10
print(a)
iq =190
print(iq)
a=20
print(a)

# naming variable

# snake_case  -> user_id
# Start with lowercase or underscore -> user_id or _user_id
# Letter,numbers, underscore -> us4er_id
# Case sensative =>  user_ID
# Don't overwrite keywords. -> dont use keywords


# constant

PI = 3.14

print(PI)

# expression vs statement

iq = 100 # statement
user_age = iq / 5  # here iq / 5 is expression and user_age = iq / 5 is statement

# augmented assignment operator


some_value = 5
some_value += 2
print(some_value)

# string


print(type("hi hello there 24!"))
username = 'supercode'
password = 'superscrect'
long_string = '''
WOW
0 0
___
---
'''
print(long_string)

first_name = "abhinay"
last_name = "yadav"
full_name = first_name + ' ' +last_name
print(full_name)

#string concatenation
print('hello ' + 'world')
print(type(str(100)))
print('hello ' + str(5))

# Escape  sequence


weather = '\tit\'s "kind of" sunny' 
# \t -> give tab space
# \n -> create in  new line
print(weather)


#formatted string

name = 'Abhinay'
age =55
print('hi',name)

print(f'hi {name}.you are {age} years olds')
print('hi {}.you are {} years olds'.format('Abhinay',"24"))
print('hi {}.you are {} years olds'.format(name,age))
print('hi {1}.you are {0} years olds'.format(name,age))
print('hi {new_name}.you are {age} years olds'.format(new_name="sally",age=76))


#string index

selfish = 'me me me'

# 0 1 2 3 4 5 6 7 store in memory
print(selfish[0])
print(selfish[1])
print(selfish[2])
print(selfish[3])
print(selfish[4])
print(selfish[5])
print(selfish[6])
print(selfish[7])

selfishness = '01234567'
# [start:stop]
print(selfishness[0:2])  # 01
print(selfishness[0:7])  # 0123456
print(selfishness[0:8])  # 01234567

# [start:stop:stepover]
print(selfishness[0:8:2])  # 0246
print(selfishness[1:])  # 1234567
print(selfishness[:5])  # 01234
print(selfishness[::])  # 01234567
print(selfishness[-1])  # 7
print(selfishness[-2])  # 6
print(selfishness[::-1])  # 76543210
print(selfishness[::-2])  # 7531


# Immutabiity

# string_immu = '01234567'

# string_immu[0] = '8' # it will through error beacuse string can be changed it can be reassign

# print(string_immu)

# String builtin function

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


# Built-in Functions

# A
# abs()
# aiter()
# all()
# anext()
# any()
# ascii()

# B
# bin()
# bool()
# breakpoint()
# bytearray()
# bytes()

# C
# callable()
# chr()
# classmethod()
# compile()
# complex()

# D
# delattr()
# dict()
# dir()
# divmod()

# E
# enumerate()
# eval()
# exec()

# F
# filter()
# float()
# format()
# frozenset()

# G
# getattr()
# globals()

# H
# hasattr()
# hash()
# help()
# hex()

# I
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()
# L
# len()
# list()
# locals()

# M
# map()
# max()
# memoryview()
# min()

# N
# next()

# O
# object()
# oct()
# open()
# ord()

# P
# pow()
# print()
# property()




# R
# range()
# repr()
# reversed()
# round()

# S
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()

# T
# tuple()
# type()

# V
# vars()

# Z
# zip()

# _
# __import__()


print(len("hello"))


# boolean
bool_name = 'Andrei'

is_cool = True

is_cool = False


print(bool(0))
print(bool(1))


# type conversion

birth_year = input('what is you birth year?\n')


age = 2024 - int(birth_year)
print(f'your age is {age}')


# coomenting in python 

# single line comment

"""
If I really hate pressing `enter` and
typing all those hash marks, I could
just do this instead
"""

# Exercise Password Checker

username = input('Enter your username:\t')
password = input('Enter you password:\t')

secret_password = len(password) * '*'
print(f'Hey {username}, your password {secret_password} is {len(password)}  letters long.')





























































