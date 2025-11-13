import json
import os

DATA_PATH = "data/students.json"

def load_students():
    """Load students from JSON file."""
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as file:
        return json.load(file)

def save_students(students):
    """Save students to JSON file."""
    with open(DATA_PATH, "w") as file:
        json.dump(students, file, indent=4)
