#!/usr/bin/env python3
# Student ID: sdaweng

import string   # importing string for punctuation and letter checks

def check_password(password, verbose=False):
    """
    Check the security of a password.
    For a password to be considered secure, it needs to:
      - Have 8 or more characters
      - Include at least one lowercase letter.
      - Include at least one uppercase letter.
      - Include at least one number.
      - Include at least one special character.
    Returns a message that either confirms the password is strong or lists the specific security issues found.
    """
    issues = []     #List to store any password problems

    if len(password) < 8: # Checks if password is short or have lesser than 8 characters
        issues.append("Password must be at least 8 characters long.")

    if not any(c.islower() for c in password): # Check users promt if there is a lowercase letter
        issues.append("Password must include at least one lowercase letter.")
    if not any(c.isupper() for c in password): # Check users prompt if there is a lowercase letter
        issues.append("Password must include at least one uppercase letter.")

    if not any(c.isdigit() for c in password): # Check users prompt if there is a number given
        issues.append("Password must include at least one digit.")

    if not any(c in string.punctuation for c in password): # Checks users prompt if there is a special character given
        issues.append("Password must include at least one special character.")

    if verbose: # If user wants detailed output
        
