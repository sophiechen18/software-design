import math
I = 7
R = 1.2
D = int(input("Enter the amount of Days that the infection has occured: "))
x = 0
tui = 0
sum = I

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

while(S == 1):
    D = int(input("Enter the amount of Days that the infection has occured"))
    sum = I
    for i in range(D):
        sum = R * sum
        sum = math.trunc(sum)
    print (sum)
    S = int(input("Press 1 to continue or any other number to stop again"))