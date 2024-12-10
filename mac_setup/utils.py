# Utility functions (e.g., for running shell commands)

import subprocess

def run_command(command):
    """Utility to run shell commands"""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")