class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying in grade {self.grade}.")


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching and his salary is {self.salary}$.")


student1 = Student("Andreas", 36, 10)
teacher1 = Teacher("Roman", 35, 6000)

student1.introduce()
student1.study()

teacher1.introduce()
teacher1.teach()
