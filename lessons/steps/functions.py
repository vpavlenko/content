STEPS = [{
    "header": "Enter the functions",
    "text": """Recall that in mathematics the factorial of a number n is defined as <nobr>n! = 1 &sdot; 2 &sdot; ... &sdot; n</nobr> (as the product of all integer numbers from 1 to n).
For example, <nobr>5! = 1 &sdot; 2 &sdot; 3 &sdot; 4 &sdot; 5 = 120.</nobr>
It is clear that factorial is easy to calculate, using a <code>for</code> loop.
Imagine that we need in our program to calculate the factorial of various numbers several times (or in different places of code).
Of course, you can write the calculation of the factorial once and then using Copy-Paste to insert it wherever you need it:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# compute 3!
res = 1
for i in range(1, 4):
    res *= i
print(res)

# compute 5!
res = 1
for i in range(1, 6):
    res *= i
print(res)
''',
    'expected_output': """
6
120
""",
    "allfine": """However, if we make a mistake in the initial code, this erroneous code will
     appear in all the places where we've copied the computation of factorial.
      Moreover, the code is longer than it could be. To avoid re-writing
       the same logic in programming languages the functions were invented.""",
},

{
    "header": "What is a function?",
    "text": """<b>Functions</b> are the code sections which are isolated from the rest of the program and executed only when called.
You've already met such functions as <code>sqrt()</code>, <code>len()</code> 
and <code>print()</code>. They all have something in common: they take parameters
 (zero, one, or several of them), and they can return a value 
 (or they can return nothing, <code>None</code>). For example, the function <code>sqrt()</code> accepts one parameter and returns a value (the square root of the given number). The <code>print()</code> function can take various number of arguments and returns nothing. 

Now we want to show you how to write a function called <code>factorial()</code> which takes a single parameter &mdash; the number, and returns a value &mdash; the factorial of that number.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
''',
'tasks': [
    {
        "instruction": 'After the function, type <code>print(factorial(3))</code>. Enjoy how you can calculate the factorial in a single line.',
        'expected_output': '6',
    },
    {
        "instruction": 'Type <code>print(factorial(5))</code>.',
        'expected_output': '120',
    },
],
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
},

{
    "header": "Explanations",
    "text": """
We want to provide a few explanations. First, the function code should be placed in the beginning of the program (before the place where we want to use the function <code>factorial()</code>, to be precise). The first line <code>def factorial(n):</code> of this example is a description of our function; the word <i>factorial</i> is an identifier (the name of our function). Right after the identifier, there goes the list of parameters that our function receives (in parentheses). The list consists of comma-separated identifiers of the parameters; in our case, there's only one parameter <code>n</code>. At the end of this row, put colon.

Then goes the function body. In Python, the body <i>must</i> be indented (by Tab or four spaces, as always). This function calculates the value of n! and stores it in the variable <code>res</code> (meaning "result"). The last line of the function is <code>return res</code>, which exits the function and returns the value of the variable <code>res</code>. 

The <code>return</code> statement can appear in any place of a function. Its execution exits the function and returns specified value to the place where the function was called. If the function does not return a value, the return statement won't actually return some value (though it still can be used). Some functions do not need to return values, and the return statement can be omitted for them.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(3))
print(factorial(5))
''',
    'expected_output': """
6
120
""",

},

{     "header": "Explanations-2",
"text": """
We'd like to provide another example. Here's the function <code>max()</code> 
that accepts two numbers and returns the maximum of them. Actually, this
 function has already become the part of Python syntax.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(3, 5))
print(max(5, 3))
print(max(int(input()), int(input())))
''',
"input_data": '''
10
20
'''
,
    'expected_output': """
5
5
20
""",

},




{     "header": "Explanations-3",
"text": """
Now you can write a function <code>max3()</code> that takes three numbers and returns the maximum of them.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def max3(a, b, c):
    # Your code here!


print(max3(3, 6, 5))
''',
'hint': '''
You can do something like <code>max(max(a, b), c)</code>, right?
''',
    'expected_output': '6',
    "allfine": """To be frank, there was no need to create the 
    function <code>max3()</code>. The built-in function <code>max()</code> 
    in Python can accept various number of arguments and return the
     maximum of them. Here is an example of how such a function can be written.""",
},






{     "header": "Global variables",
"text": """
Inside the function, you can use variables declared somewhere outside of it.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def f():
    print(a)

a = 1
f()
''',
    'expected_output': '1',
    "allfine": """
Here the variable <code>a</code> is set to 1, and the function <code>f()</code> 
prints this value, despite the fact that when we declare the function <code>f</code> this variable 
is not initialized. The reason is, at the time of calling the function <code>f()</code> (the last string) the variable <code>a</code> 
already <i>has</i> a value. That's why the function <code>f()</code> can display it.

Such variables (declared outside the function but available inside the function) are
called <em>global</em>.
    """,
},



{     "header": "Local variables",
"text": """
But if you initialize some variable inside of the function, you won't be able
to use this variable outside of it. Run the code:
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def f():
    a = 1

f()
print(a)
''',
    "allfine": "We receive error <code>NameError: name 'a' is not defined</code>. Such variables declared within a function are called <em>local</em>. They become unavailable after you exit the function.",
},





{     "header": "Local and global variables: hey, what happens in reality?",
"text": """
One fact may seem strange: if you initialize some variable inside of the function, you won't be able
to use this variable outside of it.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# What's really charming here is what happens
# if you change the value of a global variable
# inside of a function:

def f():
    a = 1
    print(a)

a = 0
print(a)
f()
print(a)
''',
    'expected_output': """0
1
0
""",
    "allfine": """This program will print you the numbers 1 and 0. 
    Despite the fact that the value of the variable <code>a</code> 
    changed inside the function, outside the function it's still
     the same! There are two different variables <code>a</code>
existing simultaneously in the program: the global <code>a</code>
and the local <code>a</code>.

     This behavior is implemented in order to &laquo;protect&raquo; 
     global variables from unexptected changes inside functions. 
     For example, if the function is called from inside the loop, the loop variable
      <code>i</code> should be protected from changes inside the function.""",
},



{     "header": "Local and global variables: hey",
"text": """
If you haven't understood the last explanation, take a look at the
 following code and think about how it worked, if
  the function could change the value of the global loop variable <code>i</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

for i in range(1, 6):
    print(factorial(i), ' = ', i, '!', sep='')

# If the global variable <code>i</code> is changed 
# inside the function, we would get this:
# 1 = 5!
# 2 = 5!
# 6 = 5!
# 24 = 5!
# 120 = 5!
''',
    "allfine": "So, if some variable is modified inside a function, that variable becomes a local variable, and its modification will not change a global variable with the same name.",
},



{     "header": "Local and global variables: hey",
"text": """
More formally: Python considers a variable local to the function, if in the code of this function
there is at least one instruction that modifies the value of the variable. Then that 
variable also cannot be used prior to initialization. Instructions that 
modify the value of a variable are operators <code>=</code>, <code>+=</code>,
 and usage of the variable as a loop <code>for</code> parameter.
Even if the variable-changing statement
is never executed, the variable is still local. Look at the example.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def f():
    print(a)
    if False:
        a = 0

a = 1
f()
''',
    "allfine": """An error occurs: <code>UnboundLocalError</code>.
    Namely, since the function contains the command which modifies the variable <code>a</code>, 
    in the function <code>f()</code> the identifier
    <code>a</code> becomes a local variable. Although the modifying instruction will 
    never be executed, the interpreter has no way to check it. Therefore,
     when you try to print the variable <code>a</code>, you use an uninitialized yet local variable.
     Python prohibits that.""",
},
 

{     "header": "You can go global",
"text": """
If you want a function to be able to change some global variable, you must declare this variable as a global
inside the function using the keyword <code>global</code>.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def f():
    global a
    a = 1
    print(a)

a = 0
print(a)
f()
print(a)
''',
    "allfine": """This example will print the output of <code>0 1 1</code>, 
    because the variable <code>a</code> is declared as global, and changing
     it inside the function causes the change of it globally. 

     However, it is better not to modify values of global variables inside a function.
      If your function must change some variable, let it <i>return</i> this 
      value and call the function with passing that variable as an input. 
      If you follow these rules, the functions' logic works independent of
       the outer code logic, and thus such functions can be easily copied from
        one program to another, saving your time.""",
},




{     "header": "You can make me global",
"text": """
For example, suppose your program should calculate the factorial of the given number that you want to save in the variable <code>f</code>.
Here's how you <u>should not</u> do it.


""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
def factorial(n):
    global f
    res = 1
    for i in range(2, n + 1):
        res *= i
    f = res

n = int(input())
factorial(n)
print(f)
# doing other stuff with variable f
''',
"input_data": '''
5
''',
    'expected_output': '120',
    "allfine": """This is the example of <u>bad</u> code, because 
    it's hard to reuse the function <code>factorial()</code>. 
    If tomorrow you need another program to use the function 
    &quot;factorial&quot;, you will not be able to just copy
     this function from here and paste in your new program. 
     You will have to ensure that that program doesn't contain the variable <code>f</code>.

Even worse, whenever you make other calls to <code>factorial()</code> from your program, 
you need to make sure that there's no variable called <code>f</code>
defined for other needs and storing the valuable data.
     """,
},




{     "header": "Global",
"text": """
It is much better to rewrite this example as follows.
""",
    "instructions": 'Click "Run" to see what happens in output!',
    "program": '''
# the chunk of code that can be copied from program to program
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
# end of the chunk

n = int(input())
f = factorial(n)
print(f)
# doing other stuff with variable f
''',
"input_data": '''
5
''',
    'expected_output': '120',
    "allfine": """This function is now ready to be called from different parts of
our program with ease. It's also ready to be copy-pasted to your other program.
    """,
},


{     "header": "Do not hesitate to return a lot",
"text": """
It is useful to say that functions can return more than one value. Here's the example of returning a <i>list</i> of two or more values: <code>return [a, b]</code>

You can call the function of such list and use it in multiple assignment: <code>n, m = f(a, b)</code>.
""",
    "instructions": 'Actually, call it. :) Run the code!',
    "program": '''
a = input()
b = input()

def f(a,b):
    return [a + "th", b + "th"]

n, m = f(a, b)
print(n)
print(m)
''',
"input_data": '''
All work and no play
All jump and hard pray
'''
,
    'expected_output': """
All work and no playth
All jump and hard prayth
""",

},


 {     "header": "Recursion: example",
"text": """
As we saw above, a function can call another function. But a function can also call itself! 

To illustrate it, consider the example of the factorial-computing function. It is well known that 0!=1, 1!=1. 
How to calculate the value of n! for large n? If we were able to calculate the value of (n-1)!,
then we easily compute n!, since n!=n&sdot;(n-1)!. But how to compute (n-1)!? If
we have calculated (n-2)!, then (n-1)!=(n-1)&sdot;(n-2)!. How to calculate (n-2)!? 
If... In the end, we get to 0!, which is equal to 1. Thus, to calculate the factorial
we can use the value of the factorial for a smaller integer. Look at the code.
""",
    "instructions": 'In the visualizer, press "Step by step" and run the program.',
    "program": '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  
''',
'hint': '''
''',
    'expected_output': '120',
    "allfine": "And now we want to explain one more time what is going on.",
    'highlight': "$('.visualizer_explain_mode').addClass('snakify-blinking');",
},


{     "header": "Recursion: theory",
"text": """
The situation when function calls itself is called <em>recursion</em>, and such function is called <em>recursive</em>.

Recursive functions are powerful mechanism in programming. Unfortunately, 
they are not always effective and often lead to mistakes. 
The most common error is <em>infinite recursion</em>, when 
the chain of function calls never ends (well, actually, it 
ends when you run out of free memory in your computer). 
An example of infinite recursion:
<pre>def f():
    return f()</pre>

The two most common reasons causing infinite recursion:

<ol type=1 start=1> 
<li>Incorrect stopping condition. For example, if in the factorial-calculating program we forget to put the check <code>if n == 0</code>, then <code>factorial(0)</code> will call <code>factorial(-1)</code>,
that will call <code>factorial(-2)</code>, etc. 
<li>Recursive call with incorrect parameters. For example, if the function <code>factorial(n)</code> calls the function <code>factorial(n)</code>, we will also obtain an infinite chain of calls.
</ol> 

Therefore, when coding a recursive function, it is first necessary to ensure it will reach its stopping conditions &mdash;
to think why your recursion will ever end.
""",
    "instructions": 'In the visualizer, press "Step by step" and run the program.',
    "program": '''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))   
''',
'tasks': [
    {
        "instruction": 'Use the visualizer. Press "Step by step" and run the program. ',
        'expected_output': '120',
    },
    {
        "instruction": 'Modify the program to calculate so-called <a href="https://en.wikipedia.org/wiki/Double_factorial">double factorial</a>. Define <code>double_factorial</code> function for that. Print <code>double_factorial(5)</code>.',
        'expected_output': '15',
    },
],
'hint': '''
As <code>double_factorial</code> of <code>n</code> is n!! = n (n-2) (n-4) ... 2 in even case and  n!! = n (n-2) (n-4) ... 1 in odd case, we have to add the elif statement: <code>elif n == 1:
                             return 1</code>

And of course you have to follow the definition of double factorial: it is like ordinary factorial but skipping every other element, <code>double_factorial (n) = n * double_factorial (n-2)</code>, so your function must <b>return</b> <code>n * factorial(n - 2)</code>.
''',
    "allfine": "Congratulations! You've passed the functions level!",
},

]
