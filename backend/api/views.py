from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

TASKS = [
    {
        "id": 1,
        "title": "Fix Python Calculator",
        "type": "Language-driven",
        "difficulty": "Easy",
        "language": "Python",
        "description": "Fix the calculator division operation.",
        "statement": (
            "The calculator produces incorrect decimal "
            "division results and does not handle division "
            "by zero correctly. Fix the functionality while "
            "keeping the existing operations working."
        ),
        "environment": [
            "Python 3.11",
            "Ubuntu Linux",
            "Pytest"
        ],
    },
    {
        "id": 2,
        "title": "Improve User Registration",
        "type": "Outcome-driven",
        "difficulty": "Medium",
        "language": "Python",
        "description": "Improve the user registration system.",
        "statement": (
            "Improve registration so that valid emails are "
            "accepted, invalid emails are rejected, duplicate "
            "emails are prevented and email comparisons are "
            "case-insensitive."
        ),
        "environment": [
            "Python 3.11",
            "Ubuntu Linux",
            "Pytest"
        ],
    }
]

@api_view(["GET"])
def task_list(request):
    return Response(TASKS)

@api_view(["GET"])
def task_detail(request, task_id):
    for task in TASKS:
        if task["id"] == task_id:
            return Response(task)

    return Response(
        {"error": "Task not found"},
        status=404
    )