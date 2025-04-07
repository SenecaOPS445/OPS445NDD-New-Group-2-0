#!/usr/bin/env python3
# Student ID: pshrestha

import argparse

def parse_arguments():
    """
    Parse command line arguments using argparse.
    """
    parser = argparse.ArgumentParser(
        description="Password Generator and Security Checker"
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True,
        help="Subcommands: 'generate' or 'check'"
    )

    # 'generate' subcommand
    parser_generate = subparsers.add_parser("generate", help="Generate a random password")
    parser_generate.add_argument("-l", "--length", type=int, default=12,
                                 help="Password length (default: 12)")
    parser_generate.add_argument("-v", "--verbose", action="store_true",
                                 help="Show detailed output")

    # 'check' subcommand
    parser_check = subparsers.add_parser("check", help="Check password strength")
    parser_check.add_argument("password", type=str,
                              help="Password to check")
    parser_check.add_argument("-v", "--verbose", action="store_true",
                              help="Show detailed output")

    return parser.parse_args()
