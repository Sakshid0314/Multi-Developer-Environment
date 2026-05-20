class Student:

    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)

student1 = Student("Rahul", "Python", 85)
student2 = Student("Anita", "Python", 92)

student1.display()
print("----------------")

student2.display()

students = ["Rahul", "Anita", "Kiran"]

print("Student List:")
for s in students:
    print(s)

print("Data Display Completed")