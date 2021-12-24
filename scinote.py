
###So, with this program, I want to turn integer input from the console into scientific notation. I believe it's a pretty basic program for some, but it rubbed my braincells and tested my python knowledge during this weekend.
###The program still has some bugs I couldn't solve, so I hope uou guys can. (btw I use sublimeREPL for the input part)

#The main bug that appears is when I input a num with a bigalg on the last algorism: it spits me this:

# Traceback (most recent call last):
#   File "C:\Users\...\Python\scinote.py", line 62, in <module>
#     scinoteConvert(input_num)
#   File "C:\Users\...\scinote.py", line 47, in __init__
#     if alglog[int(alg)-1] == False:
# IndexError: list index out of range

class scinoteConvert:
    #Should I put all the code on __init__()? Is there performenance inefficiency in doing that?

    def __init__(self, num):

        #Define the algorism lists

        #alglist: Converts num's algs into a list
        alglist = []

        #alglog: Defines what algs are > 0 with bools
        alglog = []

        #bigalgslist: Puts all the bigalgs into a list
        bigalgslist = []

        #bigalgs: integer that indicated the quantity of algs > 0
        bigalgs = 0

        #Convert the input to a string

        num = str(num)

        #Assigning base to a string data type
        base = ''

        #Creating a list of algs

        for alg in num:
            alglist.append(alg)

        #Defining what algs are > 1 (I'll call them bigalgs)

        for alg in alglist:
            
            if int(alg) < 1:
                alglog.append(True)
            else:
                alglog.append(False)
                bigalgs += 1


            #creating a list of all the bigalgs

            if alglog[int(alg)-1] == False:
                bigalgslist.append(int(alg))

        #creating the first factor of the scientific notation (1st bigalg, all other bigalgs)

        factor_1 = str(bigalgslist[0:1]) + ',' + str(bigalgslist[1:])

        #creating the second factor of the scientific notation (10)
        factor_2 = 10

        #creating the exponent of the second factor (number of algorisms in the number - 1)

        exp = str(len(str(num)) - 1)

        #Printing the output into the console (Question: Because base comes from lists, in the output, base is displayed within square brackets. Is there a way to remove all brackets from a string?)
        print('Output: ' + base + ' * ' + factor_2 + '^' + exp)

        #Printing all the variables for debug:
        #print(alglog, alglist, bigalgslist, bigalgs)

#Getting input

input_num = int(input('Insert num: '))

#Error dumping

if input_num < 1:
    exit('Error! Cannot calculate negative values!')

#Converting input into scientific notation

scinoteConvert(input_num)
