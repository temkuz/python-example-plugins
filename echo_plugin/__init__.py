from argparse import ArgumentParser

from poc_plugin.types.plugins import CLIUtils

from .types import MessageNamespace


def config_cli(cli_utils: CLIUtils):
    sub = cli_utils.subparser
    echo_parser: ArgumentParser = sub.add_parser('echo_parser', help='echo parser')
    echo_parser.set_defaults(func=show_message)
    echo_parser.add_argument('message', help='show message')


def show_message(namespace: MessageNamespace):
    message = namespace.message
    print(message)


def load_plugin():
    pass
