class Student():
    sum = 0
    # name = ''
    # age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sum = self.sum + 1
        # print(name)
        # print(age)
        # print(self.__class__.sum)

    @classmethod    #必须加上装饰器，用来操作类变量
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

student1 = Student('tom', 18)
Student.plus_sum()
Student.plus_sum()
student1.plus_sum()