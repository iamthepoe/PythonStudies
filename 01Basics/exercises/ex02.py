name = input("Insert your name: ")
len = len(name);

if(len<=4):
    print("you have a small name")
elif(len==5 or len==6):
    print("you have a normal name")
else:
    print("you have a big name")


