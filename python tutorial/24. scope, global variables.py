l = 10    #Global variable
def function1(n):
    #l= 20   #local variable
    global l  #Global keyward
    l = l+45
    print(l)
    print(n,"I have printed")
function1("this is me")
