file=open("text.txt")
# print(file.read())
# print(file.read(5)) #if we give some number then it will read that character
# we can read file line by line
# print(file.readline())
# print(file.readline())
# print(file.readline())

# read all the lines in text file line by line
# line=file.readline()
# while line !="":
#     print(line)
#     line=file.readline()

# second method read all the lines in text file line by line
for line in file.readlines():
    print(line)

file.close()