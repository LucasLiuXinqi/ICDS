class Student:
    def __init__(self, x, y, z):
        self.name = x   #定义
        self.age = y
        self.major = z
        self.nameage = x + ' ' + y  #可以拼接

    def __str__(self):
        return self.name + self.age + self.major
        #内建的字符串


    def __len__(self):
        return len(self.nameage)

    def __add__(self, other):
        Student.name = self.name + other.name
        return Student


class Teacher(Student): #可继承
    def __init__(self, name,x,y,z):
        super(Teacher, self).__init__(x,y,z)
    #通过继承可以进行差别化修改


















Lucas = Student('Lucas', '18', 'CS')
Kyle = Student('Kyle', '18', 'Econ')

print(Lucas.name)
print(Lucas.age)
print(Lucas.major)
print(Lucas.nameage)
print(Lucas)
print(len(Lucas))
c = Lucas + Kyle
print(c.name)