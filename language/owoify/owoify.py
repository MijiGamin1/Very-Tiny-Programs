from tkinter import Tk
final = ""
r = Tk()
ans = str(input("Enter your text:\n"))
anslist = []
for x in range(len(ans)):
    anslist.append(ans[x])
for x in range(len(anslist)):
    if anslist[x] == "l" or anslist[x] == "r":
        anslist[x] = "w"
    if anslist[x] == "L" or anslist[x] == "R":
        anslist[x] = "W"
    final = final + anslist[x]
print(final)
r.withdraw()
r.clipboard_clear()
r.clipboard_append(final)
r.update()
r.destroy()
