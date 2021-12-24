***SCINOTE-CONVERT***

scinote-convert is a Python program that converts integers in scientific notation (x * 10^y)

So, with this program, I want to turn integer input from the console into scientific notation. I believe it's a pretty basic program for some, but it rubbed my braincells and tested my python knowledge during this weekend.
The program still has some bugs I couldn't solve, so I hope you guys can. (I use sublimeREPL for the input part)

The main bug that appears is when I input a num with a bigalg on the last algorism: it spits me this:


```
    if alglog[int(alg)-1] == False:
IndexError: list index out of range
```

Why is this happening?

