"""In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

Unlike Java and many other languages, Python variables do not require explicit declaration of type.
The type of the variable is inferred based on the value assigned.



x = 5
name = "Samantha"  
print(x)
print(name)"""


#Rules for Naming Variables
'''To use variables effectively, we must follow Python’s naming rules:

1. Variable names can only contain letters, digits and underscores (_).
2. A variable name cannot start with a digit.
3. Variable names are case-sensitive like myVar and myvar are different.
4. Avoid using Python keywords like if, else, for as variable names.'''

# Assigning Values to Variables
"""
Basic Assignment: Variables in Python are assigned values using the = operator.
x = 5
y = 3.14
z = "Hi"

Dynamic Typing: Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
x = 10
x = "Now a string"


Multiple Assignments
Assigning Same Value: Python allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
a = b = c = 100
print(a, b, c)

x, y, z = 1, 2.5, "Python"
print(x, y, z)

int(): Converts compatible values to an integer.
float(): Transforms values into floating-point numbers.
str(): Converts any data type into a string.

s = "10"  
n = int(s)
​
cnt = 5
f = float(cnt) 
​
age = 25
s2 = str(age)  
​
print(n)  
print(f)  
print(s2)
"""

# Type of Variable
"""In Python, we can determine the type of a variable using the type() function. This built-in function returns the type of the object passed to it.

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True
​
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))"""


#Deleting a Variable
"""We can remove a variable from the namespace using the del keyword. This deletes the variable and frees up the memory it was using.
x = 10
del x
print(x) """

# Practical Examples
'''1. Swapping Two Variables: Using multiple assignments, we can swap the values of two variables without needing a temporary variable.

a, b = 5, 10
a, b = b, a
print(a, b)

 2. Counting Characters in a String: Assign the results of multiple operations on a string to variables in one line.
word = "Python"
length = len(word)
print("Length of the word:", length)
'''







