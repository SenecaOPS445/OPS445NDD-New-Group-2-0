#!/usr/bin/env python3
# Student ID: rfrancisco6
"""
Assignment 2: Password Generator with Security Checker Tool
This script integrates the functionalities from our group.
"""

import sys      # For exit function and error codes

# Import functions from our group members' modules
# Member 1's module
# Member 2's module
# Member 3's module

def main():
    # Get arguments
    args = parse_arguments()    # Get user entered
    
    if args.command == "generate":  # Generate password
        if args.length < 1:     # Make sure length is valid
            print("Error: password length must be at least 1.")
            sys.exit(1)     # Exit if error

        pwd = generate_password(args.length)    # Create password

        print("Generated password:", pwd)   # Show the password

    elif args.command == "check":   # Check password
        result = check_password(args.password, verbose=args.verbose)   # Check it
        print(result)   # Show results of the check

if __name__ == "__main__":
    main()  # Run