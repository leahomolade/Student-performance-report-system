import random
import time
from functools import wraps

#Decorator: log_and_retry
def log_and_retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, n + 1):
                print(f"Calling {func.__name__}... Attempt {attempt}")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}")
                    if attempt == n:
                        print(f"Failed after {n} attempts.")
                    else:
                        time.sleep(1)
        return wrapper
    return decorator

#Generator: get_scores
def get_scores(students):
    for student in students:
        for score in student["scores"]:
            yield student["name"], score

#Recursive function: average
def average(scores):
    if not scores:
        return 0
    if len(scores) == 1:
        return scores[0]
    return (scores[0] + (len(scores) - 1) * average(scores[1:])) / len(scores)

#Function with decorator
@log_and_retry(3)
def generate_report(students):
    if random.random() < 0.3:  # simulate random failure
        raise ValueError("Random failure occurred!")
    
    print("\nStudent Performance Report")
    print("-" * 30)
    
    for student in students:
        avg = average(student["scores"])
        print(f"{student['name']}: Average Score = {avg:.2f}")

#Sample student list
students = [
    {"name": "Leah", "scores": [70, 80, 90]},
    {"name": "Chloae", "scores": [60, 75, 85]},
    {"name": "Charlie", "scores": [88, 92, 79]},
    {"name": "Diana", "scores": [95, 85, 87]},
    {"name": "Ethan", "scores": [55, 65, 70]},
    {"name": "Fiona", "scores": [100, 90, 95]},
    {"name": "George", "scores": [77, 84, 82]},
]

# Run report
generate_report(students)

# Optional: see scores yielded one by one
print("\nYielded Scores:")
for name, score in get_scores(students):
    print(f"{name}: {score}")