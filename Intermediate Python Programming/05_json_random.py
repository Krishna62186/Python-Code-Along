# 05 - JSON and Random Module

import json
import random
from pathlib import Path

# Python dictionary -> JSON text
student = {
    "name": "Asha",
    "age": 21,
    "skills": ["Python", "SQL", "Machine Learning"]
}

json_text = json.dumps(student, indent=4)
print("JSON text:\n", json_text)

# JSON text -> Python dictionary
loaded_student = json.loads(json_text)
print("Student name:", loaded_student["name"])

# Save JSON to a file beside this script
output_path = Path(__file__).with_name("student.json")
with output_path.open("w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

# Read JSON back from the file
with output_path.open("r", encoding="utf-8") as file:
    data = json.load(file)
print("Read from file:", data)

# Random values
print("\nRandom integer:", random.randint(1, 10))
print("Random choice:", random.choice(["Python", "Java", "C++"]))
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)
