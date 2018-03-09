r=int(input("Enter the number of elements of the series "))
n1=0
n2=1
i=2
if r<= 0:
	print("Enter a positive integer..")
elif r== 1:
	print("Fibonacci series up to",r,":")
	print(n1)
else:
	print("Fibonacci series up to",r,":")
	print(n1)
	print(n2)
	for i in range(r):
		n3=n1+n2
		print(n3)
		n1=n2
		n2=n3
		i=i+1
