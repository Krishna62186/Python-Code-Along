# 03 - Lambda, *args, and **kwargs

# Lambda: a short anonymous function
square = lambda number: number * number
print("Square:", square(6))

students = [("Asha", 91), ("Ravi", 78), ("Mina", 86)]
students_sorted = sorted(students, key=lambda student: student[1], reverse=True)
print("Sorted by marks:", students_sorted)

# *args collects extra positional arguments into a tuple
def add_all(*args):
    return sum(args)

print("Sum:", add_all(10, 20, 30, 40))

# **kwargs collects extra named arguments into a dictionary
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="Asha", course="CSE", year=4)

# Combine normal parameters, *args, and **kwargs
def describe(title, *args, **kwargs):
    print("\nTitle:", title)
    print("Extra values:", args)
    print("Details:", kwargs)

describe("Student profile", "Python", "ML", age=21, city="Chennai")
