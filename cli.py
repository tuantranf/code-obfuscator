import click
from code_obfuscator.cythonizer import Cythonizer


@click.command()
@click.argument('path')
def execute(path: str):
    Cythonizer().execute(path)


if __name__ == '__main__':
    execute()
