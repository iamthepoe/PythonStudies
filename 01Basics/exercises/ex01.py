number = input("Insert a integer number: ");
try:
    number = int(number)
    if(number%2==0):
        print(f"{number} is a even");
    else:
        print(f"${number} is a odd");
except:
    print(f"{number} is not a integer");

