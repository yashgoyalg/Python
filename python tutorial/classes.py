#classes - Template
#object- instance of the class (class dwara prapt kia ggya object)
#DRY - Do not repeat Yoursself 


# class student:
#     pass

# harry = student()
# larry = student()

# harry.std = 12
# harry.name = "harry"
# print(harry.std)

class student:
    no_of_leaves = 8
    def printdetails(self):
        return f"name is (self.name).selary is (self.salary) and role is (self.role)"

harry = student()
larry = student()

harry.name = "harry"
harry.salary = 50000
harry.role = "student"

larry.name = "harry"
larry.salary = 50000
larry.role = "student"

print(larry.printdetails())