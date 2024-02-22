#!/usr/bin/env python3

import os

# Set the environment variables
os.environ["FIRST_NAME"] = input('What is your first name? ')
os.environ["MIDDLE_NAME"] = input('What is your middle name? ')
os.environ["LAST_NAME"] = input('What is your last name? ')

# Fetch all of the environment variables
FIRST_NAME_ENV = os.getenv("FIRST_NAME")
MIDDLE_NAME_ENV = os.getenv("MIDDLE_NAME")
LAST_NAME_ENV = os.getenv("LAST_NAME")

# Print the environment variables
print(FIRST_NAME_ENV)
print(MIDDLE_NAME_ENV)
print(LAST_NAME_ENV)

