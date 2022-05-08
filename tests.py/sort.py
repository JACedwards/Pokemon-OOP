# def myFunc(e):
#   return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(reverse=True, key=myFunc)

# print(cars)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
x = sorted(student_tuples, key=lambda student: student[0])   # sort by age
print(x)

# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
