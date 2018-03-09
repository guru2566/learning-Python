n1=0
n2=1
i=2
print("Fibonacci series up to 20:")
print(n1)
print(n2)
for i in range(20):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    i=i+1
