#Reads the yaml configuration file and installs software based on the configuration.

import os
import yaml

CONFIG_PATH = "config/defaults.yaml"

def parser():
    """Parse the YAML configuration file."""
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found at {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    return config
