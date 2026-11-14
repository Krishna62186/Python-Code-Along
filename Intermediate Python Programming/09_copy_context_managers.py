# 09 - Shallow Copy, Deep Copy, and Context Managers

import copy

original = [[1, 2], [3, 4]]

# Shallow copy: creates a new outer list, but nested lists are shared.
shallow = copy.copy(original)

# Deep copy: recursively copies nested objects too.
deep = copy.deepcopy(original)

original[0].append(99)

print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)

# Context manager: 'with' manages setup and cleanup automatically.
# The file is closed automatically when the block ends.
with open("context_demo.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python context managers!")

with open("context_demo.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile content:", content)

# A custom context manager using a class
class SimpleContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("Leaving the context")
        return False  # Do not suppress exceptions

with SimpleContext():
    print("Inside the context")
