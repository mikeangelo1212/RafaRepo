l =["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","X","Y","Z"]
for i in l:
    f=0
    if f%3 == 0:
        l.remove(i)
        f = f+1
print(l)