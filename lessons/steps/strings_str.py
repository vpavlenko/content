STEPS = [{
    "header": "The string theory-1",
    "text": """
A string can be read from the standard input using the function <code>input()</code>. 
Moreover, you can define it in single or double quotes. Look at the code section:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
a = 'No man is an island'
b = "Who is John Galt?"
your_string = input()

print(a)
print(b)
print(your_string)
''',
    "input_data": "write something here",
    "allfine": '',
},



{
    "header": "The string theory-2",
    "text": """
You can repeat a string by multiplying it by an integer.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''

''',
'tasks': [
    {
        "instruction": "Type <code>print('>_<' * 5)</code>, then run your program.",
        'expected_output': '>_<>_<>_<>_<>_<',
    },
    {
        "instruction": "Do you like the output? Personally, I don't: the symbols come too close to each other. Correct the string <code>'>_<'</code> such that smiles have <b>two</b> spaces between them.",
        'expected_output': '>_<  >_<  >_<  >_<  >_<',
    },
],
    "allfine": '',
},


{
    "header": "The string theory-3",
    "text": """
A string in Python is a sequence of characters. The function <code>len(some_string)</code>
returns how many characters there are in a string:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print(len('abcdefghijklmnopqrstuvwxyz')) 
''',
'expected_output': '26',
    "allfine": 'We see Python successfully calculated the length of our string &mdash; we know that <a href="https://en.wikipedia.org/wiki/English_alphabet">English alphabet</a> contains exactly 26 letters.',
},


{
    "header": "The string theory-4",
    "text": """
Every object in Python can be converted to string using the function <code>str(some_object)</code>.
So we can convert numbers to strings:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = str(2 ** 100)
print(s)
print(len(s))
''',
     'expected_output': """
1267650600228229401496703205376
31
""",
    "allfine": '',
},



{
    "header": "Slice Girls: a single character",
    "text": """
A slice gives from the given string one character or some fragment:
substring or subsequence.

The simplest form of slice is a single character
slice: <code>S[i]</code> gives <code>i</code>th character of the string. Now, the hardest thing to get all this string business: <b>indexing starts at 0; the first element has index 0, the second has index 1, and so on</b>.
That is, if <code><nobr>S = 'Hello'</nobr></code>, 
<code><nobr>S[0] == 'H'</nobr></code>, <code><nobr>S[1] == 'e'</nobr></code>, <code><nobr>S[2] == 'l'</nobr></code>,
<code><nobr>S[3] == 'l'</nobr></code>, <code><nobr>S[4] == 'o'</nobr></code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
S = 'Hello'

print(S[0])
print(S[1])
print(S[2])
print(S[3])
print(S[4])
''',
'expected_output': """
H
e
l
l
o
""",
    "allfine": '',
},



{
    "header": "No char type in Python",
    "text": """
Note that in Python there is no special type for characters of a string. <code>S[i]</code>
also has the type <code>str</code>, just as the source string. 

<p>Number <code>i</code> in <code>S[i]</code> is called <b><em>index</em></b>.

<p>If you specify a negative index, it is counted
starting at the end of your string, starting with the number <code>-1</code>. That said, <code><nobr>S[-1] == 'o'</nobr></code>,
<code><nobr>S[-2] == 'l'</nobr></code>, <code><nobr>S[-3] == 'l'</nobr></code>, <code><nobr>S[-4] == 'e'</nobr></code>,
<code><nobr>S[-5] == 'H'</nobr></code>. 
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
S = 'Hello'

print(S[-1])
print(S[-2])
print(S[-3])
print(S[-4])
print(S[-5])
''',
'expected_output': """
o
l
l
e
H
""",
    "allfine": '',
},


{
    "header": "Table tennis",
    "text": """
Let's summarize it in the table:

<table border='1' cellspacing="0" cellpadding="3"> 
<tr> 
<th>String S</th> 
<td align="center">H</td> 
<td align="center">e</td> 
<td align="center">l</td> 
<td align="center">l</td> 
<td align="center">o</td> 
</tr> 
<tr> 
<th>Index</th> 
<td align="center">S[0]</td> 
<td align="center">S[1]</td> 
<td align="center">S[2]</td> 
<td align="center">S[3]</td> 
<td align="center">S[4]</td> 
</tr> 
<tr> 
<th>Index</th> 
<td align="center">S[-5]</td> 
<td align="center">S[-4]</td> 
<td align="center">S[-3]</td> 
<td align="center">S[-2]</td> 
<td align="center">S[-1]</td> 
</tr> 
</table>
""",
    "instructions": 'Click "Run" to proceed!',
    "program": '''

''',
    "allfine": '',
},




{
    "header": "Don't be an errorist",
    "text": """
If the index in the slice <code>s[i]</code> is 
<ul>
<li>greater than or equal to <code>len(s)</code></li>
<li>or less than <code>-len(s)</code></li>
</ul>
the following error occurs: <code>IndexError: string index out of range</code>.

So it's a bad idea to ask Python to <code>print(s[100])</code> for a short string like <code>s = "My morning portion of Snakify"</code>. For such string, there is no 101-th symbol (never forget any indexing in any programming languages starts at 0; the first symbol always has index 0).
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = "Don't print 1000-th symbol"
''',
'tasks': [
    {
        "instruction": "Print the length of the given string.",
        'expected_output': '26',
    },
    {
        "instruction": "Calculate the index of the last symbol.",
        'expected_output': '25',
    },
    {
        "instruction": "Print the last symbol.",
        'expected_output': 'l',
    },
],
"hint": """
print(len(s))
last = len(s) - 1  
print(s[last]) 
print(s[last+1]) 
""",
    "allfine": '',
},




{
    "header": "What is a substring?",
    "text": """
If you call slice with two parameters <code>s[a:b]</code>, it 
returns the substring of length <code>b - a</code>,
which starts with the character at index <code>a</code> and
ends with the character at index </code>b</code>, <b>not including it</b>.
For example, if <code>s == 'Hello'</code>, <code>s[1:4] == 'ell'</code> (for slice <code>s[1:4]</code> only indexes 1,2 and 3 are included).

You can get the same substring using <code>s[-4:-1]</code> (recall negative indexing starts at the end of a string).

You may mix positive and negative indexes in the same slice: for example, <code>s[1:-1]</code> is
exactly the same substring (the slice begins with the character with index 1 and 
ends with an index of -1, not including it).
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'Hello'
print(s[1:4])
print(s[-4:-1])
print(s[1:-1])
''',
'expected_output': """
ell
ell
ell
""",
    "allfine": '',
},



{
    "header": "Playing with parameters",
    "text": """
Slices with two parameters never cause <code>IndexError</code>. For example, for <code>s == 'Hello'</code> 
the slice <code>s[1:5]</code> 
returns the string <code>'ello'</code>, and the result is the same as
if the second index was very large, like
<code>s[1:100]</code>.

If you omit the second parameter (but preserve the colon),
then the slice continues until the end of a string. For example, to remove
the first character from a string (its index is 0)
take the slice <code>s[1:]</code>. Similarly,
if you omit the first parameter (<code>s[:7]</code>), then Python takes the slice, starting at the beginning of a string.
That is, to remove the last character from a string, you can use slice
<code>s[:-1]</code>. The slice <code>s[:]</code> is equal to a string
<code>s</code> itself.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'Hello'
print(s[1:5])    
print(s[1:100])  
print(s[1:])     
print(s[:-1])    
print(s[:])      
''',
'expected_output': """
ello
ello
ello
Hell
Hello
""",
    "allfine": '',
},



{
    "header": "Immutability of strings",
    "text": """
Any slice of a string creates a new string and never modifies the original one. The reason is, in Python strings are immutable, i.e they cannot be changed as objects.
You can only assign the variable to a new string, but the old one stays in memory.

(In fact in Python there are no variables. They are only names that are pointing to objects.
You can first point with a name to an object, and then point to the same object with another name; different names
can point to the same object.)
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'Hello'
t = s  # s and t point to the same string
t = s[2:4]  # now t points to the new string 'll'
print(s)  # prints 'Hello' as s is not changed
print(t)  # prints 'll'
''',
'expected_output': """
Hello
ll
""",
    "allfine": '',
},





{
    "header": "Slices: specifying the step",
    "text": """
If you specify a slice with three parameters <code>S[a:b:d]</code>,
the third parameter specifies the step, same as for function
<code>range()</code>. In this case only the characters with the indexes <code>a</code> <nobr><code>a + d</code></nobr>, <nobr><code>a + 2 * d</code></nobr> and so on are taken, until character with index <code>b</code> is reached and, as usual, <b>not 
including it</b>.
For instance, if the third parameter is equal to 2, the slice takes
every second character. 

We want to tell you the fun fact: if the step of the slice equals to
<code>-1</code>, the characters go in reverse order. :)
You can reverse a string <code>S</code> with this: <code>S[::-1]</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'abcdefg'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])
''',
'expected_output': """
b
g
bc
bcdef
abc
cdefg
abcdef
aceg
bdf
gfedcba
""",
    "allfine": '',
},






{
    "header": "Slices: specifying the step",
    "text": """
We'd like to stress how the third parameter of the slice is similar to the third parameter of the function <code>range()</code>:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'abcdefghijklm'

print(s[0:10:2])

for i in range(0, 10, 2):
    print(i, s[i])
''',
'expected_output': """
acegi
0 a
2 c
4 e
6 g
8 i
""",
    "allfine": 'These two two-line pieces of code are essentially the same.',
},



{
    "header": "Methods: find()",
    "text": """
A <em>method</em> is a function that is bound to an object. When a method is called,
the method is applied to an object and does some computations related to it.
Methods are invoked as <code>object_name.method_name(arguments)</code>.
For example, in <code>s.find(&quot;e&quot;)</code>&nbsp; the string method <code>find()</code> is applied to
the string <code>s</code> with one argument <code>&quot;e&quot;</code>.

Method <code>find()</code> takes a substring as argument and searches for it
inside the string on which it's called.
The function returns the index of the first occurrence of a substring.
If a substring is not found, the method returns <code>-1</code>. 
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'Hello'
print(s.find('e'))
# this will print 1
print(s.find('ll'))
# and this will print 2
print(s.find('L'))
# and this prints -1
''',
'expected_output': """
1
2
-1
""",
    "allfine": '',
},




{
    "header": "Methods: rfind()",
    "text": """
Similarly, the method <code>rfind()</code> returns the index of the last occurrence
of the substring.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'abracadabra'
print(s.find('b'))

print(s.rfind('b'))
''',
'expected_output': """
1
8
""",
    "allfine": '',
},




{
    "header": "More on find() and rfind() methods",
    "text": """
If you call <code>find()</code> with three arguments
<code>s.find(substring, left, right)</code>, the search is performed
inside the <code>s[left:right]</code> slice. If you specify only two arguments, like
<code>s.find(substring, left)</code>, the search is performed
in the slice <code>s[left:]</code>, that is, starting with the character at index
<code>left</code> until the end of a string. Method <code>s.find(substring, left, right)</code>
returns the absolute index (an index in the whole string <code>s</code>, and not in the slice).
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
s = 'my name is bond, james bond, okay?'
print(s.find('bond'))

print(s.find('bond', 12))

''',
'expected_output': """
11
23
""",
    "allfine": '',
},


{
    "header": "replace() method",
    "text": """
Method <code>replace()</code> replaces all occurrences of a given substring with another one. Syntax
<code>s.replace(old, new)</code>&nbsp; takes the string <code>s</code> and replaces
all occurrences of substring <code>old</code> with the substring <code>new</code>. 
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print('a bar is a bar, essentially'.replace('bar', 'pub'))
''',
'expected_output': """
a pub is a pub, essentially
""",
    "allfine": '',
},



{
    "header": "replace() method: calling it with three arguments",
    "text": """
You can pass the third argument <code>count</code> using <code>replace()</code> method, like this: <code>s.replace(old, new, count)</code>. If the third argument is passed, only first <code>count</code> occurrences are replaced.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print('a bar is a bar, essentially'.replace('bar', 'pub', 1))
''',
'expected_output': """
a pub is a bar, essentially
""",
    "allfine": '',
},



{
    "header": "count() method",
    "text": """
This method counts the number of occurrences of one string within another string. The simplest
form is this one: <code>s.count(substring)</code>. Only non-overlapping occurrences are taken into account.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print('Abracadabra'.count('a'))
# this will print '4'

print(('aaaaaaaaaa').count('aa'))
# and this will print '5'
''',
'expected_output': """
4
5
""",
    "allfine": '',
},



{
    "header": "count() method: calling it with three arguments",
    "text": """
If you specify three parameters <code><nobr>s.count(substring, left, right)</nobr></code>,
the count is performed within the slice <code>s[left:right]</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
print('A sailor went to sea to see what he could see, but all he could have see, was sea, sea, sea'.count('se', 25, -3))

# The function count() will calculate the slice [25:-3]. 
# The slice [25:-3] of
# 'A sailor went to sea to see what he could see, but all he could have see, was sea, sea, sea'
# is equal to
# 'ee what he could see, but all he could have see, was sea, sea, '
# Then the function count() is going to find occurences of 'se' in the resulting string. There are only four such occurences,
# thus it will print '4'.

''',
'expected_output': """
4
""",
    "allfine": '',
},

]

#<!-- ord, chr -->