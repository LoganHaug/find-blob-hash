"""Brute Forces blob hashes based on user inputted string"""
# External Imports
import shlex
import string
import subprocess
# No Internal Imports
ALL_CHARS = [char for char in string.printable]
print(ALL_CHARS)
USER_STRING = input('Enter a string: ')
# Use shlex.split to preserve spaces within quotes and preserve the quotes
COMMAND = shlex.split("command", posix=False)
OUTPUT = subprocess.run(COMMAND, check=True, stdout=subprocess.PIPE).stdout
# output is a byte-like string and needs to be decoded
# Remove trailing newlines and replace UNIX formatted newlines
OUTPUT = output.decode('utf-8').rstrip('\n').replace('\r\n', '\n')
