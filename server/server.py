import sys
import click

@click.group()
def cli():
    pass


@cli.command()
@click.option("--port", required=False, type=click.INT, default=5000)
def server(port):
    print(f"Hello {port}")


if __name__ == "__main__":
    sys.exit(cli())
