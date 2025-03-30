#!/usr/bin/env python3
# Student ID: [your_seneca_id]
"""
Assignment 2: Password Generator with Security Checker Tool
This script can either generate a random password or check the security of a given password.
It uses argparse for command-line handling.
"""

import argparse      # For handling command-line options and arguments
import random        # For generating random selections
import string        # For lists of characters (letters, digits, punctuation)
import sys           # For system exit and error handling

def generate_password(length):
    """
    Generate a random password of the specified length.
    (Uses ascii letters, digits, and punctuation)
    """
    # Validate that the length is at least 1.
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    # Allowed characters: letters, digits, punctuation.
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters.
    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    return password

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
    issues = []
    # Check for minimum length.
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long.")
    # Check for lowercase letters.
    if not any(c.islower() for c in password):
        issues.append("Password must include at least one lowercase letter.")
    # Check for uppercase letters.
    if not any(c.isupper() for c in password):
        issues.append("Password must include at least one uppercase letter.")
    # Check for digits.
    if not any(c.isdigit() for c in password):
        issues.append("Password must include at least one digit.")
    # Check for special characters.
    if not any(c in string.punctuation for c in password):
        issues.append("Password must include at least one special character.")
    
    # If verbose flag is set, print detailed analysis.
    if verbose:
        print("Password analysis:")
        print("Length:", len(password))
        print("Contains lowercase:", any(c.islower() for c in password))
        print("Contains uppercase:", any(c.isupper() for c in password))
        print("Contains digit:", any(c.isdigit() for c in password))
        print("Contains special character:", any(c in string.punctuation for c in password))
    
    # Return the security status.
    if issues:
        return "Weak password. Issues:\n" + "\n".join(issues)
    else:
        return "Strong password."

def parse_arguments():
    """
    Parse command line arguments using argparse.
    Returns the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Password Generator with Security Checker Tool"
    )
    # Create subparsers for different commands.
    subparsers = parser.add_subparsers(dest="command", required=True,
                                       help="Subcommands: 'generate' to create a password, 'check' to validate one")
    
    # Subparser for generating a password.
    parser_generate = subparsers.add_parser("generate", help="Generate a random password")
    parser_generate.add_argument("-l", "--length", type=int, default=12,
                                 help="Length of the password (default is 12)")
    parser_generate.add_argument("-v", "--verbose", action="store_true",
                                 help="Print detailed output about the generation process")
    
    # Subparser for checking a password.
    parser_check = subparsers.add_parser("check", help="Check the security of a password")
    parser_check.add_argument("password", type=str, help="The password to check")
    parser_check.add_argument("-v", "--verbose", action="store_true",
                              help="Print detailed output about the security check")
    
    return parser.parse_args()

def main():
    # Parse command-line arguments.
    args = parse_arguments()
    
    # Execute the command based on the provided subcommand.
    if args.command == "generate":
        # Validate the length before generation.
        if args.length < 1:
            print("Error: password length must be at least 1.")
            sys.exit(1)
        pwd = generate_password(args.length)
        # If verbose, print additional details.
        if args.verbose:
            print("Generated password details:")
            print("Allowed characters include letters, digits, and punctuation.")
        print("Generated password:", pwd)
    elif args.command == "check":
        # Check the security of the provided password.
        result = check_password(args.password, verbose=args.verbose)
        print(result)

if __name__ == "__main__":
    main()
