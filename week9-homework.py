### QUESTION 1
## create class Student, which holds parameters name, age and grade

class Student:
    def __init__(self, first_name, age, grade):
        self.first_name = first_name
        self.age = age
        self.grade = grade

students = []
students.append(Student('Raj', 16, "11th"))
students.append(Student('Joe', 17, "11th"))

for student in students:
    print(student.first_name, student.age, student.grade)

### QUESTION 2
## create class Staff, which holds parameters name, department, role, salary. create class Teacher, which supersets Staff, and holds additional parameter age
print('')

class Staff:
    def __init__(self, first_name, department, role, salary):
        self.first_name = first_name
        self.department = department
        self.role = role
        self.salary = salary

class Teacher(Staff):
    def __init__(self, first_name, department, role, salary, age):
        super().__init__(first_name, department, role, salary)
        self.age = age

teachers = []
teachers.append(Teacher('Raj', 'Science', 'Teacher', 40000, 20))
teachers.append(Teacher('Joe', 'Science', 'Teacher', 70000, 58))

for teacher in teachers:
    print(teacher.first_name, teacher.department, teacher.role, teacher.salary, teacher.age)

### QUESTION 3
## create class Square, and define two methods that return teh square area and perimeter given the length of a side
print('')

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def square_area(self):
        return self.side_length**2

    def perimeter(self):
        return self.side_length*4

squares = []
squares.append(Square(20))
squares.append(Square(50))

for square in squares:
    print(f"Square with side length {square.side_length} will have:\n  Area: {square.square_area()}\n  Perimeter: {square.perimeter()}")