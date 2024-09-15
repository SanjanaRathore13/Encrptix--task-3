def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        return "The Zero value is not allowed for the denomination"
    
cont = 1
while (cont!=0):
    print("\n")
    print("**** Calculator ****")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("\n")

    choice =int(input("Enter the choice (1-5):  "))

    if choice ==1:
        a=int(input("Enter the First Value:  "))
        b=int(input("Enter the Second Value:  "))
        print(add(a,b))
        cont=int(input("Do you want to continue ? Press 1 for Yes  and Press 0 for No:  " ))

    elif choice==2:
        a=int(input("Enter the First Value:  "))
        b=int(input("Enter the Second Value:  "))
        print(sub(a,b))
        cont=int(input("Do you want to continue ? Press 1 for Yes  and Press 0 for No:  " ))

    elif choice==3:
        a=int(input("Enter the First Value:  "))
        b=int(input("Enter the Second Value:  "))
        print(multi(a,b))
        cont=int(input("Do you want to continue ? Press 1 for Yes  and Press 0 for No:  " ))

    elif choice==4:
        a=int(input("Enter the First Value:  "))
        b=int(input("Enter the Second Value:  "))
        print(div(a,b))
        cont=int(input("Do you want to continue ? Press 1 for Yes  and Press 0 for No:  " ))

    elif choice==5:
        print("Thanyou !!!")
        exit(1)

    else:
        print("Invalid Choice !! Please select a Valid Operation")










