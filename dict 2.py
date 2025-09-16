d={}
n=int(input("enter a a number of key value pairs"))
for i in range(n):
    key=input("enter a key:")
    value=input("enter a value:")
    d[key]=value
    print("the dictionary is",d)