def f(n,a=[]):
    highest1=a[0]
    for i in a:
        if highest1<i:
            highest1=i
    return highest1

a=[]
n=int(input("Enter the Limits: "))
print("Enter the Elements")
for i in range(n):
    a.append(int(input()))
print(f(n,a),"is highest")


