import random
from secrets import choice

random_number = random.randint(0,100)
print(random_number)
rand = random.random()*100
print(rand)

list=["starplus", "ABP","AajTak"]
choice = random.choice(list)
print(choice)