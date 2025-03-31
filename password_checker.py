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
