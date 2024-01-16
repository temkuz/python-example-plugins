from argparse import ArgumentParser

from poc_plugin.types.plugins import CLIUtils
from .functions import show_message


def config_cli(cli_utils: CLIUtils):
    sub = cli_utils.subparser
    echo_parser: ArgumentParser = sub.add_parser('echo', help='echo plugin command')
    echo_parser.set_defaults(func=show_message)
    echo_parser.add_argument('message', help='message for show')


def load_plugin():
    pass
