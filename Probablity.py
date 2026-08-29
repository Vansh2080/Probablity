import random
c=int(input("Enter the number of time you want to flip the coin : "))
head=0
tail=0
for i in range(c):
    result=random.choice(["Head" , "Tail"])

    if result == "Head":
        head =head+1 
    else:
        tail=tail+1
print("Heads" , head)
print("Tails" , tail)
prbh=(head/c)*100
prbt=(tail/c)*100
thph=50
thpt=50
print("Experimental probablity of head is : " , prbh ,"%")
print("Theoritical probablity of head is : " , thph , "%")
print("Experimental probablity of tail is : " , prbt , "%")
print("Theoritical probablity of tail is : " , thpt , "%")
d=int(input("How many times a dice is to be thrown : "))
prbnum=0
num=int(input("Choose a number between 1 to 6 : "))
if (num>=1 and num<=6):
    for i in range(d):
        result=random.choice([1,2,3,4,5,6])
        if result == num:
            prbnum=prbnum+1
            prbd=(prbnum/d)*100
    thed=16.6
    print("Experimental value of getting the chosen number is: " , prbd , "%")
    print("Theoritical value of getting the chosen number is : ", thed , "%")
else: print("Wrong number")

