# Handles Homebrew and software installations

import subprocess
import os
import yaml


CONFIG_PATH = "config/defaults.yaml"  # Path to your configuration file


def check_homebrew():
    """Check if Homebrew is installed, and install it if missing."""
    print("Checking for Homebrew...")
    try:
        subprocess.run(["brew", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Homebrew is already installed.")
    except FileNotFoundError:
        print("Homebrew not found. Installing...")
        subprocess.run(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
            shell=True,
            check=True,
        )
        print("Homebrew installed successfully.")


def install_taps(taps):
    """Install Homebrew taps."""
    for tap in taps:
        print(f"Installing tap: {tap}...")
        subprocess.run(["brew", "tap", tap], check=True)



def install_casks(casks):
    """Install Homebrew casks."""
    for cask in casks:
        print(f"Installing cask: {cask}...")
        subprocess.run(["brew", "install", "--cask", cask], check=True)

def install_formulas(formulas):
    """Install Homebrew formulas."""
    for formula in formulas:
        print(f"Installing formula: {formula}...")
        subprocess.run(["brew", "install", formula], check=True)

def parse_config():
    """Parse the YAML configuration file."""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found at {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    return config

def install_software(prefs):
    """Main method to install software based on the configuration file."""
    try:
        check_homebrew()
        config = prefs

        # Install taps
        if "taps" in config.get("homebrew", {}):
            install_taps(config["homebrew"]["taps"])

        # Install formulas
        if "formulas" in config.get("homebrew", {}):
            install_formulas(config["homebrew"]["formulas"])

        # Install casks
        if "casks" in config.get("homebrew", {}):
            install_casks(config["homebrew"]["casks"])

        print("Software installation completed successfully!")
    except Exception as e:
        print(f"Error during installation: {e}")
