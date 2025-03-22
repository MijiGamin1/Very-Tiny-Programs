num = int(input("Enter your number here:\n"))
numlist = []
sortlist = []
sortnum = ""
xnum = ""
for x in range(num):
    xnum = x + 1
    if (num/xnum).is_integer():
        numlist.append(num/xnum)
for x in range(len(numlist)):
    sortlist.append(str(numlist[x]) + "," + str(numlist[len(numlist) - 1 - x]))
for x in range(len(sortlist)):
    print(sortlist[x])
    