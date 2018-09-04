#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.

#Þessi algorithm gefur þér fyrstu n tölurnar í röðinni
#1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#
#byrjar á því að skilgreina n
#  semsagt summan af seinustu 3 stökum
# byrjar á tölunni 0
# tekur svo þá tölu og plúsar við hana summuna af seinustu 3 stökum 
# hækkar svo töluna þína um 1 og byrjar aftur 

n = int(input("Enter the length of the sequence: ")) # Do not change this line
stak1 = 3
stak2 = 2
stak3 = 1
sum_temp = 0 
count = 1

while count <= n:
    if count == 1:
        print(stak3)
    elif count == 2:
        print(stak2)
    
   
        
        
    
    else:
       
        print(stak1)
        sum_temp = stak1 + stak2 + stak3
        
        stak3 = stak2 
        stak2  = stak1
        
        stak1 = sum_temp


        

    count += 1

    
    

   
    
    