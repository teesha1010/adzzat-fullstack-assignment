
import re

def register_user(email, users):

    if not isinstance(email, str):
        return {
            "success": False,
            "message": "Invalid email"
        }

    email = email.strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(pattern, email):
        return {
            "success": False,
            "message": "Invalid email"
        }

    existing_emails = [
        user.lower() for user in users
    ]

    if email.lower() in existing_emails:
        return {
            "success": False,
            "message": "Email already registered"
        }

    users.append(email)

    return {
        "success": True,
        "message": "User registered successfully"
    }
