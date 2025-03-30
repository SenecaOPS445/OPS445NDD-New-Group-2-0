#!/usr/bin/env python3
# Student ID: sdaweng

import string   # importing string for punctuation and letter checks

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
