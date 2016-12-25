STEPS = [{
    "header": "Nested lists: processing and printing",
    "text": """In real-world tasks you often have to store rectangular data table. [say more on this!]
Such tables are called <em>matrices</em> or two-dimensional arrays. In Python any table can be represented as a list of lists (a list, where each element is in turn a list).
For example, here's the program that creates a numerical table with two rows and three columns, and then makes some manipulations with it:

The first element of <code>a</code> here &mdash; <code>a[0]</code> &mdash; is a list of numbers
<code>[1, 2, 3]</code>. The first element of <em>this</em> new list is <code>a[0][0] == 1</code>; moreover,
<code>a[0][1] == 2</code>, <code>a[0][2] == 3</code>,
<code>a[1][0] == 4</code>, <code>a[1][1] == 5</code>,
<code>a[1][2] == 6</code>.""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
b = a[0]
print(b)
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print(a[0])
print(b)
''',
    'expected_output': 
"""
[1, 2, 3]
[4, 5, 6]
[1, 2, 3]
3
[[1, 7, 3], [4, 5, 6]]
[1, 7, 3]
[1, 7, 9]
[1, 7, 9]
""",
    "allfine": "Let's move on!",
},

{
    "header": "Nested loops",
    "text": """To process 2-dimensional array, you typically use nested
loops. The first loop iterates through the row number, the second loop runs through the elements inside of a row.
For example, that's how you display two-dimensional numerical list on the screen line by line,
separating the numbers with spaces:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
''',
    'expected_output': 
"""
1 2 3 4 
5 6 
7 8 9 
""",
    "allfine": "Let's move on!",
},

{
    "header": "Looping by elements",
    "text": """We have already tried to explain that a for-loop variable in 
Python can iterate not only over a <code>range()</code>, but generally over all the elements of any sequence. 
Sequences in Python are lists and strings (and some other objects that we haven't met yet). 
Look how you can print a two-dimensional array, using this handy feature of loop <code>for</code>:""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
''',
    'expected_output': 
"""
1 2 3 4 
5 6 
7 8 9 
""",
    "allfine": "Let's move on!",
},

{
    "header": "Looping by elements",
    "text": """Naturally, to output a single line you can use
method <code>join()</code>:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    print(' '.join([str(elem) for elem in row]))
''',
    'expected_output': 
"""
1 2 3 4 
5 6 
7 8 9 
""",
    "allfine": "Let's move on!",
},

{
    "header": "Problem: sum all the elements",
    "text": """This is how you can use 2 nested loops to calculate the sum of all
the numbers in the 2-dimensional list.

Or the same with iterating by elements, not by the variables <code>i</code> and <code>j</code>:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)
''',
    'expected_output': 
"""
45
45
""",
    "allfine": "Let's move on!",
},

{
    "header": "Nested lists: the creation",
    "text": """Suppose that two numbers are given: the number of rows of <code>n</code> and the number of columns
<code>m</code>. You must create a list of size <code>n</code>&times;<code>m</code>, filled with, say, zeros.

The obvious solution appears to be wrong:

This can be easily seen if you set the value of <code>a[0][0]</code>
to <code>5</code>, and then print the value of <code>a[1][0]</code>&nbsp;&mdash; it will also be equal to 5. The reason is,
<code>[0] * m</code> returns just a <em>reference</em> to a list of <code>m</code> zeros, but not a list.
The subsequent repeating of this element creates a list of <code>n</code>
items that all reference to the same list (just
as well as the operation <code>b&nbsp;=&nbsp;a</code> for lists does not create
the new list), so all rows in the resulting list are actually
the same string.

Using our visualizer, keep track of the id of lists. If two lists have the same id number, it's actually the same list in memory.
""",
'tasks': [
    {
        "instruction": 'Add the line <code>a[0][0] = 5</code>',
        'expected_output': '',
    },
    {
        "instruction": 'Add the line <code>print(a)</code>. Click "Run" to see what happens in output!',
        'expected_output': """
[[5, 0, 0], [5, 0, 0], [5, 0, 0], [5, 0, 0], [5, 0, 0], [5, 0, 0], [5, 0, 0], [5, 0, 0]]
        """,
    },
],
    "program": '''
m = 3
n = 8
a = [[0] * m] * n
''',
    "allfine": "Let's move on!",
},

{
    "header": "The right way",
    "text": """Thus, a two-dimensional list cannot be created simply by
repeating a string. What to do?..

A possible way: you can create a list of <code>n</code> elements
(say, of <code>n</code> zeros) and then make each of the elements a link to another one-dimensional list of <code>m</code>
elements:
""",
    "instructions": 'Do that!',
    "program": '''
n = 3
m = 4
a = [[0] * m] * n
a[0][0] = 5
print(a)

# or

n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
a[0][0] = 5
print(a)
''',
    'expected_output': """
[[5, 0, 0, 0], [5, 0, 0, 0], [5, 0, 0, 0]]
[[5, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """,
    "allfine": "Let's move on!",
},

{
    "header": "Another right way",
    "text": """Another (but similar) way: create an empty list and then <code>append</code> a new element to it <code>n</code>
times (this element should be a list of length <code>m</code>):
""",
    "instructions": 'Do that!',
    "program": '''
n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)
print(a)
''',
    'expected_output': """
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """,
    "allfine": "Let's move on!",
},

{
    "header": "The easiest way",
    "text": """But the easiest way is to use generator, creating a list of
<code>n</code> elements, each of which is a list of <code>m</code> zeros: 

In this case each element is created independently from the others.
The list <code>[0] * m</code> is <code>n</code> times consructed as the new one, and no copying of references occurs.
""",
    "instructions": 'Do that!',
    "program": '''
n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
''',
    'expected_output': """
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """,
    "allfine": "Let's move on!",
},

{
    "header": "The easiest way",
    "text": """But the easiest way is to use generator, creating a list of
<code>n</code> elements, each of which is a list of <code>m</code> zeros: 

In this case each element is created independently from the others.
The list <code>[0] * m</code> is <code>n</code> times consructed as the new one, and no copying of references occurs.
""",
    "instructions": 'Do that!',
    "program": '''
n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
''',
    'expected_output': """
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """,
    "allfine": "Let's move on!",
},

{
    "header": "How do you input a two-dimensional array?",
    "text": """But the easiest way is to use generator, creating a list of
<code>n</code> elements, each of which is a list of <code>m</code> zeros: 

In this case each element is created independently from the others.
The list <code>[0] * m</code> is <code>n</code> times consructed as the new one, and no copying of references occurs.
""",
    "instructions": 'Do that!',
    "program": '''
# the first line of input is the number of rows of the array
n = int(input()) 
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
print(a)
''',
"input_data": '''
3
1 2 3 4
5 6
7 8 9
'''
,
    'expected_output': """
[[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    """,
    "allfine": "Let's move on!",
},

{
    "header": "Generator way",
    "text": """You can do the same with generators:
""",
    "instructions": 'Do that!',
    "program": '''
# the first line of input is the number of rows of the array
n = int(input()) 
a = [[int(j) for j in input().split()] for i in range(n)]
print(a)
''',
"input_data": '''
3
1 2 3 4
5 6
7 8 9
'''
,
    'expected_output': """
[[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    """,
    "allfine": "Let's move on!",
},

{     "header": "Processing a two-dimensional array: an example",
"text": """Suppose you are given a square array (an array of
<code>n</code> rows and <code>n</code> columns). And suppose you
have to set elements of the main diagonal equal to 1 (that is,
those elements <code>a[i][j]</code> for which <code>i==j</code>),
to set elements above than that diagonal equal to 0, and to set
elements below that diagonal equal to 2. That is, you need to produce
the array like that the array you can see on the code side.

You can produce such an array manually by setting <code>a[0][0] = 1</code>, <code>a[0][1] = 0</code> and so on, but you won't do it manually for arrays of 10000 rows and 10 columns, which are often the case.

We are eager to show you several ways to solve this problem. 
""",
    "instructions": 'Do that!',
    "program": '''
#   This is example for <code>n==4</code>.
#
#   1 0 0 0
#   2 1 0 0
#   2 2 1 0
#   2 2 2 1
''',

    'expected_output': '',
    "allfine": "Let's move on!",
},

{     "header": "Processing a two-dimensional array: an example",
"text": """
Note:

<ol type=1 start=1> 
<li>elements that lie above the main diagonal&nbsp;&ndash; are elements <code>a[i][j]</code> for which <code>i&lt;j</code>
<li>for elements below the main diagonal <code>i&gt;j</code>
</ol> 

Thus, we can compare the values <code>i</code> and <code>j</code>; the result of comparison determines the value of <code>a[i][j]</code>.

On the code side there's the algorithm we get.
""",
    "instructions": 'Do that!',
    "program": '''
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
''',
    'expected_output': """
1 0 0 0
2 1 0 0
2 2 1 0
2 2 2 1
    """,
    "allfine": "This algorithm is slow: it uses two loops and for each pair <code>(i,j)</code> executes one or two <code>if</code> instructions. If we choose another algorithm, we will be able to do it without a conditional statement.",
},

{     "header": "I fill you-1",
"text": """

""",
    "instructions": "Write such a loop that would fill the diagonal elements (the elements <code>a[i][i]</code>) with <code>1</code>'s.",
    "program": '''
# First, fill the main diagonal, for which we will need one loop:
''',
'hint': '''
n = 7 # for example, 7
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][i] = 1

for row in a:
    print(' '.join([str(elem) for elem in row]))
''',
    'expected_output': """
1 0 0 0 0 0 0
0 1 0 0 0 0 0
0 0 1 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 1 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 1
""",
    "allfine": "Nice! The main diagonal is filled. Now it's to fill the rest of array.",
},

{     "header": "I fill you-2",
"text": """
Think of the elements above the main diagonal; they must be filled with zeros. To make this, for each row
with the number <code>i</code> you need to assign a value to <code>a[i][j]</code> for <code>j</code>=<code>i+1</code>, ..., <code>n-1</code>. To do that, you need nested loops; look at the code section.

By analogy, as you see, for <code>j</code> less than <code>i</code> the elements <code>a[i][j]</code> are set equal to <code>2</code>.
""",
    "instructions": "Combine this code and the code from the previous step to obtain the code filling the whole array.",
    "program": '''
for i in range(n):
    for j in range(i + 1, n):
        a[i][j] = 0

for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
''',
'hint': '''

''',
    'expected_output': """
1 0 0 0 0 0 0
2 1 0 0 0 0 0
2 2 1 0 0 0 0
2 2 2 1 0 0 0
2 2 2 2 1 0 0
2 2 2 2 2 1 0
2 2 2 2 2 2 1
""",
    "allfine": "Nice! The main diagonal is filled. Now it's to fill the rest of array.",
},

{     "header": "I fill you-3",
"text": """
Here's another solution, which repeats lists to build the next rows of the list. The <code>i</code>-th line of the list consists of <code>i</code> numbers
<code>2</code>, followed by one integer <code>1</code>, followed by <code>n-i-1</code> zeros:
""",
    "instructions": "Combine this code and the code from the previous step to obtain the code filling the whole array.",
    "program": '''
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
''',
'hint': '''

''',
    'expected_output': """
1 0 0 0 0 0 0
2 1 0 0 0 0 0
2 2 1 0 0 0 0
2 2 2 1 0 0 0
2 2 2 2 1 0 0
2 2 2 2 2 1 0
2 2 2 2 2 2 1
""",
    "allfine": "",
},

{     "header": "I fill you-4",
"text": """

""",
    "instructions": "Combine this code and the code from the previous step to obtain the code filling the whole array.",
    "program": '''
n = 4
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)
# or, without for-cycle,
# a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))    
''',

'hint': '''

''',
    'expected_output': """
1 0 0 0 0 0 0
2 1 0 0 0 0 0
2 2 1 0 0 0 0
2 2 2 1 0 0 0
2 2 2 2 1 0 0
2 2 2 2 2 1 0
2 2 2 2 2 2 1
""",
    "allfine": "",
},

{     "header": "Nested generators-1",
"text": """
You can use nested generators to create two-dimensional arrays, placing
the generator of the list which is a string inside the generator of all the strings. Recall that you can create a list of <code>n</code> rows and <code>m</code> columns using the generator (which
creates a list of <code>n</code> elements, where each element is a list of
<code>m</code> zeros):
""",
    "instructions": "Combine this code and the code from the previous step to obtain the code filling the whole array.",
    "program": '''
# As usual, you can replace the loop with the generator:
m = 3
n = 8
a = [[0] * m for i in range(n)]
print(a)
''',
'hint': '''

''',
    'expected_output': """
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
""",
    "allfine": "",
},

{     "header": "Nested generators-2",
"text": """
But the internal list can also be created using, for example, such generator:
<code>[0 for j in range(m)]</code>. Nesting one generator into another, we obtain the code as we wrote.

What's the point of using the longer syntax? At the moment, there's no point :), but the number 0 can be replaced by some expression that depends on <code>i</code> (the line number) and <code>j</code> (the column number), so with this longer syntax it is possible to get the matrix filled
according to some formula.
""",
    "instructions": "Combine this code and the code from the previous step to obtain the code filling the whole array.",
    "program": '''
m = 3
n = 8
a = [[0 for j in range(m)] for i in range(n)]
print(a)
''',
'hint': '''

''',
    'expected_output': """
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
""",
    "allfine": "",
},

{     "header": "Initialization: an example",
"text": """
For example, suppose you need to initialize the following array (for convenience, extra spaces are added between items):

In this array there are <code>n = 5</code> rows, <code>m = 6</code> columns, and the element
with row index <code>i</code> and column index <code>j</code> is calculated by the formula 

<code>a[i][j] = i * j</code>.

<p>And as always, you could use generator to create such an array:

<code>[[i * j for j in range(m)] for i in range(n)]</code>
""",
    "instructions": "Create such an array.",
    "program": '''
#    0  0  0  0  0  0
#    0  1  2  3  4  5
#    0  2  4  6  8 10
#    0  3  6  9 12 15
#    0  4  8 12 16 20
''',
'hint': '''
m = 6
n = 5
a = [[i * j for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))    
''',
    'expected_output': """
0 0 0 0 0 0
0 1 2 3 4 5
0 2 4 6 8 10
0 3 6 9 12 15
0 4 8 12 16 20
""",
    "allfine": "",
}


]