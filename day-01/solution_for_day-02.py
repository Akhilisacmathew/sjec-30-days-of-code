num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
for i in range(num1,num2+1,1):
    if(i%3==0):
        print("foo")
    elif(i%3!=0 and i%2==0):
        print("bar")
    elif(i%3!=0 and i%2!=0):
        print("baz")