#this is a program to run a pattern giveen below:-
#input n = 4
# output : A
#          b C
#          D e F
#          g H i J

n = int(input("Enter n \n"))
j=0
for i in range(n): 
    count=0
    while j<=28 :
        a= chr(97+j)
        if(j%2==0):
            a=a.upper()
        print(a, end=" ")
        j+=1
        if count >= i :
             print()
             break
        else :
            count+=1
