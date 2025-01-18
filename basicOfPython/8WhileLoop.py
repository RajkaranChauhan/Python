it=4
while it>1:
    if it !=3:
        print(it)

    it=it-1
print("while execution done")

print("BREAK")
it=4
while it>1:
    if it ==3:
        break
    print(it)
    it=it-1
print("break execution done")

print("Continue")
it=4
while it>1:
    it = it - 1
    if it ==3:
        continue
    print(it)

print("Continue execution done")