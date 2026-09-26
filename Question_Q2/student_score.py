import requests
import matplotlib.pyplot as plt


API_URL = "http://127.0.0.1:8000/students"


response = requests.get(API_URL)

print("Status code:", response.status_code)

data = response.json()

names = []
scores = []

for student in data:
    names.append(student["name"])
    scores.append(student["score"])

average_score = sum(scores)/len(scores)

print("\nStudent scores:")

for name, score in zip(names, scores):
    print(name, ":", score)

print("\nAverage score:", average_score)

plt.bar(names, scores)

plt.xlabel("Students")
plt.ylabel("Scores")

plt.title("Student Test Score")

plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("student_scores.png")

plt.show()