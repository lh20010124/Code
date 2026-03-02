class Person:
    def __call__(self, name):
        print("__call__" + "Hello " + name)

    def hello(selfself, name):
        print("Hello " + name)

Person = Person()
Person("zhangsan")
Person.hello("lisi")