import click
from mac_setup import read_config, installer, dock, mac_preferences

@click.group()
def cli():
    """
    Mac Setup Automation Tool
    
    Automate the setup of your macOS environment, including software installation,
    Dock customization, and system preferences tweaks.
    """
    pass

@cli.command()
@click.option("--config", default="config/default_config.yaml", show_default=True,
              help="Path to the YAML configuration file.")
def setup(config):
    """
    Run the full setup process using the specified configuration file.
    """
    click.echo("Starting the full Mac setup process...")
    installer.CONFIG_PATH = config  # Set the configuration path dynamically
    installer.install_software()
    dock.customize_dock()
    mac_preferences.set_preferences()
    click.echo("Mac setup completed successfully!")

@cli.command()
@click.option("--config", default="config/defaults.yaml", show_default=True,
              help="Path to the YAML configuration file.")
def install(config):
    """
    Install software from the configuration file.
    """
    click.echo("Installing software from the configuration...")
    read_config.CONFIG_PATH = config
    prefs = read_config.parser()
    installer.CONFIG_PATH = config
    installer.install_software(prefs)

@cli.command()
def dock():
    """
    Customize the macOS Dock.
    """
    click.echo("Customizing the macOS Dock...")
    dock.customize_dock()

@cli.command()
@click.option("--config", default="config/defaults.yaml", show_default=True,
              help="Path to the YAML configuration file.")
def preferences(config):
    """
    Set macOS system preferences.
    """    
    read_config.CONFIG_PATH = config
    prefs = read_config.parser()["preferences"]
    click.echo("Applying macOS system preferences...")
    mac_preferences.set_preferences(prefs)


if __name__ == "__main__":
    cli()
