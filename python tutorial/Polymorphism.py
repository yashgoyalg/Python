class cat:
    def sound(self):
        print("Meow")
class dog:
    def sound(self):
        print("Bow bow")
def makesound(animalsound):
    animalsound.sound()

obj1= cat()
obj2=dog()
makesound(obj1)
makesound(obj2)