#!/usr/bin/env python3
# Student ID: [your_seneca_id] (Group Member 3)

import argparse

def parse_arguments():
    """
    Parse command line arguments using argparse.
    Returns the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Password Generator with Security Checker Tool"     # Describe what the program does
    )
    # Create subparsers for different commands: generate and check.
    subparsers = parser.add_subparsers(dest="command", required=True,   # User choose a command
                                       help="Subcommands: 'generate' to create a password, 'check' to validate one")
    
    # Subparser for generating a password.
    parser_generate = subparsers.add_parser("generate", help="Generate a random password")  # Create generate command
    parser_generate.add_argument("-l", "--length", type=int, default=12,    # Add length option
                                 help="Length of the password (default is 12)")
    parser_generate.add_argument("-v", "--verbose", action="store_true",    # Add verbose option
                                 help="Print detailed output about the generation process")
    
    # Subparser for checking a password.
    parser_check = subparsers.add_parser("check", help="Check the security of a password")  # Create check command
    parser_check.add_argument("password", type=str, help="The password to check")   # Password is required
    parser_check.add_argument("-v", "--verbose", action="store_true",   # Add verbose option
                              help="Print detailed output about the security check")
    
    return parser.parse_args()  # Process the command-line arguments and return them
