STEPS = [{
    "header": "Lists: why do we need them",
    "text": """Most of programs work not only with variables. They also use lists of variables.
A program can handle an information about students by reading the list of
students from the keyboard or from a file. A change in the number of students in a class
must <b>not</b> require modification of the program source code.

We have already faced the task of processing elements of a sequence &mdash;
for example, when finding the largest element of the sequence. But 
we haven't kept the whole sequence in computer's memory. However, 
in many situations it is necessary to keep the entire sequence, like
if we had to print out all the elements of a sequence
in ascending order (&quot;sort a sequence&quot;).
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
Primes = [2, 3, 5, 7, 11, 13]
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

print(Primes)
print(Rainbow)
''',
    'expected_output': """
[2, 3, 5, 7, 11, 13]
['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
""",
},


{
    "header": "Lists",
    "text": """
To store such data, in Python you can use the data structure
called <em>list</em> (in most programming languages the term &mdash; &ldquo;array&rdquo; is used).
A list is a sequence of elements <b>numbered
from 0</b>, just as characters in the string. The list can be defined manually defining each of its elements, like here:


The list <code>Primes</code> has 6 elements, namely:
<code>Primes[0]&nbsp;==&nbsp;2</code>, 
<code>Primes[1]&nbsp;==&nbsp;3</code>, 
<code>Primes[2]&nbsp;==&nbsp;5</code>, 
<code>Primes[3]&nbsp;==&nbsp;7</code>, 
<code>Primes[4]&nbsp;==&nbsp;11</code>, 
<code>Primes[5]&nbsp;==&nbsp;13</code>.

The list <code>Rainbow</code> has 7 elements, each of which
is the string. Indexes of elements are written in square brackets.

Like characters in a string, list elements can also have negative index, for example, 
<code>Primes[-1]&nbsp;==&nbsp;13</code>, 
<code>Primes[-6]&nbsp;==&nbsp;2</code>.  The negative index means we start at the last element and go left when reading a list.
""",
    'tasks': [
    {
        "instruction": 'What is <code>Primes[-3]</code>? Make your guess, then type <code>print(Primes[-3])</code>',
        'expected_output': '7',
    },
],
    "allfine":
"""
Since <code>Primes[-1]</code> is equal to 13 and <code>Primes[-6]</code> is equal to 2, it is quite easy to fill in the missing elements: <code>Primes[-2]</code> is equal to 11, <code>Primes[-3]</code> is equal to 7, <code>Primes[-4]</code> is equal to 5, <code>Primes[-5]</code> is equal to 3, <code>Primes[-6]</code> is equal to 2.
""",
    "program": '''
Primes = [2, 3, 5, 7, 11, 13]
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
''',
},



{
    "header": "The number of elements: len()",
    "text": """Most of programs work not only with variables. They also use lists of variables.
A program can handle an information about students by reading the list of
students from the keyboard or from a file. A change in the number of students in a class
must <b>not</b> require modification of the program source code.

We have already faced the task of processing elements of a sequence &mdash;
for example, when finding the largest element of the sequence. But 
we haven't kept the whole sequence in computer's memory. However, 
in many situations it is necessary to keep the entire sequence, like
if we had to print out all the elements of a sequence
in ascending order (&quot;sort a sequence&quot;).

You can obtain the number of elements in a list with the function <code>len</code> (meaning <i>length of the list</i>), e.g. 
<code>len(Primes)&nbsp;==&nbsp;6</code>.
""",
    'tasks': [
    {
        "instruction": 'Calculate the length of <code>Primes</code> list. (We hope you know that there are infinite number of prime numbers!)',
        'expected_output': '6',
    },
    {
        "instruction": 'Calculate the length of <code>Rainbow</code> list.',
        'expected_output': '7',
    },
],
"hint":
"""
Of course all you have to do is to <code>print(len(Primes))</code>, and then <code>print(len(Rainbow))</code>.
""",
    "program": '''
Primes = [2, 3, 5, 7, 11, 13]
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
''',
},


{
    "header": "List elements are changeable",
    "text": """
    Unlike strings, the elements of a list are changeable; they can be changed by assigning new values to them.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('And now print the rainbow!')
for i in range(len(Rainbow)):
    print(Rainbow[i])
''',
    'expected_output': """
Red
And now print the rainbow!
red
Orange
Yellow
Green
Blue
Indigo
Violet
""",
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
},


{
    "header": "Creating a list: append()",
    "text": """
We want to tell you several ways of creating and reading lists. First of all, you can create
an empty list (the list with no items, its length is 0), and you can add items to the end of your list
using <code>append</code>. For example, suppose the program receives
the number of elements in the list <code>n</code>, and then <code>n</code> elements of
the list one by one each at the separate line. Look at the example of input data in this format.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [] # create an empty list
n = int(input()) # read number of element in the list
for i in range(n): 
    new_element = int(input()) # read next element
    a.append(new_element) # add it to the list
    # the last two lines could be replaced by one:
    # a.append(int(input()))
print(a)
''',
"input_data": '''
5
1809
1854
1860
1891
1925
'''
,
    'expected_output': """
[1809, 1854, 1860, 1891, 1925]
""",
},



{
    "header": "The number of elements: len()",
    "text": """
In the demonstrated example the empty list is created, then the number of elements is read, then you read the list items line by line and append to the end.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)
''',
"input_data": '''
5
1809
1854
1860
1891
1925
'''
,
    'expected_output': """
[1809, 1854, 1860, 1891, 1925]
""",
},


{
    "header": "What can you do with your list?",
    "text": """
There are several operations defined for lists: list concatenation
(&quot;gluing&quot; one list to another) and repetition (multiplying a list
by a number).
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [1, 2, 3]
b = [4, 5]
c = a + b
d = b * 3
print([7, 8] + [9])
print([0, 1] * 3)
print(c)
print(d)
''',
    'expected_output': """
[7, 8, 9]
[0, 1, 0, 1, 0, 1]
[1, 2, 3, 4, 5]
[4, 5, 4, 5, 4, 5]
""",
    "allfine": 'The resulting list <code>c</code> will be equal to <code>[1, 2, 3, 4, 5]</code>, and a list of <code>d</code> will be equal to <code>[4, 5, 4, 5, 4, 5]</code>. This allows you to organize the process of reading lists differently: first, consider the size of the list and create a list from the desired number of elements, then loop through the variable <code>i</code> starting with number 0 and inside the loop read <code>i</code>-th element of the list:',
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
},


{
    "header": "Print your list!",
    "text": """
You can print <i>elements</i> of a list <code>a</code> with <code>print(a)</code>;
this displays the list items surrounded by square brackets and separated by commas. 
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [0] * int(input())
for i in range(len(a)):
    a[i] = int(input())
print(a)
''',
"input_data": '''
5
1809
1854
1860
1891
1925
'''
,
    'expected_output': """
[1809, 1854, 1860, 1891, 1925]
""",
},


{
    "header": "Print your list! - 2",
    "text": """
In general, this is inconvenient; usually, you are in need to print all the elements in one line or one item per line. Here are two examples of that, using other forms of loop:

<p> Here the index <code>i</code> is changed, then the element <code>a[i]</code> is displayed.

<p>In this example, the list items are displayed in one line separated by spaces, and it's not the index that is changed but rather the value of the variable itself (for example, in the loop <code>for elem in ['red', 'green', 'blue']</code> variable
<code>elem</code> will take the values <code>'red'</code>,
<code>'green'</code>, <code>'blue'</code> successively.
""",
    "instructions": 'Type <code>print(a[i])</code> in the loop body (the third line) and click "Run" to see what happens in output. Then uncomment three line printing the list in a single line.',
    "program": '''
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    # Your code here!

# a = [1, 2, 3, 4, 5]
# for elem in a:
#     print(elem, end=' ')
''',
    'expected_output': """1
2
3
4
5
1 2 3 4 5 
""",
},



{
    "header": "Iterating over the elements",
    "text": """
Pay special attention to the last example! A very important part of Python ideology is <code>for</code> loop, which provides the convenient way to iterate over all elements of some sequence.

This is where Python differs from Pascal, where you have to iterate over elements' <i>indexes</i>,
but not over the elements themselves. 

Here's an example showing the use of the <code>for</code> loop when you are needed to extract all the digits from a string and to make numeric list of them.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# given: s = 'ab12c59p7dq'
# you need to extract digits from the list s
# to make it so:
# digits == [1, 2, 5, 9, 7]
s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)
''',
    'expected_output': """
[1, 2, 5, 9, 7]
""",
},


{
    "header": "How do you split?",
    "text": """
List items can be given in one line separated by a character; in this case, the entire list can be read using <code>input()</code>. You can then use a string method
<code>split()</code>, which returns a list of strings resulting after cutting the initial string by spaces. Example:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# the input is a string
# 1 2 3
s = input() # s == '1 2 3'
a = s.split() # a == ['1', '2', '3']
print(a)
''',
"input_data": '''
1 2 3
'''
,
    'tasks': [
        {
            "instruction": '''Run this program with the input data of <code>1 2 3</code>. Note that the output is <code>['1', '2', '3']</code>. It consists of strings, not of numbers!''',
            'expected_output': "['1', '2', '3']",
        },
        {
            "instruction": 'Usually you want to get the list of numbers. Thus, you have to convert the list items one by one to integers. Before <code>print(a)</code>, add a <code>for</code> loop which will convert every element to the <code>int()</code> version of it.',
            'expected_output': "[1, 2, 3]",
        },
    ],
    'expected_output': 'replit',
                "hint": """
<pre>
for i in range(len(a)):
    a[i] = int(a[i])
</pre>
""",

},



{
    "header": "Viva love generators",
    "text": """
Using the special magic of Python &mdash; generators &mdash;
the same can be done in one line. We will explain of how does this code work in the next step.

If you want to read a list of fractional numbers, you have to change
<code>int()</code> to <code>float()</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [int(s) for s in input().split()]
print(a)
''',
"input_data": '''
1 2 3
'''
,
    'expected_output': "[1, 2, 3]",
},


{
    "header": "Viva love generators",
    "text": """
The method <code>split()</code> has an optional parameter that
determines which string will be used as the separator
between list items. For example, calling the method <code>split('.')</code>
returns the list obtained by splitting the initial string where the character
<code>'.'</code> is encountered:
""",
    "instructions": 'Run and look at the output.',
    "program": '''
a = '192.168.0.1'.split('.')
print(a)
''',
    'expected_output': "['192', '168', '0', '1']",
},


{
    "header": "Join() me",
    "text": """
In Python, you can display a list of strings using one-line commands. 
For that, the method <code>join</code> is used; this method has one parameter: a list of strings. 
It returns the string obtained by concatenation of the elements given, and the separator is inserted between the elements of the list; this separator is equal to the string on which is the method applied. We know that you didn't
understand the previous sentence from the first time. :) Look at the examples:
""",
    'tasks': [{
        "instruction": 'Add a <code>print()</code> instruction to print "red", "green", "blue" separated by owl: <code>(@,@)</code>',
        'expected_output': """
red green blue
redgreenblue
red***green***blue
red(@,@)green(@,@)blue
""",
}],
    "program": '''
a = ['red', 'green', 'blue']
print(' '.join(a))

print(''.join(a))

print('***'.join(a))
''',
},


{
    "header": "Dark magic",
    "text": """
If a list consists of numbers, you have to use the dark magic of generators.
See how you can print out the elements of a list, separated by spaces.
""",
    "instructions": 'Run the code',
    "program": '''
a = [1, 2, 3]
print(' '.join([str(i) for i in a]))
# the next line causes a type error,
# as join() can only concatenate strs
# print(' '.join(a))
''',
    'expected_output': "1 2 3",
    "allfine": 'However, if you are not a fan of dark magic, you can achieve the same effect using the loop <code>for</code>.',
},


{
    "header": "Generators-1",
    "text": """
<p>To create a list filled with identical items, you can use
the repetition of list, for example:

<p>To create more complicated lists you can use
<em>generators</em>: the expressions allowing to fill a list according to a formula.
The general form of a generator is as follows:

<code>
[expression for variable in sequence]
</code>

<p>where <code><em>variable</em></code> is the ID of some
variable, <code><em>sequence</em></code> is a sequence of values,
which takes the variable (this can be a list, a string, or an object obtained using the function <code>range</code>),
<code><em>expression</em></code>&nbsp;&mdash; some expression, usually depending on the variable used in the generator. The list elements will be filled according to this expression.

""",
    "program": '''
n = 5
a = [0] * n
print(a)
''',
    'expected_output': "[0, 0, 0, 0, 0]",
},



{
    "header": "Generators-2",
    "text": """
Here are some examples of generators.

This is how you create a list of <code>n</code> zeros using the generator.
""",
    "program": '''
a = [0 for i in range(5)]
print(a)
''',
    'expected_output': "[0, 0, 0, 0, 0]",
},


{
    "header": "Generators-3",
    "text": """
Here's how you create a list filled with squares of integers.
""",
    "program": '''
n = 5
a = [i ** 2 for i in range(n)]
print(a)
''',
    'expected_output': "[0, 1, 4, 9, 16]",
},


{
    "header": "Generators-4",
    "text": """
If you need to fill out a list of squares of numbers from 1 to <code>n</code>,
you can change the settings of <code>range</code> to
<code>range(1, n + 1)</code>:
""",
    "program": '''
n = 5
a = [i ** 2 for i in range(1, n + 1)]
print(a)
''',
    'expected_output': "[1, 4, 9, 16, 25]",
},


{
    "header": "Generators-5",
    "text": """
Here's how you can get a list filled with random
numbers from 1 to 9 (using <code>randrange</code>
from the module <code>random</code>):
""",
    "program": '''
from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]
print(a)
''',
},


{
    "header": "Generators-6",
    "text": """
And in this example the list will consist of lines read
from standard input: first, you need to enter the number of elements of
the list (this value will be used as an argument of
the function <code>range</code>), second&nbsp;&mdash; that number of strings.
""",
    "program": '''
a = [input() for i in range(int(input()))]
print(a)
''',
"input_data": '''
5
a
b
1
2
3
'''
,
    'expected_output': '''['a', 'b', '1', '2', '3']''',
},


{
    "header": "Slices-1",
    "text": """
<p>You can <em>slice</em> lists and strings. Namely:


<p><code>A[i:j]</code> will return you the list 
<code>A[i]</code>, <code>A[i+1]</code>, ..., <code>A[j-1]</code>.

<p><code>A[i:j:-1]</code>&nbsp; slice <code>i-j</code> elements

<code>A[i]</code>, <code>A[i-1]</code>, ..., <code>A[j+1]</code>
(that is, in descending order of indexes).

<p><code>A[i:j:k]</code> will return you the list 
<code>A[i]</code>, <code>A[i+k]</code>, <code>A[i+2*k]</code>,... .
If <code>k</code>&lt;0, the elements come in descending order.
""",
    "program": '''
A = [10, 20, 30, 40, 50, 60]
print(A[1:4])
s = 'abcdef'
print(s[1:4])
''',
},


{
    "header": "Slices-2",
    "text": 'In <code>A[i:j]</code> you may omit each of the numbers <code>i</code> or <code>j</code> (remember, they stand for the beginning of the slce and for the end of the slice).',
    "program": '''
s = 'abcdef'
print(s[1:4])
print(s[1:])
print(s[:4])
''',
},


{
    "header": "Lists are mutable",
    "text": """
Lists, unlike strings, are <b>mutable objects</b>: you can assign a list item to a new value. Moreover, it is possible to change entire
slices. Think how this program works before running it.
""",
    "program": '''
A = [1, 2, 3, 4, 5]
A[2:4] = [7, 8, 9]
# print(A)
''',
'tasks': [
    {
        "instruction": 'Uncomment the line <code>print(A)</code>. Run the program. Enjoy the output.',
        'expected_output': "[1, 2, 7, 8, 9, 5]",
    },
],
    "allfine": '''Here we received a list <code>[1, 2, 3, 4, 5]</code>, and then try to replace the two
 elements of the slice <code>A[2:4]</code> with a list of three elements. 
 The two elements were replaced by three. The resulting list is as follows:
  <code>[1, 2, 7, 8, 9, 5]</code>.''',
},


{
    "header": "Lists are mutable-2",
    "text": """
And here, the resulting list will be <code>[40, 2, 30, 4, 20, 6, 10]</code>. The reason is,
<code>A[::-2]</code> is a list of elements

<code>A[-1]</code>, <code>A[-3]</code>, <code>A[-5]</code>, A<code>-7</code>, and that elements are
assigned to 10, 20, 30, 40, respectively. 

If a discontinuous slice (i.e. a slice with a step <code>k</code>, <code>
k > 1</code>) is assigned a new value, then the number of elements in the old and new slices
necessarily coincide, otherwise error <code>ValueError</code> occurs.
""",
    "program": '''
A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40]
# print(A)
''',
'tasks': [{
        "instruction": 'Uncomment the line <code>print(A)</code>. Run the program. Enjoy the output.',
        'expected_output': "[40, 2, 30, 4, 20, 6, 10]",
    },
],
},



{
    "header": "Operations on lists",
    "text": """
You can easily do many different operations with lists.

<code>x in A</code> Checks whether an item is in the list A. Returns True or False
<br>
<code>x not in A</code> Checks whether an item is not in the list A. Returns True or False
<br>
<code>min(A)</code> Returns the smallest element of list A
<br>
<code>max(A)</code> Returns the biggest element of list A
<br>
<code>A.index(x)</code> The index of the first occurrence of element x in the list; in its absence generates an exception ValueError
<br>
<code>A.count(x)</code> The number of occurrences of element x in the list
<br>
""",
    "program": '''
a = [2, 3, 5, 8, 13, 5, 5]
# print(8 in a)
''',
    'tasks': [
        {
            "instruction": '''Given a list <code>[2, 3, 5, 8, 13, 5, 5]</code>, check if <code>8</code> is in it''',
            'expected_output': 'True',
        },
        {
            "instruction": "Check if <code>15</code> isn't in it</code>",
            'expected_output': 'False',
        },
        {
            "instruction": 'Print the minimum of the list',
            'expected_output': "2",
        },
        {
            "instruction": 'Print the maximum of the list',
            'expected_output': '13',
        },
        {
            "instruction": "Print the index of the element <code>13</code>",
            'expected_output': '4',
        },
        {
            "instruction": "Print the number of occurrences of <code>5</code> in the list",
            'expected_output': "3",
        },
    ],
    "allfine": "Congratulations! You've passed the lists level!",
},

]