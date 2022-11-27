#Pattern printing 

a= int(input("Enter number of lines you want to print: "))
b= bool(int(input("Please enter 1 for true and  0 for false: ")))

def star(a,b):
    if b==True:
        c=1
        while c<=a:
            print(c*"*")
            c= c+1
    else:
        while a>0:
            print(a* "*")
            a=a-1
star(a,b)