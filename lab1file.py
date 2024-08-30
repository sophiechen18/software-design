import math
I = 7
R = 1.2
D = int(input("Enter the amount of Days that the infection has occured: "))
pop = 39740
x = 0
tui = 0



II = I


sum = 0

sum2 = I
sum3=0
    

for i in range(D):
    
    sum = I * R
    sum2 = sum2 + sum
    I = sum


    

    if (i == 14):
        tui = 9972 * math.trunc(sum2) 
        x=1
        sum3=sum2
        



sum2 = math.trunc(sum2)   
sum3 = math.trunc(sum3)
if x == 1:
    
    print ("Total Infected {}".format( sum2))
    print ("Total Infected at drop period (14 days) {}".format(sum3))
    print ("Tution {}".format(tui))
    print ("Precent infected {}".format(math.trunc((sum2/pop) * 100)))

else:
    print ("Total Infected {}".format( sum2))
    print ("Tution  {}".format( sum2 * 9972))
    print ("Precent infected {}".format(math.trunc((sum2/pop) * 100)))

S = int(input("Press 1 to continue or any other number to stop again"))


while(S == 1):
    sum = 0

    sum2 = II
    I = II
    D = int(input("Enter the amount of Days that the infection has occured: "))
    
    for i in range(D):
    
        sum = I * R
        sum2 = sum2 + sum
        I = sum


    

        if (i == 14):
            tui = 9972 * math.trunc(sum2) 
            x=1
            sum3=sum2
        



    sum2 = math.trunc(sum2)
    sum3 = math.trunc(sum3) 
    if x == 1:
    
        print ("Total Infected {}".format( sum2))
        print ("Total Infected at drop period (14 days) {}".format(sum3))
        print ("Tution {}".format(tui))
        print ("Precent infected {}".format(math.trunc((sum2/pop) * 100)))
    
    else:
    
        print ("Total Infected {}".format( sum2))
        print ("Tution  {}".format( sum2 * 9972))
        print ("Precent infected {}".format(math.trunc((sum2/pop) * 100)))
    
    S = int(input("Press 1 to continue or any other number to stop again"))
