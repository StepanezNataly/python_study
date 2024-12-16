grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

print(len(grades))
print(type(grades))

first_gpa = sum(grades[0]) / len(grades[0])
second_gpa = sum(grades[1]) / len(grades[1])
third_gpa = sum(grades[2]) / len(grades[2])
fourth_gpa = sum(grades[3]) / len(grades[3])
fifth_gpa = sum(grades[4]) / len(grades[4])
gpa_grades = [first_gpa, second_gpa, third_gpa, fourth_gpa, fifth_gpa]
print(gpa_grades)
print(len(students))
print(type(students))
students = list(students)
sort_students = sorted(students)
print(sort_students)

students_grades = dict(list(zip(sort_students, gpa_grades)))
print(students_grades)
