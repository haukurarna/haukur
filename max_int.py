#Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
 
#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.

# Notandi setur inn tölu 
#forrit biður hann um að setja inn tölu þangað til hann setur inn neikvæða tölu.
#Ef talan sem sett er inn er stærri en talan sem áður var sett inn þá breytir hún gildinu
#
#
num_int = 0
max_int = 0
while num_int >=0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int 

# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
