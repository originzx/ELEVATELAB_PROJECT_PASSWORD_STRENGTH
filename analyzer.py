import re

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 25
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add symbols.")

    if password.lower() in ["password", "123456", "qwerty"]:
        score = 5
        feedback = ["Avoid common passwords."]

    return score, feedback
