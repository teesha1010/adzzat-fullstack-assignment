
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from app import register_user

def test_valid_email():
    users = []

    result = register_user("test@gmail.com", users)

    assert result["success"] is True
    assert len(users) == 1

def test_invalid_email():
    users = []

    result = register_user("invalid-email", users)

    assert result["success"] is False
    assert len(users) == 0

def test_duplicate_email():
    users = ["test@gmail.com"]

    result = register_user("test@gmail.com", users)

    assert result["success"] is False
    assert len(users) == 1

def test_case_insensitive_duplicate():
    users = ["test@gmail.com"]

    result = register_user("TEST@gmail.com", users)

    assert result["success"] is False
    assert len(users) == 1

def test_email_whitespace():
    users = []

    result = register_user(" test@gmail.com ", users)

    assert result["success"] is True
    assert users[0] == "test@gmail.com"

def test_missing_email():
    users = []

    result = register_user("", users)

    assert result["success"] is False
    assert len(users) == 0