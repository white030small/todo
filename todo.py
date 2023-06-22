list=[]
while TimeoutError:
    inform=input("")
    list.append(inform)
    if inform == "end":
        break
    elif inform == "del":
        ld=input()
        del list["ld"]
        continue
print(list)
con=input("continue???")#bug
if con == "yes":#bug
    continue#bug
elif con == "no":#bug
    break#bug