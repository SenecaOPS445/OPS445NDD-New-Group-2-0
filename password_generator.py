#!/usr/bin/env python3
# Student ID: [your_seneca_id] (Group Member 1)

import random   # For random selection
import string   # For character sets

def generate_password(length):
    """
    Generate a random password of the given length.
    Includes letters, digits, and punctuation.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Combine letters, digits, and symbols
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly build the password
    return ''.join(random.choice(allowed_chars) for _ in range(length))

