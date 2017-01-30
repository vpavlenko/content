STEPS = [{
    "header": "The syntax",
    "text": '''
Let's write a program which, given an integer x, prints |x| &mdash; its absolute value.

By definition of absolute value, if x > 0, such program should just print x. Otherwise, it should print -x. Naturally we are about to <em>check</em> if some condition is met. The behaviour is different when it <i>is</i> met and when it is not.

The keywords <code>if</code> and <code>else</code> are used in such situations. Look at the code.

Given -273 as the input data, it outputs 273. Why? Check the tick "step by step" and look at the visualizer. 
''',
    "program": '''
x = int(input())
if x > 0:
    print(x)
else:
    print(-x)
''',
    "input_data": '''
-273''',
    "expected_output": """
273
""",
    "allfine": "",
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",

},


{
    "header": "If and else: what has just happened?",
    "text": '''
Let's discuss what's happening in details.

This program uses the conditional statement <code>if</code>. After the <code>if</code>
we put a condition <code>x&nbsp;&gt;&nbsp;0</code> following by colon.
After that we put a block of instructions which will be executed only if the condition
is true (i.e. evaluates to <code>True</code>). This block may be followed by the word
<code>else</code>, colon and another block of instructions which will be executed only if the condition is false
(i.e. evaluates to <code>False</code>). In the case above, the condition if false, so the if-block is ignored and the else-block
is executed. 
''',
    "program": '''
x = int(input())
if x > 0:
    print(x)
else:
    print(-x)
    ''',
    "input_data": '''
-273''',
    "expected_output": """
273
""",
    "allfine": "",
},





{
    "header": "Carthage must be indented",
    "text": '''
Each block (each set of instructions after colon) should be indented with four spaces.

Python won't understand you if you don't indent your code.

Python also won't understand you if you indent your code in places where it's not expected. So, the code like 
<pre>
print("first line")
    print("second line")
</pre>
would throw the error.
''',
    "program": '''
# This will throw an error
# because of unexpected indentation:
print("first line")
    print("second line")

''',
    "allfine": "",
},




{
    "header": "Carthage must be indented correctly",
    "text": '''
In this program we removed the indentation, and now the code crashes. Please, restore the indentation
to make it correct and runnable again.

''',
    "program": '''
x = int(input())
if x > 0:
    # Put four spaces or press <Tab> in the beginning of this line:
print(x)  
else:
    # And here:
print(-x)  
''',
    "input_data": '''
-273''',
    "expected_output": '''273''',
    "allfine": "",
},



{
    "header": "If and else: theory",
    "text": '''


To sum up, the conditional statement in Python has the following syntax:
<pre>
if <var>condition</var>:
    <span style="color: green;">true-block</span>
    <span style="color: green;">several instructions that are executed</span>
    <span style="color: green;">if the condition evaluates to True</span>
else:
    <span style="color: red;">false-block</span>
    <span style="color: red;">several instructions that are executed</span>
    <span style="color: red;">if the condition evaluates to False</span>
</pre>
''',
    'program': '''
day = input()
if day == 'Monday':
    print('Such a hard day.')
    print('I wish there were no alarm clocks.')
else:
    print('Moderate day.')
    print('Could be worse.')
''', 
    
    'input_data': '''Monday
''',
    "expected_output": '''
Such a hard day.
I wish there were no alarm clocks.
''',
    "allfine": "",
},



{
    "header": "Sometimes you don't need <code>else</code>",
    "text": '''

You can omit the <code>else</code> keyword and the whole false-block if nothing should be
done if the condition is false. Consider the problem of calculating the absolute value of <code>x</code> and look at the code section.

Indeed, the variable <code>x</code> has to be assigned to <code>-x</code> only if <code>x &lt; 0</code>. Otherwise, it has to remain the same and we don't need to handle this case, don't need to do something with it.

The instruction <code>print(x)</code> is executed anyway, because it is not indented,
so it doesn't belong to the true-block.

Indentation is the general way in Python to separate blocks of code. All instructions within the same
block should be indented the same way, i.e. they should have the same number of spaces
at the beginning of the line. It is recommended to use 4 spaces for indentation.

In most of other languages the curly braces <code>{</code> and <code>}</code> are used to form blocks. 
The creators of Python decided to replace <code>{...}</code>-like blocks with indentation.
This is the question of habit, but, to our opinion, indentation makes your code far more readable than keeping an eye on all the curly braces. 

''',
    "program": '''
x = int(input())
if x < 0:
    x = -x
print(x)
''',
    "input_data": '''
-273''',
    "expected_output": '''
273
''',
    "allfine": "",
},



{
    "header": "Nested conditionals",
    "text": '''
Any Python instruction may be put into if-block and else-block, including another conditional
statement. This way we get nested conditions. The blocks of inner conditions are indented
using twice more spaces (eg. 8 spaces). Let's see an example: the program, which, given the coordinates of a point
on the plane, prints its <a href="https://en.wikipedia.org/wiki/Quadrant_(plane_geometry)">quadrant</a>.
''',
    "instructions": 'Click the tick "step by step", click "Run" and enjoy our visualizer to show the execution flow.',
    "program": '''
x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        # x > 0, y > 0
        print("Quadrant I")
    else:
        # x > 0, y <= 0
        print("Quadrant IV")
else:
    if y > 0:
        # x <= 0, y > 0
        print("Quadrant II")
    else:
        # x <= 0, y <= 0
        print("Quadrant III")
''',
    "input_data": '''
2
-3
''',
    "expected_output": '''
Quadrant IV
''',
    "allfine": """See we've given the input "2", "-3". So, x = 2, y = -3. x > 0, so the block after <code>x > 0</code> will be executed. The condition <code>y > 0</code> is false, so the block following after it won't be executed, and the corresponding <code>else</code> block will be executed. In that block, there's the only instruction to print "Quadrant IV".""",
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
},



{
    "header": "Comparison operators",
    "text": '''
Usually the condition after <code>if</code> has one or more of the following operators:

<code>&lt;</code>: less&nbsp;<!-- /@w -->&mdash; the condition is true if left side is less than right side. 

<code>&gt;</code>: greater&nbsp;<!-- /@w -->&mdash; the condition is true if left side is greater than right side. 

<code>&lt;=</code>: less or equal.

<code>&gt;=</code>: greater or equal.

<code>==</code>: equal.

<code>!=</code>: not equal.
</dl>

For example, the condition <code>x&nbsp;*&nbsp;x&nbsp;&lt;&nbsp;1000</code>
means &ldquo;the value of the expression <code>x&nbsp;*&nbsp;x</code> is less than 1000&rdquo;,
and the condition <code>2&nbsp;*&nbsp;x&nbsp;!=&nbsp;y</code> means &ldquo;the doubled value
of the variable <code>x</code> is not equal to the value of the variable <code>y</code>&rdquo;.

The comparison operators in Python may be chained like this: <nobr><code>a == b == c</code></nobr> or <nobr><code>x &lt;= y &gt;= 10</code></nobr>. It's a rare thing among programming languages.
''', 'program': '''
x = 10
y = 20
if 2 * x != y:
    print("x and y don't make 1:2 ratio")
else:
    print("x and y make 1:2 ratio")
''',
    "expected_output": '''
x and y make 1:2 ratio
''',
},



{
    "header": "The difference between = and ==",
    "text": '''
There's the common mistake young programmers make: writing your <code>if</code> condition, when you're about to check if a = b, you <b>should NOT</b> type <code>if&nbsp;a&nbsp;=&nbsp;b</code>. The reason is, in programming languages <code>=</code> is the assigment operator: <code>a&nbsp;=&nbsp;5</code>, <code>name&nbsp;=&nbsp;'Matilda'</code>. The operator <code>=</code> <em>assigns</em> a value (say, 5) to a variable (say, <code>a</code>).

Instead, <b>you type</b> <code>if&nbsp;a&nbsp;==&nbsp;b</code>. The operator <code>==</code> (two <code>=</code> signs) is the equality checking operator.
''', 
'program': '''
year = 2016
if year % 4 == 0:
    print("Well, it's probably leap year now")
else:
    print("This year is definitely not leap one")
''',
    "expected_output": '''
Well, it's probably leap year now
''',
},



{
    "header": "True and false",
    "text": '''
<p>When you do a comparison, it can be true and false. Look at the code section. 

<p>You probably agree that "2 < 5" is true and "2 > 5" is false. You probably also agree that it's false that 7 <= -1 and it's true that 6 >= 6.

We've also talked a bit about <code>==</code>. But what is <code>!=</code>? What does that operator mean?

Fortunately that's easy enough to remember. <code>==</code> stands for "is equal to", and <code>!=</code> means "is not equal to". As simple as that.

Now you can ensure that 8 != 4 and 2 == 2, and that propositions "5 == 8" and "73 != 73" are not true.
''',
    "program": '''
print(2 < 5)    # will print "True"
print(2 > 5)    # will print "False"
print(7 <= -1)  # will print "False"
print(6 >= 6)   # will print "True"
print(5 == 8)   # will print "False"
print(8 != 4)   # will print "True"
print(73 != 73) # will print "False"
print(2 == 2)   # will print "True"
''',
    "expected_output": '''
True
False
False
True
False
True
False
True
''',
},



{
    "header": "Boolean objects, boolean type",
    "text": '''
As our clever Wikipedia <a href="https://en.wikipedia.org/wiki/Boolean">tells us</a>, a Boolean data type is a data type with only two possible values: true or false.

So if variable <code>a</code> is boolean, it can have only two values, and those values are <code>True</code> and <code>False</code>. 

There's the peculiarity. Actually you can assign numbers to such variable: <code>a&nbsp;=&nbsp;0</code> or <code>a&nbsp;=&nbsp;1</code>. This is because Python treats <code>0</code> as <code>False</code> and treats <code>1</code> as <code>True</code>. Moreover, Python treats empty string (the string '') as <code>False</code>, and every another string in this true/false sense is <code>True</code>.

As <code>int()</code> tries to convert input data to integer, you can use <code>bool()</code> to cast input data to true or false. Look at the code section.
''',
    "program": '''
print(bool(-10))    # True
print(bool(0))      # False - zero is the only false number
print(bool(10))     # True

print(bool(''))     # False - empty string is the only false string
print(bool('abc'))  # True
''',

    "expected_output": '''
True
False
True
False
True
''',
},



{
    "header": "The magic of logic",
    "text": '''
Sometimes you need to check several conditions at once.
For example, you can check if a number <code>n</code> is even using the condition
<code>n&nbsp;%&nbsp;2&nbsp;==&nbsp;0</code>
(<code>n</code> gives a remainder <code>0</code> when dividing by <code>2</code>).

If you need to check that two numbers <code>n</code> and <code>m</code> are both even, 
you should check both <code>n&nbsp;%&nbsp;2&nbsp;==&nbsp;0</code>
and <code>m&nbsp;%&nbsp;2&nbsp;==&nbsp;0</code>.
To do that, you join them using an operator <code>and</code>
(logical AND): <code>n&nbsp;%&nbsp;2&nbsp;==&nbsp;0&nbsp;and&nbsp;m&nbsp;%&nbsp;2&nbsp;==&nbsp;0</code>.

''',
    "program": '''
n = int(input())
m = int(input())

if n % 2 == 0 and m % 2 == 0:
    print("Hooray!")
else:
    print("X-ray")
''',
    "input_data": '''
58
12
''',
    "expected_output": '''
Hooray!
''',
},



{
    "header": "AND, OR and negation",
    "text": '''
Python has logical AND, logical OR and negation.

Operator <code>and</code> is the <a href="https://en.wikipedia.org/wiki/Binary_operation">binary</a> operator which evaluates to <code>True</code>
if and only if both its left-hand side and right-hand side are <code>True</code>.

Operator <code>or</code> is the binary operator which evaluates to <code>True</code>
if at least one of its sides is <code>True</code>.

Operator <code>not</code> is the <a href="https://en.wikipedia.org/wiki/Unary_operation">unary</a> negation.
It's evaluated to <code>True</code> if the input value is <code>False</code>, and, vice versa, it evaluates to <code>false</code> if the input value is <code>true</code>.

Look at this program. It checks if at least one of the two numbers ends by 0:
''',
    "program": '''
a = int(input())
b = int(input())
if a % 10 == 0 or b % 10 == 0:
    print('YES')
else:
    print('NO')
''',
    "input_data": '''
15
40
''',
    "expected_output": '''
YES
''',
},



{
    "header": "Examples, examples",
    "text": '''
Let's check that the number <code>a</code> is positive and 
the number <code>b</code> is non-negative:

<pre>if a &gt; 0 and not (b &lt; 0):
</pre>

Instead of <code> not (b&nbsp;&lt;&nbsp;0)</code> we can write <code>(b&nbsp;&gt;=&nbsp;0)</code>.
''',
    "program": '''
a = int(input())
b = int(input())
if a > 0 and b >= 0:
# another suitable expression is
# if a > 0 and not b < 0:
    print('YES')
else:
    print('NO')
''',
    "input_data": '''
5
0
''',
    "expected_output": '''
YES
''',
},



{
    "header": "Elif",
    "text": '''
If you have more than two options using the conditional operator, you can use 
<code>if... elif... else</code> statement.

Look at the code section to see how it works. As you see, we just rewrote the quadrants code from above.

In this case the conditions in <code>if</code> and <code>elif</code>s are checked one after another until
the first true condition is found. Then only the true-block for that condition is being executed. If all the 
conditions are false, the else-block is being executed, if you've written it.
''',
    "program": '''
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Quadrant I")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif y > 0:
    print("Quadrant II")
else:
    print("Quadrant III")
''',
    "input_data": '''
-5
7
''',    "expected_output": '''
Quadrant II
''',

}

]