obj=[1,2,3,4,5]
for i in obj:
    print(i**2) # square of number

# range use
print(" range use")
for x in range(5):
    print(x)

# Sum of natural numbers n
print("Sum of natural numbers n")
n=5
sum=0
for i in range(2,n):  #when ever we use range then range(5) means 0,1,2,3,4 and range(2,5) is 2,3,4
    # print(i)
    sum +=i
print(sum)

# Setup of 2
print("Stepup of 2")
for k in range(1,11,2):
    print(k)