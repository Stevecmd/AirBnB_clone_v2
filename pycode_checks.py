#!/usr/bin/python3
<<<<<<< HEAD
"""
Module to run pycodestyle checks on specified directories and files.
"""

import subprocess

def run_pycodestyle_checks():
    """
    Run pycodestyle checks on specified directories and files.
    """
    # Define the commands to run
    commands = [
        "pycodestyle models/*.py",
        "pycodestyle models/engine/*.py",
        "pycodestyle tests/*.py",
        "pycodestyle tests/test_models/*.py",
        "pycodestyle web_flask/*.py"
    ]

    # Execute each command
    for command in commands:
        print(f"Running: {command}")
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        # Print the output and errors, if any
        if stdout:
            print(stdout.decode('utf-8'))
        if stderr:
            print(stderr.decode('utf-8'))

    print("All checks completed.")

if __name__ == "__main__":
    run_pycodestyle_checks()
=======
import subprocess

# Define the commands to run
commands = [
    "pycodestyle models/*.py",
    "pycodestyle models/engine/*.py",
    "pycodestyle tests/*.py",
    "pycodestyle tests/test_models/*.py",
    "pycodestyle web_flask/*.py"
]

# Execute each command
for command in commands:
    print(f"Running: {command}")
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    # Print the output and errors, if any
    if stdout:
        print(stdout.decode('utf-8'))
    if stderr:
        print(stderr.decode('utf-8'))

print("All checks completed.")
>>>>>>> origin/master
