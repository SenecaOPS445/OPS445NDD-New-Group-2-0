#!/usr/bin/env python3
# Student ID: [your_seneca_id] (Group Member 1)

import random   # For generating random characters
import string   # For accessing sets of characters

def generate_password(length):
    """
    Generate a random password of the specified length.
    (Uses ascii letters, digits, and punctuation)
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    # Allowed characters include uppercase/lowercase letters, digits, and punctuation.
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    # Build the password by randomly choosing allowed characters.
    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    return password
