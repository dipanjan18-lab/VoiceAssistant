class MyClassA:
    def method_a(self):
        print("This is method A from MyClassA")

class MyClassB:
    def method_b(self):
        print("This is method B from MyClassB")

        # Creating an instance of MyClassA
        my_class_a_instance = MyClassA()

        # Calling the method_a from MyClassA using the instance
        my_class_a_instance.method_a()
        # now = my_class_a_instance.method_a()
        # print(now)
        obj_b = MyClassB()
        obj_b.method_b()

# if __name__ == "__main__":
MyClassB.method_b()