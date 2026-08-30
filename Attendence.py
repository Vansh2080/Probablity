attended = int(input("Enter classes attended: "))
total = int(input("Enter total number of classes: "))
target = int(input("Enter your target attendance percentage: "))
percentage = (attended/total) * 100
print("Your current attendance is:", percentage, "%")
required = (target/100) * total
required = int(required)
if required < (target/100) * total:
    required = required + 1

more = required - attended
rem = total - attended

if more <= 0:
    print("You have already reached your target.")

if more <= rem:
    print("You need to attend", more, "more classes.")

else:
    print("You cannot reach your target attendance.")