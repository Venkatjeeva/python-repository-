f1=open("file.txt","r")
l=f1.readlines()
while(l!=''):
    print(l)
    l=f1.readline()
f1.close()