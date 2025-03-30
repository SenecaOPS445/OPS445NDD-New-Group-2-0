#!/usr/bin/env python3
# Student ID: [your_seneca_id] (Group Member 2)

import string   # For string punctuation and letter checks

def check_password(password, verbose=False):
    """
    Check the security of a password.
    The password must:
      - Be at least 8 characters long.
      - Contain at least one lowercase letter.
      - Contain at least one uppercase letter.
      - Contain at least one digit.
      - Contain at least one special character.
    Returns a string indicating whether the password is strong or listing its issues.
    """
    issues = []      # List to store any password problems

    if len(password) < 8:   # Check if password is too short
        issues.append("Password must be at least 8 characters long.")

    if not any(c.islower() for c in password):  # Check for lowercase letters
        issues.append("Password must include at least one lowercase letter.")

    if not any(c.isupper() for c in password):  # Check for uppercase letter
        issues.append("Password must include at least one uppercase letter.")

    if not any(c.isdigit() for c in password):  # Check for numbers
        issues.append("Password must include at least one digit.")

    if not any(c in string.punctuation for c in password):  # Check for special characters
        issues.append("Password must include at least one special character.")
    
    if verbose:     # If user wants detailed output
        print("Password analysis:")
        print("Length:", len(password))     # Show password length
        print("Contains lowercase:", any(c.islower() for c in password))    # Show lowercase result
        print("Contains uppercase:", any(c.isupper() for c in password))    # Show uppercase result
        print("Contains digit:", any(c.isdigit() for c in password))        # Show digits result
        print("Contains special character:", any(c in string.punctuation for c in password))    # Show special chars result
    
    if issues:      # If there are any issues
        return "Weak password. Issues:\n" + "\n".join(issues)   # Return all issues
    else:       # No issues found
        return "Strong password."   # Password is strong
