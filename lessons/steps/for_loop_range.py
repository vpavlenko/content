STEPS = [{
    "header": "Loops? Why do I need them?",
    "text": """
Quite often programs need to repeat some block several times. That's where 
loops come in handy. To sum first <code>5</code> numbers, for sure you
 can write something like what you see in the code section.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
sum = 0
sum = sum + 1
sum = sum + 2
sum = sum + 3
sum = sum + 4
sum = sum + 5
print(sum)
''',
    'expected_output': '15',
    "allfine": "But it is inconvenient. Imagine you had to sum the first 100 numbers, or do another bunch of similar calculations. You surely wouldn't write the 100 lines!",
},



{
    "header": "The loop called <em>for</em>",
    "text": """
If you have to do fixed amount of operations &mdash; say, sum the 100 first numbers &mdash; the <code>for</code> loop saves the day.

There are <code>for</code> and <code>while</code> loop operators in Python, in this lesson we cover <code>for</code>.

<p><code>for</code> loop iterates over any sequence.
Let's see the simplest example of using <code>for</code>. 
Same as with if-else, <em>indentation</em> is what specifies 
which instructions are controlled by <code>for</code> and which aren't.

""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, 'color of rainbow is', color)
    i = i + 1
''',
    'expected_output': """
# 1 color of rainbow is red
# 2 color of rainbow is orange
# 3 color of rainbow is yellow
# 4 color of rainbow is green
# 5 color of rainbow is cyan
# 6 color of rainbow is blue
# 7 color of rainbow is violet
""",
    "allfine": """I solemnly congratulate you with the first <code>for</code> loop in your life!

    In this example the variable <code>color</code> iterates over the values <code>'red'</code>,
<code>'orange'</code> etc, and for each value the underlying loop block is executed. Loop block contains two
operators: call of the function <code>print()</code> that prints new data and assignment operator
that increases the value of the variable <code>i</code> by one.""",
},




{
    "header": "You may iterate over different types",
    "text": """
Loop variable can iterate over the objects of different types.
In the next example the variable <code>i</code> is pointing to <code>int</code> object for the
first three iterations and to <code>str</code> object for the last three iterations:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for i in 1, 2, 3, 'one', 'two', 'three':
    print(i)
''',
    'expected_output': """
1
2
3
one
two
three
""",
    "allfine": "In all these examples sequences like <code>'red', 'orange', 'yellow'</code> are actually a compound Python object. It has a type <code>tuple</code> which we'll dig into more in the next levels.",
},




{
    "header": "You may iterate over characters of a string",
    "text": """
<code>for</code> loop iterates over <i>any</i> sequence. Any string in Python is the sequence of
its characters, so we can iterate over them using <code>for</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for character in 'hello':
    print(character)
''',
    'expected_output': """
h
e
l
l
o
""",
},



{
    "header": "Range: starting with the example",
    "text": """
Another use case is to iterate over some integer variable in increasing or decreasing order.
Such a sequence of integers can be created using the function <code>range(min_value, max_value)</code>:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for i in range(5, 8):
    print(i, i ** 2)
print('end of loop')
''',
    'expected_output': """
5 25
6 36
7 49
end of loop
""",
    "allfine": 'And now we wish to explain how does <code>range()</code> work in details. Press "Continue" for that.',
},


{
    "header": "Range: how does it work?",
    "text": """
Function <code>range(min_value, max_value)</code> generates the sequence of numbers
<code>min_value</code>, <code>min_value + 1</code>, ..., <code>max_value - 1</code>. 

We'd like to stress: the number <code>max_value</code> is <i>not</i>
included.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for i in range(4,8):
    print(i)
# This will print 4, 5, 6 and 7
''',
    'expected_output': """
4
5
6
7
""",
},



{
    "header": "Range: calling with one argument",
    "text": """
There's the reduced form of range() &mdash; <code>range(max_value)</code>. That is exactly the same as <code>range(0, max_value)</code>, i.e. 
<code>range(max_value)</code> generates the sequence of numbers
<code>0</code>, <code>1</code>, <code>2</code>, ..., <code>max_value - 1</code>. 
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for i in range(5):
    print(i)
''',
    'expected_output': """
0
1
2
3
4
""",
    "allfine": "",
},



{
    "header": "Don't create empty ranges",
    "text": """
If you pass an empty sequence to <code>range()</code>, like <code>range(-5)</code> or <code>range(7, 3)</code>, the for-block won't be executed.

Generally, you're not interested in creating empty ranges.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for i in range(-5):
    print("This won't be printed")
for k in range(8, 6):
    print('Nothing will be printed')
''',
    'expected_output': '',
    "allfine": "",
},



{
    "header": "How do you finally sum up integers?",
    "text": """
Let's finally learn how to sum the integers from 1 to <code>n</code> inclusively.

Remember: the maximum value in <code>range(min_value, max_value)</code> is <b>not</b> included! To make <code>i</code> running from 1 to <code>n</code> inclusively, the maximum value in <code>range()</code> should be <code>n + 1</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the shorthand for
    # result = result + i
print(result)
''',
    'expected_output': '15',
    "allfine": "",
},


{
    "header": "When *= doesn't mean a kiss",
    "text": """
In the previous program, we've written <code>result += i</code> instead of <code>result = result + i</code>. The operators <code>+=</code>, <code>-=</code>, <code>*=</code>, <code>/=</code> are common shortcuts; see the code section.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
result = 0
debt = 1000
prod = 1
divine = 100
n = 5
for i in range(1, n + 1):
    result += i   # the same as result = result + i
    debt -= i     # the same as debt = debt - i
    prod *= i     # the same as prod = prod * i
    divine /= i     # the same as divine = divine / i
print(result)
print(debt)
print(prod)
print(divine)
''',
    'expected_output': """
15
985
120
0.8333333333333334
""",
    "allfine": "And the line <code>count += 1</code> is arguably the most widespread line in coding. Go to the next step! :)",
},



{
    "header": "Step can be negative",
    "text": """
To iterate over a decreasing sequence, we can use the extended form of <code>range()</code> with three
arguments &mdash; <code>range(start_value, end_value, step)</code>. When omitted, the step is implicitly
equal to 1. However, it can be any non-zero value. The loop always includes <code>start_value</code> and excludes <code>end_value</code>
during iteration:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
for i in range(10, 0, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2
''',
    'expected_output': """
10
8
6
4
2
""",
    "allfine": "",
},



{
    "header": "Formatted output: print() like a smart kid",
    "text": """
By default, the <code>print()</code> function prints all its arguments separating them by a space, and, after printing all the arguments, it puts
the newline symbol. This behavior can be changed using keyword arguments <code>sep</code> (separator) and <code>end</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=', ', end='. ')
print(4, 5, 6, sep=', ', end='. ')
print()
print(1, 2, 3, sep='', end=' -- ')
print(4, 5, 6, sep=' * ', end='.')
''',
    'expected_output': """
1 2 3
4 5 6
1, 2, 3. 4, 5, 6. 
123 -- 4 * 5 * 6.
""",
    "allfine": "Congratulations! Now you briefly know how to use <code>for</code> in Python. Prove it by solving problems :)",
},


]

