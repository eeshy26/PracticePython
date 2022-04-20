class employee1:

    def intro(self):
        print("Lots of people like coding.")

    def code(self):
        print("Some like coding but some do not")

class employee2(employee1):

    def code(self):
        print("I like coding")

class employee3(employee1):

    def code(self):
        print("I don't like coding")

obj_employee1=employee1()
obj_employee2=employee2()
obj_employee3=employee3()

obj_employee1.intro()
obj_employee1.code()

obj_employee2.intro()
obj_employee2.code()

obj_employee3.intro()
obj_employee3.code()
