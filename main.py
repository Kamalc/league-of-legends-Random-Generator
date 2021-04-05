from Search_Google import Search_Save

mylist = []
with open("Top_List.txt", "r") as a_file:
    for line in a_file:
        stripped_line = line.strip()
        mylist.append(stripped_line)
        # print(stripped_line)

idx = 2
sz = len(mylist)

while idx < sz:
    print(mylist[idx])
    Search_Save(mylist[idx], 'Ignore_Area/Images')
    idx += 8


