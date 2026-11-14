# 07 - Generators and yield

# A normal function returns a result.
# A generator yields values one at a time.

def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for value in count_up_to(5):
    print(value)

# Generator expression: similar to a list comprehension,
# but values are produced lazily.
squares = (number * number for number in range(1, 6))
print("Squares:", list(squares))

# Example: read a large file one line at a time
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")

# Uncomment after creating sample.txt in this folder:
# for line in read_lines("sample.txt"):
#     print(line)
