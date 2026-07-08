from student import Student
from CourseGroup import CourseGroup

student = Student("Анна", "Иван", 25, "Инженер по тестированию")
classmate1 = Student("Иван", "Петров", 27, "Инженер п тестированию")
classmate2 = Student("Мария", "Сидорова", 24, "Инженер по тестированию")
classmate3 = Student("Дмитрий", "Кузнецов", 26, "Инженер по тестированию")

cours_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(cours_group)


