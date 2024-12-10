# Project documentation
## Overview

This project automates the setup of your macOS environment, including software installation, Dock customization, and system preferences tweaks.

## Features

- **Full Setup**: Run the complete setup process using a specified configuration file.
- **Software Installation**: Install software based on a YAML configuration file.
- **Dock Customization**: Customize the macOS Dock.
- **System Preferences**: Apply macOS system preferences from a configuration file.

## Commands

### `setup`

Run the full setup process using the specified configuration file.

```sh
python mac_setup/cli.py setup --config path/to/config.yaml
```

### `install`

Install software from the configuration file.

```sh
python mac_setup/cli.py install --config path/to/config.yaml
```

### `dock`

Customize the macOS Dock.

```sh
python mac_setup/cli.py dock
```

### `preferences`

Set macOS system preferences.

```sh
python mac_setup/cli.py preferences --config path/to/config.yaml
```

## Configuration

The configuration files are in YAML format and include settings for software installation, Dock customization, and system preferences.

## Usage

1. Clone the repository.
2. Install the required dependencies.
3. Run the desired command with the appropriate configuration file.

## License

This project is licensed under the MIT License.