def dict1(d):
     z="";
     for k,v in d.items():
          z+=k+"="+v+";"
     z=z[:-1]
     return z;

d={}
for i in range(2):
     y=input().split()
     d[y[0]]=y[1]
print(dict1(d))
