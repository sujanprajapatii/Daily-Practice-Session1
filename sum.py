#Lambda function sample
a = int(input("Enter any 1st no:"))
b = int(input("Enter any 2nd no:"))
sum = lambda x,y: x + y
c = sum(a,b)
print(c)