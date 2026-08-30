a=0
tf=0
tt=0
ts=0
to=0

while True:
   
    while True:
        print("Choose the category of the expense")
        print("Enetr F for food")
        print("Enter T for travel")
        print("Enter S for shopping")
        print("Enter O for other")
        c=(input("Enter the category"))
        if c=="F":
            a=int(input("Enter the amount"))
            tf=tf+a
        if c =="T":                          # also fix lowercase "t" → "T"
            a=int(input("Enter the amount"))
            tt=tt+a
        if c=="S":
            a=int(input("Enter the amount"))
            ts=ts+a
        if c =="O":
            a=int(input("Enter tha amount"))
            to=to+a
        more=input("Add another expense? (y/n): ")
        if more!="y":
            break
    total=tf+tt+ts+to
    print("Total Expenditue in Food : ", tf)
    print("Total expenditure in Travel : " , tt)
    print("Total Expenditure in shopping : " ,ts )
    print("Total Expentidure in Other : " ,to)
    print ("Total Expenditure : " , total)
    if tf>=tt and tf>=ts and tf>=to:
            print("Most expensive category is food")
    if tt>=tf and tt>=ts and tt>=to:
            print("Most expensive category is travel")
    if ts>=tf and ts>=tt and ts>=to:
            print("Most expensive category is shopping")
    if to>=tt and to>=tf and to>=ts:
            print("Most expensive category is other")
    again=input("Do you want to continue? (y/n): ")
    if again!="y":
        break
