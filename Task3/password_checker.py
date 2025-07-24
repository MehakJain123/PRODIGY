import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Criteria 2: Lowercase letters
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add lowercase letters.")

    # Criteria 3: Uppercase letters
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add uppercase letters.")

    # Criteria 4: Numbers
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add numbers.")

    # Criteria 5: Special characters
    if re.search(r"[@#$%^&+=!*/?]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add special characters (e.g., @, #, !).")

    # Final strength decision
    if strength_points == 5:
        strength = "Strong 💪"
    elif strength_points >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak 🚫"

    return strength, feedback

# Get input from user
password = input("Enter your password to check: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)
if feedback:
    print("Suggestions to improve:")
    for f in feedback:
        print("-", f)
