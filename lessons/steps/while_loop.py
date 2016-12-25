STEPS = [{
    "header": "While loop",
    "text": """
<code>while</code> loop repeats
the block of statements many times while some condition evaluates to <code>True</code>. When the condition is evaluated to <code>False</code>, the block of statements is executed no more, and while loop is ended.
The condition is given before the loop body (before the block of statements) and is checked before each execution of the loop body.
Typically, the <code>while</code> loop is used when it is impossible or inconvenient
to determine the exact number of loop iterations in advance.

Primarily, Python checks the condition.
If it is False, the loop is terminated and the program performs instructions that go after the <code>while</code> loop.

If the condition is True, the loop body is executed, and then the condition is checked again. This continues while the condition is True.

Once the condition becomes False, the loop terminates and the program performs instructions that go after the <code>while</code> loop.
""",
    "program": '''
# while some condition:
#     a block of statements

i = 1
while i <= 5:
    print(i)
    i += 1
''',
},



{
    "header": "While loop: an example",
    "text": """
The following program prints
squares of all integers from 1 to 10. (Here you can replace the <code>while</code> loop by the 
<code>for ... in range(...)</code> loop.)

<p>In this example, the variable <code>i</code> inside the loop iterates from 1 to 10.
Such a variable whose value changes with each new loop iteration
is called a counter. Note that after executing this fragment
the value of the variable <code>i</code> is defined and is equal to <code>11</code>,
because when <code>i == 11</code> the condition <code>i &lt;= 10</code> is False for the first time.
""",
    "program": '''
i = 1
while i <= 10:
    print(i ** 2)
    i += 1
''',
'tasks': [ 
    {
        "instruction": 'Run the code.',
        'expected_output': """
1
4
9
16
25
36
49
64
81
100
""",
    },
    {
        "instruction": "Print the cubes of all integers from -10 to 10, including both ends.",
        'expected_output': """
-1000
-729
-512
-343
-216
-125
-64
-27
-8
-1
0
1
8
27
64
125
216
343
512
729
1000
        """,
    },

],
},




{
    "header": "While loop: another example",
    "text": """
Here's another use case of the <code>while</code> loop
to determine the number of digits of an integer <code>n</code>.

On each iteration we cut the last digit of the number
using integer division by 10 (<code>n //= 10</code>). In the variable 
<code>length</code> we count how many times we did that.
""",
    "instructions": 'Run the code.',
    "program": '''
n = int(input())
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)  # 7
''',
"input_data": '''
5678973
'''
,
    'expected_output': '7',
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
    "allfine": 'In Python there is another, easier way to solve this problem: <code><nobr>length = len(str(i))</nobr></code>.',
},


{
    "header": "Loop control flow: else",
    "text": """
You can write an <code>else:</code> statement after a loop body which is executed
<i>once</i> after the end of the loop.

At the first glance, this statement doesn't seem to have sense, because the <code>else:</code> statement
body can just be put <i>after</i> the end of the loop. "else" statement after a loop only has sense when used
in combination with the instruction <code>break</code>. If during the execution of the loop Python encounters
<code>break</code>, it immediately stops the loop execution and exits out of it.
In this case, the <code>else:</code> branch is not executed. So, <code>break</code> is used to abort the loop execution during
the middle of any iteration.
""",
    "instructions": 'Run the code.',
    "program": '''
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)
''',
    'expected_output': """
1
2
3
4
5
6
7
8
9
10
Loop ended, i = 11
""",
},


{
    "header": "Black Jack and else",
    "text": """
Here is a Black Jack-like example: a program that reads numbers and sums them
until the total gets greater or equal to 21. The input sequence ends with 0
for the program to be able to stop even if the total sum of all numbers is less than 21.

Let's see how it behaves on the different inputs.
""",
    "program": '''
total_sum = 0
a = int(input())
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')
''',
    'tasks': [
    {
        "instruction": 'Enter the strings "2", "4", "7", "0" to the input section, then run the program.',
        'expected_output': 'Total sum is less than 21 and is equal to 13 .',
    },
    {
        "instruction": 'Enter the strings "9", "9", "5", "4", "0" to the input section, then run the program.',
        'expected_output': 'Total sum is 23',
    },
],
    'input_data': '''2
4
7
0''',
    "allfine": 'In the first case, the loop is exited normally after checking the condition, so the "else" branch is executed.<br><br> In the second case, the loop is aborted by <code>break</code>, so the "else" branch is skipped.',
},


{
    "header": "Else after for",
    "text": """
"Else" branch can also be used with the "for" loop. Let's look at the example when a program reads exactly five integers
but stops right when the first negative integer is met.
""",
    "program": '''
for i in range(5):
    a = int(input())
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')
''',
    'tasks': [
    {
        "instruction": 'Enter the strings "3", "6", "2", "4", "5" to the input section, then run the program.',
        'expected_output': 'No negative numbers met',
    },
    {
        "instruction": 'Enter the strings "3", "6", "-2", "4", "5" to the input section, then run the program.',
        'expected_output': 'Met a negative number -2',
    },
],
    'input_data': '''3
6
2
4
5''',
    "allfine": "In the first case, the loop is exited normally, so the <code>else</code> branch is executed. <br><br> In the second case, the loop is aborted, so the <code>else</code> branch isn't executed.",
},



{
    "header": "Continue",
    "text": """
Another instruction used to control the loop execution is
<code>continue</code>. If Python meets <code>continue</code> somewhere in the middle of the loop iteration,
it skips all the remaining instructions and proceeds to the next iteration.
""",
    "instructions": 'Run the code.',
    "program": '''
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
''',
    'expected_output': """
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
""",
},


{
    "header": "Break and continue exit only the innermost loop",
    "text": """
If the <code>break</code> and <code>continue</code> are placed inside several nested
loops, they affect only the execution of the innermost one. Have a look at rather silly example
to demonstrate it.
""",
    "instructions": 'Run the code.',
    "program": '''
for i in range(3):
    for j in range(5):
        if j > i:
            # breaks only the for on line 2
            break
        print(i, j)
''',
    'expected_output': """
0 0
1 0
1 1
2 0
2 1
2 2
""",
},


{
    "header": "Avoid using break and continue",
    "text": """
If the <code>break</code> and <code>continue</code> are placed inside several nested
loops, they affect only the execution of the innermost one. Have a look at rather silly example
to demonstrate it.
""",
    "program": '''
n = int(input())
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Length is', length)

# It's cleaner and easier-to-read 
# to rewrite this loop with a meaningful loop condition:

n = int(input())
length = 0
while n != 0:
    length += 1
    n //= 10
print('Length is', length)
''',
"input_data": '''
567
567
'''
,
    'expected_output': """
Length is 3
Length is 3
""",
    "allfine": "The instructions <code>break</code> and <code>continue</code> are discouraged, if you can implement your idea without them. Here is a typical example of <i>bad usage</i> of the <code>break</code> in the code that counts the number of digits in an integer.",
},



{
    "header": "Multiple assignment",
    "text": """
In Python it is possible for a single assignment statement to change the value of several variables (see the code section).
""",
    "instructions": 'Run an example.',
    "program": '''
a, b = 0, 1

# The above code does the same as the below code:

a = 0
b = 1

# The difference between the two versions is that
# multiple assignment changes the values of two
# variables simultaneously. It is crucial in terms
# of code readability sometimes.
''',
},


{
    "header": "When multiple assignment saves the party",
    "text": """
In Python it is possible for a single assignment statement to change the value of several variables (see the code section).
""",
    "instructions": 'Note the line <code>previous, current = current, previous + current</code>. Run the code.',
    "program": '''
def fibonacci(n):
    previous = 1
    current = 1
    for i in range(n):
        previous, current = current, previous + current
    return current

print(fibonacci(6))
''',
    'expected_output': '21',
    "allfine": """You've successfully printed the 6-th <a href="https://en.wikipedia.org/wiki/Fibonacci_number">Fibonacci number</a>.""",
},



{
    "header": "In older languages",
    "text": """
The left-hand side of "=" should have a comma-separated list of variable names.
The right-hand side can be any expressions
separated by commas. The left-hand side and the right-hand side lists should be of equal length.
""",
    "instructions": 'Run the code.',
    "program": '''
# Multiple assignment is useful when you need
# to exchange the values of two variables.
# In older programming languages
# this can be done using an auxiliary variable:

a = 1
b = 2
tmp = a
a = b
b = tmp
print(a, b) # will print '2 1'

# In Python, the same swap can be written in one line:

a = 1
b = 2
a, b = b, a
print(a, b)
''',
    'expected_output': """
2 1
2 1
""",
    "allfine": "Congratulations! You've passed the while level!",
},

]
