# Manages Dock customization
import subprocess

def customize_dock():
    """Customize the macOS Dock"""
    print("Customizing the Dock...")
    # Example: Remove all default icons
    subprocess.run(["defaults", "write", "com.apple.dock", "persistent-apps", "-array"], check=True)
    subprocess.run(["killall", "Dock"], check=True)