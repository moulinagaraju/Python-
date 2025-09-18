# Python-n=int(input(" n= "))
sum=0
temp=n
while n:
r=n%10
n=n//10
sum=sum+r
print("Sum of digits of", temp, "is",sum)
n= 8945
Sum of digits of 8945 is 26

n=int(input(" n= "))
sum=1
temp=n
while n:
r=n%10
n=n//10
sum=sum*r
print("Product of digits of", temp , "is",sum)
n= 7865
Product of digits of 7865 is 1680

n=int(input(" n= "))
sum=0
temp=n
while n:
r=n%10
n=n//10
sum=sum*10+r
print("Reverse of", temp , "is",sum)
if sum==temp:
print(temp, "is a palindrome")
else:
print(temp, "is not a palindrome")
n= 6784
Reverse of 6784 is 4876
6784 is not a palindrome

n=int(input(" n= "))
sum=0
temp=n
k=len(str(n))
while n:
r=n%10
n=n//10
sum=sum+pow(r,k)
if sum==temp:
print(temp, "is an Armstrong number")
else:
print(temp, "is not an Armstrong number")
n= 369
369 is not an Armstrong number



n=int(input(" n= "))

sum=0

temp=n

while n:

r=n%10

n=n//10

factr=1

for i in range(1,r+1):

factr=factr*i

sum=sum+factr

if sum==temp:

print(temp, "is a strong number")

else:

print(temp, "is not a strong number")

n= 145

145 is a strong number


#1. Write a program to find the largest element among three Numbers.

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

c = int(input("Enter third number: "))

largest = a if a > b and a > c else b if b > c else c

print("The largest number is:", largest)

The largest number is: 23

a = 10

b = 25

c = 15

maximum = max(a, b, c)

print("Maximum is:", maximum)

a = 10

b = 25

c = 15

if a >= b and a >= c:

maximum = a

elif b >= a and b >= c:

maximum = b

else:

maximum = c

print("Maximum is:", maximum)

def find_max(a, b, c):

if a >= b and a >= c:

return a

elif b >= a and b >= c:

return b

else:

return c

print("Maximum is:", find_max(10, 25, 15))

numbers = [10, 25, 15]

numbers.sort()

print("Maximum is:", numbers[-1])

Maximum is: 25

# 2. prime numbers within an interval

a = int(input("Enter start of interval: "))

b = int(input("Enter end of interval: "))

print("Prime numbers between", a , "and", b, "are:")

for i in range(a, b + 1):

if i > 1:
for j in range(2, int(i**0.5)+1):

if i % j == 0:

break

else:

print(i, end=' ')

Prime numbers between 40 and 200 are:

41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149

151 157 163 167 173 179 181 191 193 197 199

#3. swap two numbers without using a temporary variable

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")

print("First number:", a)

print("Second number:", b)

After swapping:

First number: 36

Second number: 27

# 4 Operators

a = 10

b = 5

# i) Arithmetic Operators

print("Addition:", a + b)

print("Subtraction:", a - b)

print("Multiplication:", a * b)

print("Division:", a / b)

# ii) Relational Operators

print("a > b:", a > b)

# iii) Assignment Operators

a += 3

print("a after += 3:", a)

# iv) Logical Operators

print("Logical AND:", a > 5 and b < 10)

# v) Bitwise Operators

print("Bitwise AND:", a & b)

# vi) Ternary Operator

max_val = a if a > b else b

print("Max using ternary:", max_val)

# vii) Membership Operators

print("5 in [1,2,3,4,5]:", 5 in [1, 2, 3, 4, 5])

# viii) Identity Operators

x = 10

y = 10

print("x is y:", x is y)


Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
a > b: True
a after += 3: 13
Logical AND: True
Bitwise AND: 5
Max using ternary: 13
5 in [1,2,3,4,5]: True
x is y: True
#5. add and multiply complex numbers
a = complex(input("Enter first complex number (e.g. 2+3j): "))
b = complex(input("Enter second complex number: "))
print("Addition:", a + b)
print("Multiplication:", a * b)
Addition: (2+7j)
Multiplication: (-36+2j)
#6. multiplication table of a given number
num = int(input("Enter a number to print its multiplication table: "))
n1 = int(input("Enter a number 10 or 20: "))
for i in range(1, n1+1):
print(f"{num} x {i} = {num * i}")
16 x 1 = 16
16 x 2 = 32
16 x 3 = 48
16 x 4 = 64
16 x 5 = 80
16 x 6 = 96
16 x 7 = 112
16 x 8 = 128
16 x 9 = 144
16 x 10 = 160
16 x 11 = 176
16 x 12 = 192
16 x 13 = 208
16 x 14 = 224
16 x 15 = 240
16 x 16 = 256
16 x 17 = 272
16 x 18 = 288
16 x 19 = 304
16 x 20 = 320


def operations(a, b):

add = a + b

sub = a - b

mul = a * b

div = a / b

quo = a // b

rem = a % b

return add, sub, mul, div , quo, rem

u, v, w, x, y, z = operations(17, 5)

print("Addition:", u)

print("Addition:", v)

print("Subtraction:", w)

print("Multiplication: ", x)

print("Division: ", y)

print("Remainder: ", z)

Addition: 22

Addition: 12

Subtraction: 85

Multiplication: 3.4

Division: 3

Remainder: 2

#8. Function using default arguments

def greet(name="Guest"):

print("Hello,", name)

greet("Satya")

greet()10. Check if substring is present in a string

Hello, Satya

Hello, Guest

#9. Function using default arguments

def string_length(s):

count = 0

for _ in s:

count += 1

return count

text = input("Enter a string: ")

print("Length of string:", string_length(text))

Length of string: 5

#10. Check if substring is present in a string

string = input("Enter the main string: ")

substring = input("Enter the substring: ")

if substring in string:

print("Substring is present.")

else:

print("Substring is not present.")


NRIIT

#11. List operations: addition, insertion, slicing

lst = [10, 20, 30, 40]

# Addition (append)

lst.append(50)

print("After addition:", lst)

# Insertion

lst.insert(2, 25)

print("After insertion at index 2:", lst)

# Slicing

print("Slicing from index 1 to 4:", lst[1:5])

After addition: [10, 20, 30, 40, 50]

After insertion at index 2: [10, 20, 25, 30, 40, 50]

Slicing from index 1 to 4: [20, 25, 30, 40]

#12. Perform any 5 built-in functions on a list

lst = [4, 2, 9, 1, 5]

print("Original list:", lst)

print("Length:", len(lst))

print("Maximum:", max(lst))

print("Minimum:", min(lst))

print("Sorted list:", sorted(lst))

print("Sum:", sum(lst))

Original list: [4, 2, 9, 1, 5]

Length: 5

Maximum: 9

Minimum: 1

Sorted list: [1, 2, 4, 5, 9]

Sum: 21

In [ ]:

In [4]:

In [5]:

In [ ]:


#13. 12. Perform any 5 built-in functions on a list

# Creating tuples

student1 = ("Krisna", 20, "Guntur", "NRIIT")

student2 = ("Rahul", 22, "Ongole", "RVRJCCE")

# Concatenating tuples

combined = student1 + student2

# Printing result

print("Concatenated Tuple:", combined)

Concatenated Tuple: ('Krisna', 20, 'Guntur', 'NRIIT', 'Rahul', 22, 'Ongole', 'R

VRJCCE')

#14. Count Number of Vowels in a String (No control flow)

# Using sum and lambda without explicit loops

s = "Artificial Intelligence"

vowels = 'aeiouAEIOU'

# Count vowels using map and lambda

count = sum(map(lambda c: c in vowels, s))

print("Number of vowels:", count)

Number of vowels: 10

#15. Check if Key Exists in a Dictionary

# Sample dictionary

data = {"name": "John", "age": 25, "city": "Hyderabad"}

# Check key existence

key = "age"

if key in data:

print(f"Key '{key}' exists in the dictionary.")

else:

print(f"Key '{key}' does not exist.")

Key 'age' exists in the dictionary.

#16. Add New Key-Value Pair to Dictionary

# Existing dictionary

profile = {"name": "Sita", "age": 21}

# Add new key-value pair

profile["college"] = "IIT Delhi"

print("Updated Dictionary:", profile)

Updated Dictionary: {'name': 'Sita', 'age': 21, 'college': 'IIT Delhi'}

#17. Sum All Items in a Dictionary

# Dictionary with numeric values

marks = {"Math": 85, "Physics": 90, "Chemistry": 80}

# Summing values
total = sum(marks.values())

print("Total Marks:", total)

Total Marks: 255


#18. Sort words in a file (convert to lowercase) and write to another file

# Read words from input.txt, sort and write to output.txt

with open("input.txt", "r") as infile:

words = infile.read().lower().split()

words.sort()

with open("output.txt", "w") as outfile:

outfile.write(" ".join(words))

print("Words sorted and written to output.txt")

Words sorted and written to output.txt

#19. Print each line of a file in reverse order

with open("input.txt", "r") as file:

lines = file.readlines()

# Reverse the order of lines

for line in reversed(lines):

print(line.strip())

Banana Apple Orange Kiwi Grape

#20. Count characters, words, and lines in a file

with open("input.txt", "r") as file:

text = file.read()

lines = text.splitlines()

words = text.split()

chars = len(text)

print("Lines:", len(lines))

print("Words:", len(words))

print("Characters:", chars)

Lines: 1

Words: 5

Characters: 30

#21. Array operations: create, display, append, insert, reverse

arr = [10, 20, 30]

print("Original array:", arr)

# Append

arr.append(40)

print("After append:", arr)

# Insert

arr.insert(2, 25)

print("After insert at index 2:", arr)

# Reverse

arr.reverse()

print("After reverse:", arr)
Original array: [10, 20, 30]

After append: [10, 20, 30, 40]

After insert at index 2: [10, 20, 25, 30, 40]

After reverse: [40, 30, 25, 20, 10]

#22. Add, transpose, and multiply two matrices

import numpy as np

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# Add

print("Addition:\n", A + B)

# Transpose

print("Transpose of A:\n", A.T)

# Multiply

print("Multiplication:\n", np.dot(A, B))

Addition:

[[ 6 8]

[10 12]]

Transpose of A:

[[1 3]

[2 4]]

Multiplication:

[[19 22]

[43 50]]

#23. Create a class representing a shape with area and perimeter

class Rectangle:

def __init__(self, length, breadth):

self.length = length

self.breadth = breadth

def area(self):

return self.length * self.breadth

def perimeter(self):

return 2 * (self.length + self.breadth)

# Example

r = Rectangle(5, 3)

print("Area:", r.area())

print("Perimeter:", r.perimeter())

Area: 15

Perimeter: 16

import math

from abc import ABC, abstractmethod

# Base class

class Shape(ABC):

@abstractmethod

def area(self):

pass

@abstractmethod
def perimeter(self):

pass

# Circle subclass

class Circle(Shape):

def __init__(self, radius):

self.radius = radius

def area(self):

return math.pi * self.radius ** 2

def perimeter(self):

return 2 * math.pi * self.radius

# Square subclass

class Square(Shape):

def __init__(self, side):

self.side = side

def area(self):

return self.side ** 2

def perimeter(self):

return 4 * self.side

# Triangle subclass (assuming it's a general triangle)

class Triangle(Shape):

def __init__(self, a, b, c):

self.a = a

self.b = b

self.c = c

def area(self):

# Using Heron's formula

s = (self.a + self.b + self.c) / 2

return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

def perimeter(self):

return self.a + self.b + self.c# Example usageif __name__ == "__main__":

shapes = [ Circle(5),Square(4),Triangle(3, 4, 5)]

for shape in shapes:

print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")

print(f"{shape.__class__.__name__} Perimeter: {shape.perimeter():.2f}\n")

Circle Area: 78.54

Circle Perimeter: 31.42

Square Area: 16.00

Square Perimeter: 16.00

Triangle Area: 6.00

Triangle Perimeter: 12.00


#24. Check if JSON string contains a complex object

import json

def contains_complex(json_str):

try:

obj = json.loads(json_str)

return any(isinstance(v, complex) for v in obj.values())

except:

return False

# Example

print(contains_complex('{"a": 2, "b": 3+4j}'))

False

#25. NumPy array creation using array()

import numpy as np

arr = np.array([[1, 2 ,3], [4, 5, 6]])

print("Array:\n", arr)

Array:

[[1 2 3]

[4 5 6]]

#26. Use of ndim, shape, size, dtype

print("Dimensions:", arr.ndim)

print("Shape:", arr.shape)

print("Size:", arr.size)

print("Data type:", arr.dtype)

Dimensions: 2

Shape: (2, 3)

Size: 6

Data type: int32

#27. Basic slicing, integer and Boolean indexing

# Slicing

print("Slice:\n", arr[:, 1]) # all rows index 1

# Integer indexing

print("Integer index:", arr[1, 0]) # 2nd row 1st column

# Boolean indexing

print("Greater than 2:\n", arr[arr > 2])

Slice:

[2 5]

Integer index: 4

Greater than 2:

[3 4 5 6]

#28. Find min, max, sum, cumulative sum

print("Minimum:", arr.min())

print("Maximum:", arr.max())

print("Sum:", arr.sum())
print("Cumulative sum:\n", np.cumsum(arr))

Minimum: 1

Maximum: 6

Sum: 21

Cumulative sum:

[ 1 3 6 10 15 21]

#29. Dictionary to Pandas DataFrame + head() and selection

import pandas as pd

data = { "ID": list(range(1, 11)), "Age": [21, 22, 23, 21, 24, 25, 22, 23, 24,

"City": ["Delhi", "Mumbai", "Chennai", "Delhi", "Mumbai", "Chennai", "Delhi"

"Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"] }

df = pd.DataFrame(data)

# (a) Apply head()

print("Head of DataFrame:\n", df.head())

# (b) Data selection

print("Only Score column:\n", df["Score"])

print("Rows where Score > 90:\n", df["Score"] > 90)

Head of DataFrame:

ID Age Score City Gender

0 1 21 88 Delhi M

1 2 22 92 Mumbai F

2 3 23 85 Chennai M

3 4 21 90 Delhi F

4 5 24 91 Mumbai M

Only Score column:

0 88

1 92

2 85

3 90

4 91

5 87

6 89

7 93

8 94

9 90

Name: Score, dtype: int64

Rows where Score > 90:

0 False

1 True

2 False

3 False

4 True

5 False

6 False

7 True

8 True

9 False

Name: Score, dtype: bool

#30. Scatter plot between two DataFrame columns

import matplotlib.pyplot as plt
plt.scatter(df["Age"], df["Score"])

plt.xlabel("Age")

plt.ylabel("Score")

plt.title("Age vs Score")

plt.grid(True)

plt.show()



# Check the given number is even or odd

# Sum, sum of squares, sum of cubes of n natural numbers

n=int(input('Enter n value: '))

if n%2==0:

print('The Given Number',n,'is even')

else:

print('The Given Number',n,'is odd')

# Sum of natural numbers

sum_n=n*(n+1)/2

print('The Given Sum of ',n,'natural numbers is',sum_n)

# Sum of squares of n natural numbers

sum_n_sq=n*(n+1)*(2*n+1)/6

print('The Given Sum of ',n,'squares of natural numbers is',sum_n_sq)

# Sum of cubes of n natural numbers

sum_n_cu=n*n*(n+1)*(n+1)/4

print('The Given Sum of ',n,'cubes of natural numbers is',sum_n_cu)

The Given Number 7 is odd

The Given Sum of 7 natural numbers is 28.0

The Given Sum of 7 squares of natural numbers is 140.0

The Given Sum of 7 cubes of natural numbers is 784.0

# Arithmetic Progression

# Take input of 'a','d' and 'n'

a = float(input("Enter the value of a: "))

d = float(input("Enter the value of d: "))

n = int(input("Enter the value of n: "))

print("Terms in Arithmetic Progression")

for i in range(1,n+1):

t_n = a + (i-1)*d

print(t_n)

print("nth term in AP : ", t_n)

#Sum of first n terms in Arithmetic Progression

S_n = n*(2*a + (n-1)*d) /2

print("Sum of first n terms: ", S_n)

Terms in Arithmetic Progression

5.0

8.0

11.0

14.0

17.0

20.0

23.0

26.0

29.0

32.0

nth term in AP : 32.0

Sum of first n terms: 185.0

# Geometic Progression

# Take input of 'a','d' and 'n'

a = int(input("Enter the value of a: "))

r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))

print(" Terms in Geometic Progression")

for i in range(1,n+1):

t_n = a *r**(i-1)

print(t_n)

print("nth term in GP: ", t_n)

#Sum of first n terms in Geometic Progression

S_n = a*(pow(r,n)-1)/(r-1)

print("Sum of first n terms: ", S_n)

Terms in Geometic Progression

3

6

12

24

nth term in GP: 24

Sum of first n terms: 45.0

# A: Final Amount, P: Initial Principal r: Annual Interest Rate %

# n: Number of compounding periods per year t: Number of years-Time period

P = float(input("Enter the value of P: "))

r =float(input("Enter the value of r: "))

n = float(input("Enter the value of n: "))

t = float(input("Enter the value of t: "))

r=r/100

A1=P*pow(1+r/n, n*t)

A2=P*pow((n+r)/n, n*t)

A3=P*(1+r/n)**(n*t)

A4=P*((n+r)/n)**(n*t)

print(' Amount1=%.2f'%A1,"\n",'Amount2=%.2f'%A2,"\n",

'Amount3=%.2f'%A3,"\n",'Amount4=%.2f'%A4)

CI=A4-P

print('Compound Interest=%8.2f'%CI)

Amount1=6326.60

Amount2=6326.60

Amount3=6326.60

Amount4=6326.60

Compound Interest= 1326.60

P = float(input("Enter the value of P: "))

r =float(input("Enter the value of r: "))

n = float(input("Enter the value of n: "))

t = float(input("Enter the value of t: "))

r=r/100

A1=P*pow(1+r/n, n*t)

A2=P*pow((n+r)/n, n*t)

A3=P*(1+r/n)**(n*t)

A4=P*((n+r)/n)**(n*t)

print('Amount=%8.2f%8.2f%8.2f%8.2f'%(A1,A2,A3,A4))

CI=A1-P

print('Compound Interest=%8.2f'%CI)

Amount= 6341.21 6341.21 6341.21 6341.21

Compound Interest= 1341.21
from math import tan, pi

# Polygon Properties

n=int(input('Number of sides of Polygon n:'))

a = float(input("Enter the Length of a Side a: "))

sum_ext=360

ang_ext=360/n

sum_int=180*n-360

ang_int=sum_int/n

n_tri=n-2

n_diag=n*(n-3)/2

area = n * a**2 / (4 * tan(pi/n))

print('%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f %8.2f '%(sum_ext,ang_ext, sum_int,ang_int

360.00 72.00 540.00 108.00 3.00 5.00 110.11

number=int( input("Enter given number: "))

nd=len(str(number))

n1=int(input('Enter n1: '))

n2= int(input('Enter n2: '))

a=int(input('Enter a: '))

b= int(input('Enter b:'))

# Computes first n1 digits

first_n1 = number//pow(10,nd-n1)

# Computes last n2 digits

last_n2 = number % pow(10,n2)

digit_a_nd=number % 10**(nd-a+1)

digit_a_b=digit_a_nd//10**(nd-b)

digit_1_b=number//10**(nd-b)

digit_a_b1=digit_1_b%10**(b-a+1)

print("\nFirst {0} digits = {1}".format(n1, first_n1))

print(" \nLast {0} digits = {1}" .format( n2,last_n2))

print(" \nFrom {0} to {1} digits = {2} and {3}" .format( a,b,digit_a_b,digit_a_b1

First 10 digits = 1234567898

Last 8 digits = 87654321

From 5 to 10 digits = 567898 and 567898

#number of different characters of same size strings

def diff(a, b):

return [i for i in range(len(a)) if a[i] != b[i]]

a = input("Enter string1: ")

b = input("Enter string2: ")

print(diff(a, b))

[0, 1, 3, 4]

# factors of a given number

def print_factors(x):

print("The factors of", x, "are:")

for i in range(1, x+1):

if x % i == 0:

print(i)

num = int(input("Enter a number: "))

In [13]:

print_factors(num)

The factors of 12 are:

1

2

3

4

6

12

# Proper factors of a given number

def print_factors(x):

print("The factors of", x, "are:")

for i in range(1, x//2+1):

if x % i == 0:

print(i)

num = int(input("Enter a number: "))

print_factors(num)

The factors of 12 are:

1

2

3

4

6

n1=int(input('Enter ist number: '))

n2=int(input('Enter 2nd number: '))

sum1=sum2=0

n11=n1//2+1

n22=n2//2+1

for i in range(1,n11):

if n1%i==0:

sum1+=i

for j in range(1,n22):

if n2%j==0:

sum2+=j

if(sum1==n2 and sum2==n1):

print(n1,' and ',n2,'are Amicable numbers')

else:

print(n1,' and ',n2,'are not Amicable numbers')

220 and 284 are Amicable numbers

def factorial(n):

if n == 0 or n == 1:

return 1

else:

return n * factorial(n - 1)

lst = [145, 375, 100, 2, 10, 40585, 0]

strong_nums = list(filter(lambda num: sum(factorial(int(digit))

for digit in str(num)) == num, lst))

print("Strong numbers in the given list are:", strong_nums)

Strong numbers in the given list are: [145, 2, 40585]

# sorting true or false

def is_sorted(lst, key=lambda x: x):

for i, el in enumerate(lst[1:]):

if key(el) < key(lst[i]): # i is the index of the previous element

return False

return True

print(is_sorted([5, 9, 11, 67, 70]))

True

#nth root of x

def root():

x = int(input("Enter x value: "))

n = int(input("Enter n value: "))

if n == 0:

n = 2

r = float(pow(x, 1 / n))

return r

print(root())

1.9679896712654303

n=int(input('Enter Factorial n:'))

nz=0;

while(n>0):

n=n//5

nz=nz+n

print(nz)

print("Number of trailing Zeros = %d"%nz)

923

1107

1143

1150

1151

1151

Number of trailing Zeros = 1151

print("Enter nth power a prime number as factor of a factorial:");

n=int(input('Enter Factorial n:'))

n1=int(input('Enter Base n1:'))

temp=n

nthpower=0;

while(n>0):

n=n//n1

nthpower=nthpower+n

print("Power of given number", n1," as factor of",temp , " =", nthpower)
Enter nth power a prime number as factor of a factorial:

Power of given number 13 as factor of 170 = 14

def compute_HCF(x, y):

# choose the greater number

if x > y:

min = y

else:

min = x

while(True):

if x % min== 0 and y % min == 0:

hcf = min

break

min -= 1

return hcf

num1 = int(input('Enter num1: '))

num2 = int(input('Enter num2: '))

print("The HCF is", compute_HCF(num1, num2))

The HCF is 6

a = int(input("1stnumber:"))

b = int(input("2ndnumber:"))

HCF = 1

if a>b:

min=b

else:

min=a

for i in range(2,min+1):

if(a%i==0 and b%i==0):

HCF = i

print("First Number is: ",a)

print("Second Number is: ",b)

print("HCF of the numbers is: ",HCF)

First Number is: 24

Second Number is: 40

HCF of the numbers is: 8

a = int(input("1stnumber:"))

b = int(input("2ndnumber:"))

HCF = 1

if a>b:

min=b

else:

min=a

while(a%min!=0 or b%min!=0):

min=min-1

HCF = min

print("First Number is: ",a)

print("Second Number is: ",b)

print("HCF is: ",HCF)
First Number is: 16

Second Number is: 24

HCF is: 8

# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

# choose the greater number

if x > y:

max = x

else:

max = y

while(True):

if((max % x == 0) and (max % y == 0)):

lcm = max

break

max += 1

return lcm

num1 = int(input('Enter num1: '))

num2 = int(input('Enter num2: '))

print("The L.C.M. is", compute_lcm(num1, num2))

The L.C.M. is 48

# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

# choose the greater number

if x > y:

max = x

else:

max = y

for i in range(max,x*y+1):

if i% x == 0 and i % y == 0:

lcm = i

return lcm

num1 = int(input('Enter num1: '))

num2 = int(input('Enter num2: '))

print("The L.C.M. is", compute_lcm(num1, num2))

The L.C.M. is 299

m1 = int(input("Enter the value of m1: "))

d1 = float(input("Enter the value of d1: "))

h1 = float(input("Enter the value of h1: "))

w1 = float(input("Enter the value of w1: "))

value = input("Enter m2 or d2 or h2 or w2:")

print("m2=1 or d2=1 or h2=1 or w2=1:")

m2 = float(input("Enter the value of m2: "))

d2 = float(input("Enter the value of d2: "))

h2 = float(input("Enter the value of h2: "))

w2 = float(input("Enter the value of w2: "))

match value:

case "m2":

m2=m1*d1*h1*w2/(w1*d2*h2)
print('Persons Required M2=',m2)

case "d2":

d2=m1*d1*h1*w2/(w1*m2*h2)

print('Days Required D2=',d2)

case "h2":

h2=m1*d1*h1*w2/(w1*m2*d2)

print('hours per Day h2=',h2)

case "w2":

w2=m2*d2*h2*w1/(m1*d1*h1)

print('howork done/items w2=',w2)

m2=1 or d2=1 or h2=1 or w2=1:

Persons Required M2= 25.6

costly=int(input('Enter Costly: '))

cheap=int(input('Enter Cheap: '))

mean=int(input('Enter Mean: '))

x=mean-cheap

y=costly-mean

xbyy=(mean-cheap)/(costly-mean)

total=int(input('Enter total: '))

#mean*(x+y)=costly*x+cheap*y

x1=x/(x+y)*total

y1=y/(x+y)*total

mean=(costly*x1+cheap*y1)/(x1+y1)

y1=(costly-mean)*x1/(mean-cheap)

x1=(mean-cheap)*y1/(costly-mean)

costly=(mean*(x1+y1)-cheap*y1)/x1

cheap=(mean*(x1+y1)-costly*x1)/y1

sumxy=(costly*x1+cheap*y1)/mean

print('x/y=%2f x1=%d y1=%d sumxy=%d '%(xbyy,x1,y1,x1+y1))

x/y=0.666667 x1=40 y1=60 sumxy=100

date=int(input('Enter Date:'))

month=int(input('Enter Month:'))

year = int(input("Enter year(yyyy):"))

if year%4 == 0 and year%100!=0 or year%400==0:

odd_days=[0,3,4,0,2,5,0,3,6,1,4,6,2]

else:

odd_days=[0,3,3,6,1,4,6,2,5,0,3,5,1]

year1=year-1

year2=year1%400

if year2>300:

odd1=1

year3=year2%300

elif year2>200:
odd1=3

year3=year2%200

elif year2>100:

odd1=5

year3=year2%100

else:

year3=year2

odd1=0

odd2=(year3+year3//4)%7

odd3=(date+odd_days[month-1])%7

odd=(odd1+odd2+odd3)%7

print(odd)

day_names = ['Sunday', 'Monday', 'Tuesday',

'Wednesday', 'Thursday', 'Friday', 'Saturday']

print(day_names[odd])

Enter Date:15

Enter Month:8

Enter year(yyyy):2047

4

Thursday

h=[0,1,2,3,4,5,6,7,8,9,10,11]

angle=30

for i in range(0,12):

m1=(30*h[i]-angle)/5.5

if(m1<0):

m1=(30*h[i]+360-angle)/5.5

if m1==60:

h[i]=h[i]+1

m2=(30*h[i]+angle)/5.5

# if m2>60:

print(h[i],' h m1= ', m1, 'm m2=',m2, 'm')

1 h m1= 60.0 m m2= 10.909090909090908 m

1 h m1= 0.0 m m2= 10.909090909090908 m

2 h m1= 5.454545454545454 m m2= 16.363636363636363 m

3 h m1= 10.909090909090908 m m2= 21.818181818181817 m

4 h m1= 16.363636363636363 m m2= 27.272727272727273 m

5 h m1= 21.818181818181817 m m2= 32.72727272727273 m

6 h m1= 27.272727272727273 m m2= 38.18181818181818 m

7 h m1= 32.72727272727273 m m2= 43.63636363636363 m

8 h m1= 38.18181818181818 m m2= 49.09090909090909 m

9 h m1= 43.63636363636363 m m2= 54.54545454545455 m

10 h m1= 49.09090909090909 m m2= 60.0 m

11 h m1= 54.54545454545455 m m2= 65.45454545454545 m

# Python program to find angle between hour and minute hands

# Function to Calculate angle b/w hour hand and minute hand

def calcAngle(h,m):

# validate the input

if (h < 0 or m < 0 or h > 24 or m > 60):

print('Wrong input-Solution for the given data is as follows:
if h == 12:
h = 0
if m >=60:
h=h+m//60
m=m%60
if(h>12):
h = h%12;
# Calculate the angles moved by hour and minute hands
print('h=',h)
print('m=',m)
hour_angle = 0.5 * (h * 60 + m)
minute_angle = 6 * m
# Find the difference between two angles
angle = abs(hour_angle - minute_angle)
# Return the smaller angle of two
# possible angles
angle = min(360 - angle, angle)
return angle
h =int(input('Enter hours: '))
m =int(input('Enter minutes: '))
print('Angle ', calcAngle(h,m))
h= [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
---------------------------------------------------------------------------
NameError Traceback (most recent call last)
Cell In[14], line 17
15 print('h=',h)
16 #print('m=',m)
---> 17 hour_angle = 0.5 * (h * 60 + m)
18 minute_angle = 6 * m
19 # Find the difference between two angles
NameError: name 'm' is not defined
from math import tan, pi
# Polygon Properties
n=int(input('Number of sides of Polygon n:'))
a = float(input("Enter the Length of a Side a: "))
sum_ext=360
ang_ext=360/n
sum_int=180*n-360
ang_int=sum_int/n
n_tri=n-2
n_diag=n*(n-3)/2
area = n * a**2 / (4 * tan(pi/n))
print('%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f %8.2f '%(sum_ext,ang_ext, sum_int,ang_int
Number of sides of Polygon n:5
Enter the Length of a Side a: 6
360.00 72.00 540.00 108.00 3.00 5.00 61.94
from itertools import permutations
#Permutation
n1 = int(input("Enter the value of n1: "))
n2 = int(input("Enter the value of n2: "))

n3 = int(input("Enter the value of n3: "))

perm = permutations([n1, n2, n3])

#perm = permutations([1, 2, 3])

# Print the obtained permutations

n=0

for i in list(perm):

print (i)

n+=1

print (n)

(2, 3, 6)

(2, 6, 3)

(3, 2, 6)

(3, 6, 2)

(6, 2, 3)

(6, 3, 2)

6

from itertools import combinations

# Get all combinations of [1, 2, 3] and length 2

comb = combinations([1, 2, 3], 2)

# Print the obtained combinations

n=0

for i in list(comb):

print (i)

n+=1

print (n)

(1, 2)

(1, 3)

(2, 3)

3

# Combinations with an element-to-itself

from itertools import combinations_with_replacement

# Get all combinations of [1, 2, 3] and length 2

comb = combinations_with_replacement([1, 2, 3], 2)

n=0

for i in list(comb):

print (i)

n+=1

print(n)

(1, 1)

(1, 2)

(1, 3)

(2, 2)

(2, 3)

(3, 3)

6

n = int(input("Enter the number n: "))

value = input("Enter sum_dig or rev_n or arm_strong or strong:")

sum=0
rev=0

factr=1

temp=n

match value:

case "sum_dig":

while n>0:

r =n%10

n=n//10

sum+=r

print('Sum of the digits=',sum)

case "rev_n":

while n>0:

r =n%10

n=n//10

rev=rev*10+r

print('number reverse=',rev)

case "strong":

while n>0:

r =n%10

n=n//10

factr=1

for i in range(1,r+1):

factr=factr*i

sum+=factr

if temp==sum:

print(temp,'is a stong number')

else:

print(temp,'is not a stong number')

case "arm_strong":

k=len(str(n))

while n>0:

r =n%10

n=n//10

sum+=pow(r,k)

if temp==sum:

print(temp,'is an armstong number')

else:

print(temp,'is not an armston number')

153 is an armstong number

def find_ncr(n,r):

result =factorial(n)/(factorial(r)*factorial(n-r))

return result

def find_npr(n,r):

result = factorial(n)/factorial(n-r)

return result

def factorial(n):

fact = 1

for i in range(1,n+1):

fact = fact *i

return fact
print("Enter the values of n and r")

n=int(input("n value:"))

r=int(input("r value: "))

ncr = find_ncr(n, r)

npr = find_npr(n, r)

print("%dC%d = %d\n"%(n, r, ncr))

print("%dP%d = %d"%(n, r, npr))

Enter the values of n and r

5C2 = 10

5P2 = 20

def factorial(n):

fact = 1

for i in range(1,n+1):

fact = fact *i

return fact

print("Enter the value of n and r")

n=int(input("n value:"))

r=int(input("r value: "))

npr = factorial(n)/factorial(n-r)

ncr = factorial(n)/(factorial(r)*factorial(n-r))

print("%dC%d = %d"%(n, r, ncr))

print("%dP%d = %d"%(n, r, npr))

Enter the value of n and r

5C3 = 10

5P3 = 60

# Python Program to Calculate Profit or Loss and percentage

cost_price=float(input("cost_price:"))

selling_price = float(input("selling_price: "))

if(cost_price > selling_price):

loss = cost_price - selling_price

print("Total Loss = ", loss)

loss_perc=loss/cost_price*100

print("Loss Percentage=%.2f "% loss_perc)

elif(cost_price < selling_price):

profit = selling_price-cost_price

print("Total Profit = ",profit)

profit_perc=profit/cost_price*100

print("Profit Percentage=%.2f "% profit_perc)

else:

print("No Profit No Loss!!!")

CP=float(input('Cost Price :'))

p1=float(input('Profit Per on CP for MP = '))

d=float(input('Discount Per='))

MP=CP*(1+p1/100)

SP=MP*(1-d/100)

SP=CP*(1+p1/100)*(1-d/100)

profit=SP-CP

p=100*(SP-CP)/CP

P=profit/CP*100
p=(p1-d-p1*d/100)

print('Cost Price=%.2f\nMarked Price =%.2f\nSelling Price =%.2f\nProfit=%.2f\nProfitPer=

Total Profit = 300.0

Profit Percentage=20.00

Cost Price=1600.00

Marked Price =2240.00

Selling Price =1792.00

Profit=192.00

ProfitPer=12.00

nA=int(input("nA="))

nB=int(input("nB="))

nC=int(input("nC="))

nAintB=int(input("nAintB="))

nBintC=int(input("nBintC="))

nCintA=int(input("nCintA="))

nAiBiC=int(input("nAiBiC="))

nAUBUC=nA+nB+nC-nAintB-nBintC-nCintA+nAiBiC;

print("nAUBUC = ",nAUBUC)

nAUBUC = 134

