import math
I = 7
R = 1.2
D = int(input("Enter the amount of Days that the infection has occured: "))

x = 0
tui = 0






sum = 0

sum2 = I
    

for i in range(D):
    
    sum = I * R
    sum2 = sum2 + sum
    I = sum


    

    if (i == 14):
        tui = 9972 * sum
        x=1



sum2 = math.trunc(sum2)   
if x == 1:
    math
    print (sum2)
    print (tui)

else:
    print (sum2)
    print (sum2 * 9972)

S = int(input("Press 1 to continue or any other number to stop again"))


while(S == 1):
    sum = I

    D = int(input("Enter the amount of Days that the infection has occured"))

    for i in range(D):
        
        sum = R * sum
        sum = math.trunc(sum)

        if (i == 14):
            tui = 9972 * sum
            x=1
    
    if x == 1:
        print (sum)
        print (tui)

    else:
        print (sum)
        print (sum * 9972)
    
    S = int(input("Press 1 to continue or any other number to stop again"))
