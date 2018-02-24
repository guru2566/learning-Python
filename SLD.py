def getcs():
    s=input("severname: ")
    n=input("dbname: ")
    u=input("usr: ")
    p=input("mypass: ")
    cs = "Server="+s+";"+"dbname="+n+";"+"usr="+u+";"+"pass="+p+";"

    return cs


print(getcs())
