str1 = "Raj Karan"
str2 = " Chauhan"
str3 = "Raj"

print(str1[0])  #R
print(str1[0:3]) #Raj

print(str1 + str2) #Raj Karan Chauhan

print(str3 in str1) #True
print(str3 in str2) #False

var=str1.split(" ")
print(var) #['Raj', 'Karan']
print(var[0]) #Raj


str4=" great "   #Trim
print(str4.strip()) # it will trim white space from left and right 
print(str4.lstrip()) # left white space strip
print(str4.rstrip()) # right white space strip