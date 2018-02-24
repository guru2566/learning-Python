def f(a,b,c):
    if(a<b and a<c):
        return a
    elif(b<c and b<a):
        return b
    else:
        return c

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))

print(f(x,y,z),"is the lowest")

      
