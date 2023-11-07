import os
from pathlib import Path

import click


@click.group()
def cli():
    """
    This is the command line interface (CLI) program for executing the "bake" command.
    """
    pass


# @cli.command()
# @click.argument("mode", type=click.Choice(["readme", "docstrings", "all"]))
# @click.option("--file_path", "-f", default=".", help="The path to a file or directory.")
# def bake(mode, file_path):
#     """
#     Execute the "bake" command.

#     Args:
#         mode (str): The mode to execute, one of "readme", "docstrings", or "all".
#         file_path (str): The path to a file or directory.

#     Returns:
#         None.

#     Raises:
#         None.
#     """
#     if not Path(file_path).is_dir():
#         click.echo("Provided path does not exist.")
#         return
#     try:
#         if mode == "docstrings":
#             generate_docstring(file_path=file_path)
#         elif mode == "readme":
#             generate_readme(file_path=file_path)
#         elif mode == "all":
#             pass
#     except Exception as e:
#         raise e


# def identify_python_src_directory(path="."):
#     # Iterate over every directory in the root
#     for root, dirs, _ in os.walk(path):
#         for dir in dirs:
#             # create a potential src directory and tests directory
#             src_dir = os.path.join(root, dir, "src")
#             tests_dir = os.path.join(root, dir, "tests")

#             # if src and tests directories exist
#             if os.path.isdir(src_dir) and os.path.isdir(tests_dir):
#                 # check for another directory named pkg_name under src directory
#                 if os.path.isdir(os.path.join(src_dir, dir)):
#                     pkg_name_dir = os.path.basename(os.path.join(src_dir, dir))

#                 if pkg_name_dir:
#                     if click.confirm(
#                         f"Did we identify the correct python package at {src_dir}?"
#                     ):
#                         return src_dir, pkg_name_dir
#     return


@cli.command()
# @startup_checks
def server():
    from tropoloco.server import StandaloneApplication, app

    options = {
        "bind": "%s:%s" % ("0.0.0.0", "8080"),
        "workers": 1,
        "worker_class": "uvicorn.workers.UvicornWorker",
    }
    StandaloneApplication(app, options).run()


if __name__ == "__main__":
    cli()
