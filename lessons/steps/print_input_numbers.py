STEPS = [{
    "header": "It's all about the data",
    "text": """Every program deals with data. It can take some data for input, and it can output something.
So we should know how to input data into it and how to output.

There's the function <code>print()</code> to output data from a Python program.""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(5 + 10)
''',
    'expected_output': '15',
    "allfine": 'Right, it prints 15! As easy as that!',
},



 {
    "header": """Your own. Personal. Calculator.""",
    "text": """
Of course you can perform any other mathematical operations!
""",
    "program": '''
# Your code here!
''',
    'tasks': [
    {
        "instruction": 'Type in the program window: <code>print(7 - 3)</code> and press "Run"',
        'expected_output': '4',
    },
    {
        "instruction": 'Then type <code>print(4 * 5)</code> and press "Run"',
        'expected_output': '20',
    },
    {
        "instruction": 'Then type <code>print(5 / 3)</code> and press "Run"',
        'expected_output': '1.6666666666666667',
    },
],
    "allfine": '''
Now you can use Snakify as your personal calculator.
'''},



 {
    "header": """Reach out and touch faith.""",
    "text": """
We are excited to show you some more mathematical operations. In Python, you can easily calculate the value of some number <em>in a power</em> of another number. How to calculate 2<sup>16</sup>? Just type in: <code>print(2 ** 16)</code>

""",
    "program": '''
# You are cordially invited 
# to write code in this window
# below these words.
''',
    "instructions": '''
Type in: <code>print(2 ** 16)</code> and press "Run".
''',
    'allfine': '''
As you see, two stars <code>**</code> are used for exponentiation.
''', 
    'expected_output': '65536',
},



 {
    "header": """Weird arithmetic comes in""",
    "text": """

Moreover, you can perform integer division and division with remainder. If you are interested in result of division, you print <code>print(37 // 3)</code>. If you are interested in remainder, you print <code>print(37 % 3)</code>.

""",
    "tasks": [{
        'instruction': 'Type in the program window: <code>print(37 // 3)</code> and press "Run".',
        'expected_output': '12',
    }, {
        'instruction': 'Then type <code>print(37 % 3)</code> and press "Run".',
        'expected_output': '1',
    }, ],
    "allfine": '''
So, <code>//</code> sign is integer division; <code>%</code> returns you the remainder of the left value divided by the right value. <code>37 = 12 * 3 + 1</code>, and this is why <code>37 // 3 = 12</code> and <code>37 % 3 = 1</code>.
'''},



 {
    "header": """print(a, b, c)""",
    "text": """
You may print any number of values on one line.

""",
    "instructions": '''
Just type <code>print(3*7, (17 - 2) * 8)</code> to ensure.
''',
    'expected_output': '21 120',
    "allfine": '''
Brilliant! Let's move on.
'''},



 {
    "header": """Come together! Right now...""",
    "text": """
Now carnival ends, and they come to the scene all together:
""",
    'program': '''
print(5 + 10)
print(7 - 3)
print(4 * 5)
print(5 / 3)
print(2 ** 16)  # two stars are used for exponentiation
print(37 / 3)  # single forward slash is a division
print(37 // 3)  # double forward slash is an integer division
print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder
print(3 * 7, (17 - 2) * 8)
''',
    "expected_output": """
15
4
20
1.6666666666666667
65536
12.333333333333334
12
1
21 120
""",


},



 {
    "header": """...over me!""",
    "text": """
Note that you are allowed
<ul>
  <li>to make spaces between the lines</li>
  <li>to make spaces inside any line:</li>
</ul>


 :
""",
    'program': '''
print(5 + 10)
print(7 - 3      )
print(4*     5)

print(5 / 3)
print(2 ** 16)  # two stars are used for exponentiation

print(37  / 3)  # single forward slash is a division



print(37 // 3)
print           (37 % 3)
print(  3  * 7, (  17 - 2) *   8)
''',
    "expected_output": """
15
4
20
1.6666666666666667
65536
12.333333333333334
12
1
21 120
""",
    "allfine": "However, this сan make your code messy. Keep the code easy-to-read for you and for your colleagues. :)"

},



 {
    "header": """Your marvellous comments""",
    "text": """
See the English phrases after the sign <code>#</code>? They don't look like the other code. They are just text, they are remarks.

They are called comments. A <em>comment</em> is text. You write comments to clarify what happens in the code. If Python sees the sign <code>#</code>, it ignores the rest of the line and starts reading the next line, so feel free to swear after the sign <code>#</code>.

In another words, comments are explanatory text that has no effect on program execution.
This text starts with <code>#</code> and lasts till the end of the line.

""",
    'program': '''
# This program prints ton of numbers.

print(5 + 10)
print(7 - 3)
print(4 * 5)
print(5 / 3)
print(2 ** 16)  # two stars are used for exponentiation
print(37 / 3)  # single forward slash is a division
print(37 // 3)
print(37 % 3)
print(3 * 7, (17 - 2) * 8)
''',
    "expected_output": """
15
4
20
1.6666666666666667
65536
12.333333333333334
12
1
21 120
""",

},



 {
    "header": """Say what you think of Scott and Mary""",
    "text": """
""",
    'program': '''
print("Scott + Mary = peace, love and death metal")
''',
    "instructions": '''
Try to write your own comment about Scott and Mary. Then press "Run".

Remember that comments start with <code>#</code>.
''',
    "allfine": '''
Brilliant! Let's move on.
''',
    "expected_output": """
Scott + Mary = peace, love and death metal
""",
    "checker": "return code.indexOf('#') != -1;",
},



 {
    "header": """Step by step""",
    "text": """
You've already seen this code, but you haven't seen the might of our visualizer yet. To do it, set the tick "step by step" on and then click "Run":

""",
    'program': '''
print(5 + 10)
print(7 - 3)
print(4 * 5)
print(5 / 3)
print(2 ** 16)  # two stars are used for exponentiation
print(37 / 3)  # single forward slash is a division
print(37 // 3)
print(37 % 3)
print(3 * 7, (17 - 2) * 8)
''',
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
    'allfine':
'''Impressed? You shall always execute programs line by line when you need to keep track of all the variables. Professional coders call it <em>debugging</em>.''',
},



 {
    "header": """The Oscar goes to you""",
    "text": """
""",
    "instructions": '''
Now print the remainder of the division of 41 by 7.
''',
    "expected_output": "6",
},



 {
    "header": """The task, it goes to you""",
    "text": """
""",
    "instructions": '''
Now print 3<sup>5</sup>.
''',
    "expected_output": "243",
},



 {
    "header": """The task for Elon Musk""",
    "text": """
""",
    "instructions": '''
Now print <code>5 % (101 % 3)</code> and <code>(76 // 3) * 4</code> on one line.
''',
    "expected_output": "1 100",
},



 {
    "header": """Know how to input""",
    "text": """
So far, this section was empty in our programs.

But getting a serious programmer, you will want to make some of your programs universal: each time you launch them, you will want to pass different data to input. (Generally, that means you will get different data at output.) 

To read your data from input, the function <code>input()</code> exists.
""",
    "input_data": "Here goes the input of our programs",
        'program': '''
print(input())
''',
    "expected_output": "Here goes the input of our programs",
    "highlight": "$('.visualizer_stdin_wrapper').addClass('snakify-blinking');",
},



 {
    "header": """What you input is always a string""",
    "text": """
    The function <code>input()</code> reads your input as a string. Even if you typed 23.
""",
    'program': '''
print(input())
''',
    "input_data": "23",
    "expected_output": "23",
},



 {
    "header": """Variables""",
    "text": """
Writing a complex program, you usually can't print the answer of your calculation right away. You use <em>variables</em> to keep intermediate results there.

Look at the code section. On the left to assignment operator side we put a name of variable (in this case, <code>a</code>). The name could be a string of latin characters mixed with numbers, but should not start with a number. So, <code>much3q1</code> is valid name for variable, and <code>2pac</code> is not.

On the right side to assignment operator we put any expression that Python can evaluate. It can be <code>3</code> as in the code, or it can be, say, <code>1 + (2 ** 8) % 5</code>.

The assignment operator is <code>=</code>.

Look what we've done: we assigned to the variable <code>a</code> the value of <code>3</code>. All right, now 
""",
    "program": '''
a = 3
print(a)
''',
'tasks': [
    {
        "instruction": 'Change the second line to <code>print(a * a)</code>, run the program and see what happens.',
        'expected_output': '9',
    },
    {
        "instruction": 'Erase the line <code>print(a * a)</code>. Type <code>b = a * a</code>, type <code>print(b)</code> on the next line, then run the code and see what happens.',
        'expected_output': '9',
    },
],

},



 {
    "header": """The more variables the better""",
    "text": """
Never hesitate introducing different variables! The more variables you introduce, the more readable your code would be.
""",
    'program': '''
# Compare this:
print( ( 2**10 - 3.7 ) / ( 95/6 + 8)  )

# to this:

numerator = 2**10 - 3.7
denominator = 95/6 + 8

N = numerator/denominator

print(N)
''',
    'expected_output': '42.8097902097902',
    'allfine':
'''Breaking your complex expressions to variables makes your code far more readable and prevents you from silly mistakes.'''
},



 {
    "header": """Greet yourself""",
    "text": """
Here's a program that reads the user's name and greets him.
""",
    'program': '''
print('What is your name?')
name = input()  # read a single line and store it in the variable "name"
print('Hi ' + name + '!')
    ''',
    'input_data': '''
John
''',
    "instructions": '''
Write your own name to the input section! Let it greet you!
''',
    "checker": "return stdin != 'John';",
    'expected_output': 'Hi John!',
},



 {
    "header": """The very start: summing two numbers""",
    "text": """
Let's try to write a program that has two numbers as an input and prints their sum.

We read the two numbers and store them in the variables <code>a</code> and <code>b</code>.

""",
    "instructions": '''
Read the code, run it and look at its output:
''',
    'program': '''
a = input()
b = input()
s = a + b
print(s)
    ''',
    'input_data': '''
5
7
''',
    'expected_output': '57',
},



 {
    "header": """Oops: you summed strings, not numbers""",
    "text": """
After running the example we can see that it prints <code>57</code>. As we were taught in school,
<code>5&nbsp;+&nbsp;7</code> gives <code>12</code>. What happened?

So, the program works badly, and it is important to understand why.

The reason is, in the line <code>s&nbsp;=&nbsp;a&nbsp;+&nbsp;b</code> Python has <i>summed</i> two strings, rather than two numbers.
The sum of two strings in Python works as follows: they are just glued one after another. It's also sometimes
called <em>string concatenation</em>.

""",
    "program": '''
a = input()
b = input()
s = a + b
print(s)
''',
    "input_data": '''
5
7
''',
    "instructions": '''
Use two another numbers as inputs (modifying the input section), and then watch they are glued to each other, not summed :(
'''},



 {
    "header": """What are strings and what are numbers""",
    "text": """

Look at the code side. Do you see that the values bound to variables <code>s</code> and <code>que</code>
are wrapped in quotes?

That means these values are strings, not numbers. Strings and numbers
are represented in Python differently.

(It doesn't matter what quotation marks will you use to define a string: these <code>'&nbsp;'</code> or these <code>"&nbsp;"</code>.)

""",
    'program': '''
num = 14       # This is the number
s = 'hadoop'   # This is the string
que = "wroom"   # This is also a string
print (s + que)

# 'hadoop' and "wroom" have different
# quotation marks, but Python has no problem
# with it,
# and the output is
# 'hadoopwroom'
''',
    'expected_output': 'hadoopwroom',

},



 {
    "header": """I can't multiply strings :(""",
    "text": """
All the values in Python are called <em>objects</em>. Every object has a certain type. The number 2 corresponds to an object "2" of type "int"
(i.e., an integer number).

The string <code>'hello'</code> corresponds to an object "hello" of type "str".

Every <a href="https://en.wikipedia.org/wiki/Real_number">real number</a> can be represented as an object of type "float".

The type of an object specifies what kind of operations may be applied to it.
For instance, if the two variables <code>"first"</code> and <code>"second"</code> are pointing to the objects of type <code>int</code>, Python can multiply them. However, Python can't multiply strings.
""",
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
    'program': '''
first = 5
second = 7
print(first * second)

# you can use single or double quotes to define a string
first = '5'
second = "7"
print(first * second)
    ''',

    "expected_output": """
35
TypeError: can't multiply sequence by non-int of type 'str'
""",

        'allfine':
'''The first three lines of code here successfully gave us the result of multiplication, and the last three lines granted us with the error.'''

},



 {
    "header": """Transformers: transforming strings to integers""",
    "text": """
<p>
To cast the string of digits into an integer number, we can use the function <code>int()</code>. Eg., <code>int('23')</code> transforms the string '23' into the number <code>23</code>.
</p>

""",
"instructions": "Read the number from input, then transform it to integer using <code>int()</code>.",
    'input_data': '''
364
''',    "expected_output": """
364
""",
},



 {
    "header": """Summing numbers, not strings""",
    "text": """
Using the magic of <code>int()</code>, we can now fix our incorrent program to sum the two numbers:
""",
    'program': '''
a = int(input())
# the function input() reads the first string, then int() casts it into the integer 5 
b = int(input())
# reads the first string, then casts it into the integer 7
s = a + b
print(s)
    ''',
    'input_data': '''
5
7
''',
    "expected_output": """
12
""",
    "allfine": "This is when we're rewarded for watching the types! 5+7 resulted in <code>12</code>! Hooray!<br><br>Congratulations. This is the end of the first level. You've passed it. Now try to solve some problems!",
}
]
