 
num = 15
n = input("enter value : ")
n=int(n)

i=0

while i<9 :
    if num == n :
        print("you won")
        break
    else:
        if num < n :
            n= input("false your number is greater than the solution try again")
            n=int(n)
            i+=1
        else:
            n= input("false your number id smaller than the solution try again") 
            n=int(n)
            i+=1

if (i==9 and n!=15)  :
    print("you lost")
if n==15:
    print("you won")