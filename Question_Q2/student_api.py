from fastapi import FastAPI
app = FastAPI()

students = [
    {
        "name": "Rahul",
        "score": 80
    },
    {
        "name": "Priya",
        "score": 90
    },
    {
        "name": "Amit",
        "score": 70
    },
    {
        "name": "Sneha",
        "score": 85
    }
]

@app.get("/students")
def get_students():
    return students