STEPS = [{
    "header": "Integer arithmetics",
    "text": """
We already know the following operations which may be applied to numbers:
<code>+</code>, <code>-</code>, <code>*</code> and <code>**</code>. 

The division
<code>/</code> always gives you a float (a floating-point <a href="https://en.wikipedia.org/wiki/Real_numbers">real number</a>, an object of type <code>float</code>).

From high school, you probably remember how to calculate negative powers. 
We want to provide an example if you don't remember: 2<sup>-3</sup> = 1 / ( 2<sup>3</sup> ) = 0.125.
Of course, Python allows you to calculate negative powers just the same way as positive ones: <code>print(2 ** -3)</code>.

The exponentiation <code>**</code> also returns a float when the power is negative.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(17 / 3)  
print(20 / 4)
print(2 ** 4)  
print(2 ** -3) 
''',
},




{
    "header": "Integer division",
    "text": """
There's a special operation for integer division where the remainder is discarded: <code>//</code>.

The operation that yields a remainder of such a division, though, occurs more often and is denoted by <code>%</code>.

Both operations always yield an object of type <code>int</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(17 / 3)  
print(17 // 3)
print(17 % 3)
''',
    'expected_output': """
5.666666666666667
5
2
""",
    "allfine": 'Nothing to be surprised of: 17 = 3 * 5 + 2, so the result of integer division is 5 and the remainder is 2.',
},



{
    "header": "Floating-point numbers",
    "text": """
When we read an integer value, we read a line with <code>input()</code>
and then cast a string to integer using <code>int()</code>.
When we read a floating-point number, we need to cast a string to
float using <code>float()</code>:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
x = float(input())
print(x)
y = float(input())
print(y)
''',
"input_data": '''
1.492
6
'''
,
    'expected_output': """
1.492
6.0
""",
},



{
    "header": "Very big and very small numbers",
    "text": """
You can write floats with very big or very small absolute values using the scientific notation.
Eg., the distance from the Earth to the Sun is 1.496&middot;10<sup>11</sup> meters, or <code>1.496e11</code>
in Python. The mass of one molecule of water is 2.99&middot;10<sup>-23</sup> grams,
or <code>2.99e-23</code> in Python.

""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# It is well-known that life on Earth
# appeared approximately 3.9 billion years ago.
# You can check it on Wikipedia, for example.
# Assign this value in the scientific
# notation to any variable,
# and then print that variable.
''',
    'expected_output': '3900000000.0',
    'hint': 'A billion is 10<sup>9</sup>, so you can print <code>3.9e9</code>',
},




{
    "header": "Round and round",
    "text": """
You can also cast float objects to int objects. Of course, it can be achieved using the <code>int()</code>
function, which simply discards the fractional part (rounding, thus, every number towards 0). 

But, generally, it is much more convenient to use <code>round()</code>,
 which performs that rounding we are used to.

""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(int(1.3))   # gives 1
print(int(1.7))   # gives 1
print(int(-1.3))  # gives -1
print(int(-1.7))  # gives -1

print(round(1.3))   # gives 1
print(round(1.7))   # gives 2
print(round(-1.3))  # gives -1
print(round(-1.7))  # gives -2
''',
    'expected_output': """
1
1
-1
-1
1
2
-1
-2
""",
},





{
    "header": "Floats can confuse you",
    "text": """
Floating-point real numbers can't be represented with exact precision due to hardware limitations.
This can lead to cumbersome effects. <a href="https://docs.python.org/3.6/tutorial/floatingpoint.html">See the official Python docs</a> for the details.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(0.1 + 0.2)  # gives 0.30000000000000004
''',
    'expected_output': '0.30000000000000004',
},




{
    "header": "Math module",
    "text": """
Python has a ton of functions for calculations with floats. Most of them can be
found in the <code>math</code> module.

To use this module, you need to <b>import</b> it first by writing the following instruction
at the beginning of your program:
<pre>import math</pre> 
 
For example, if we want to find the ceiling value for <code>x</code> &mdash; the smallest integer not less than 
<code>x</code> &mdash; we call the corresponding function from the math module: <code>math.ceil(x)</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
import math

x = math.ceil(4.2)
print(x)
print(math.ceil(1 + 3.8))
''',
    'expected_output': """
5
5
""",
},



{
    "header": "More ways to import math",
    "text": """
You may import only one method from the whole module and use it under
its short name. 

Look at the code to see what syntax is used for that.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
from math import ceil
 
x = 7 / 2
y = ceil(x)
print(y)
''',
    'expected_output': '4',
},
 


{
    "header": "Absolute value of a number",
    "text": """
Another function we haven't mentioned yet is <code>abs()</code> (the absolute value of a number, modulus). Just as functions <code>int()</code> and <code>round()</code>, this function is built-in function and doesn't require any imports.

""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(abs(-6))
print(abs(3.81))
print(abs(0))
''',
    'expected_output': """
6
3.81
0
""",
},


{
    "header": "Some functions from math module",
    "text": """
All the functions of any standard Python module are documented on the official Python website.
<a href="http://docs.python.org/3.6/library/math.html">Here's the description for math module</a>.
Arguably most popular functions are:

<code>floor(x)</code> &mdash; returns the largest integer less than or equal to <code>x</code>,

<code>ceil(x)</code> &mdash; returns the smallest integer greater than or equal to <code>x</code>,

<code>sqrt(x)</code> &mdash; returns the square root of <code>x</code>,

<code>log(x)</code> &mdash; returns the natural logarithm of <code>x</code>,

<code>log(x,a)</code> &mdash; returns the logarithm of <code>x</code> to base <code>a</code>,

<code>pi</code> is the mathematical constant pi = 3,1415926..

<code>e</code> &mdash; is the mathematical constant e = 2,71828..

<code>sin(x)</code> returns the sine of <code>x</code> in radians

<code>cos(x)</code> returns the cosine of <code>x</code> in radians

<code>tan(x)</code> returns the tangent function of <code>x</code>

<code>asin(x)</code> returns the arcsine of <code>x</code> in radians
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# remember the rules:
# if you use "import math",
# you must call the desired function like
# math.sqrt(x)
# or
# math.cos(y)

# But if you use "from math import cos"
# this is how you call the function: 
# cos(x)
# Then, if you what to calculate a logarithm,
# you need to write "from math import log"
# and then you may call your logarithm
# with log(y) or log(z,10)
''',
'tasks': [
    {
        "instruction": 'Print the square root of 256.',
        'expected_output': '16.0',
    },
    {
        "instruction": 'Print the floor of pi<sup>e</sup> + e<sup>pi</sup>.',
        'expected_output': '45',
    },
],
    "allfine": "Congratulations! Now you're guru of ints and floats!",
},

]