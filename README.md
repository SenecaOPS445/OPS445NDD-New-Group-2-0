# Winter 2025 Assignment 2

# Assignment 2: Password Generator with Security Checker Tool

## Description
This project is a Python tool that can do two things:
1. Generate a random password.
2. Check the strength of a given password.

It only uses Python's standard library. We use the `argparse` module to read options and arguments from the command line.

## Overview
The project is divided into four files:
- **password_generator.py** – Contains a function that makes a random password.
- **password_checker.py** – Contains a function that checks if a password is strong.
- **argument_parser.py** – Sets up command line options and arguments.
- **assignment2.py** – The main file that ties everything together.

## How the Program Works
- **Input Gathering:**  
  The program reads input from the command line. The user must choose a command:
  - `generate` to create a password.
  - `check` to test a password.
  - Optional flags such as `--verbose` can be added for more detailed output.
  
  For the generate command, the user can set the password length. For the check command, the user must provide a password.

- **Processing Requirements:**  
  - The password generator picks random letters, numbers, and symbols to create a password.
  - The password checker looks for a minimum length, lowercase letters, uppercase letters, digits, and special characters.

- **Output Presentation:**  
  - When generating a password, the new password is printed.
  - When checking a password, a message is printed showing whether the password is strong or what it is missing.

## Command-Line Arguments and Options
- **Subcommands**:
  - `generate` — Generates a random password.
  - `python3 assignment2.py generate`
  - `check` — Checks the security of a given password.
  - `python3 assignment2.py check P@ssw0rd123!`
- **Options for `generate`**:
  - `-l, --length`: Number that sets how long the password should be (default is 12).
  - `python3 assignment2.py generate -l 12`
  -  `python3 assignment2.py generate --length 12`
  - `-v, --verbose`: A flag for showing more details.
  - `python3 assignment2.py generate -l 12 -v`
  - `python3 assignment2.py generate --length 12 --verbose`
- **Options for `check`**:
  - A required argument: the password to check.
  - `-v, --verbose`: A flag for detailed feedback during the check.
  - `python3 assignment2.py check P@ssw0rd123! -v`
  - `python3 assignment2.py check P@ssw0rd123! --verbose`

## Development Challenges
- Setting up the command line arguments correctly.
- Making sure the password checker finds all required elements.
- Testing the code with different passwords.
- Dividing the code into multiple files and then integrating them smoothly using Git and pull requests.

## Timeline and Milestones
- **Planning:** 2 days to plan the work and divide the tasks.
- **Coding:** 5 days for writing and testing each file.
- **Testing:** 1 day to run and check the tool with different inputs.
- **Documentation:** 0.5 day to write this README and add comments.
- **Final Review:** 0.5 day for final checks and submission.

## Group Members
- Regie Francisco
- Sean Daweng
- Prashant K C
- Pujan Shrestha
