Development Notes – Adzzat Labs Assignment

1. Project Overview

This project was developed as part of the Adzzat Labs Full-Stack Software Engineer assignment.

The implementation includes two benchmark-style coding tasks, automated Pytest graders, Docker-based execution environments, a Django REST API and a Next.js frontend.

2. Implementation Details

Task 1: Python Calculator

Created a language-driven Python coding task.

Added starter code containing intentional implementation errors.

Developed automated tests for addition, subtraction, multiplication and division.

Added test cases for decimal division and division by zero.

Created a separate reference solution to demonstrate the expected behaviour.

Task 2: User Registration

Created an outcome-driven user registration task.

Added starter code with intentional validation issues.

Developed automated tests for valid and invalid email addresses.

Included duplicate email checks.

Added case-insensitive comparison and whitespace handling.

Backend

Implemented the backend using Django and Django REST Framework.

Created API endpoints to retrieve all tasks and individual task details.

Added task information including title, description, difficulty and environment.

Frontend

Implemented the frontend using Next.js and JavaScript.

Created a task listing interface.

Added task difficulty and category information.

Implemented a detailed task view.

Connected the frontend to the Django REST API.

Docker

Created Dockerfiles for both coding tasks.

Configured Python 3.11 environments.

Used Pytest to execute automated graders inside Docker containers.

3. Testing Performed

The following checks were performed during development:

Component

Check

Calculator grader

Executed using Pytest

Registration grader

Executed using Pytest

Calculator Docker image

Built and executed

Registration Docker image

Built and executed

Backend API

Verify task list and detail endpoints

Next.js frontend

Verify task listing and detail view

Calculator Grader Results

The original starter implementation produced:

4 tests passed.

2 tests failed.

The failed tests were:

Decimal division: returned an integer instead of a decimal result.

Division by zero: did not raise the expected exception.

These failures confirmed that the grader detects the intentional bugs in the starter implementation.

Note: Update the testing table with the actual results of every check before submission.

4. Issues Identified and Changes Made

Calculator

Issue: Integer division was used instead of normal division.

Change: The reference implementation uses / to support decimal results.

Issue: Division by zero returned an incorrect result.

Change: Added ZeroDivisionError handling.

Frontend

Change: Used Next.js instead of React with Vite to implement the frontend.

Docker

Issue: The original Docker image continued testing the starter implementation after creating a corrected reference solution.

Change: Created a separate Dockerfile for the calculator reference solution so the starter implementation remains unchanged.

5. Old code where errors occured 
### Task 1

```bash
 def register_user(email, users):

     users.append(email)

     return {
         "success": True,
       "message": "User registered successfully"
    } 
```
### Task 2

```bash
def divide(a, b):
    if b == 0:
        return 0
    return a // b
```


6. Grader Validation and Limitations

The graders were tested against the intentionally incorrect starter implementations to verify that they detect incorrect behaviour.

Reference implementations are maintained separately to demonstrate passing test cases.

The current Docker setup is intended as a local execution and testing environment. A production benchmark would require stronger isolation between the agent's writable workspace and hidden grader files.

7. AI Tools Used

ChatGPT was used for assistance with:

Understanding the assignment requirements.

Planning the project structure.

Designing coding tasks and test cases.

Docker setup and troubleshooting.

Backend and frontend implementation guidance.

Documentation preparation.

Generated code was reviewed and tested during development.

8. Future Improvements

Add more coding tasks with different difficulty levels.

Improve test coverage with additional edge cases.

Introduce stronger container isolation.

Keep hidden graders separate from agent-accessible files.

Add agent execution and result reporting.

Explore Harbor-compatible Docker image publishing.

Improve frontend task filtering and search.

9. Final Remarks

The project demonstrates a basic full-stack implementation combining coding-task design, automated testing, Docker execution, REST API development and a Next.js user interface.

The focus was on creating a clear, testable and maintainable project structure while documenting implementation decisions and limitations.