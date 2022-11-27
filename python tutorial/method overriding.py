class A:
    def sound(self):
        print("Hi")
class B(A):      #class B ko Class A mai inherit kia h 
    def sound(self):
        print("By")

obj1= B()    #overriding concept applied
obj1.sound()
