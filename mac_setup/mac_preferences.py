# Handles macOS system preference tweaks

import subprocess

def set_preferences(preferences):
    """Set macOS system preferences"""
    print("Setting Finder preferences...")
    finder_preferences = str(preferences["show_hidden_files"])
    subprocess.run(["defaults", "write", "com.apple.finder", "AppleShowAllFiles", "-bool", finder_preferences ], check=True)
    subprocess.run(["killall", "Finder"], check=True)