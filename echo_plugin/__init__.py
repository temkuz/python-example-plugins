from poc_plugin.variables.cli import CLI_SUBPARSER
from .functions import show_message


def config_cli():
    echo_parser = CLI_SUBPARSER.add_parser('echo', help='echo plugin command')
    echo_parser.set_defaults(func=show_message)
    echo_parser.add_argument('message', help='message for show')


def load_plugin():
    config_cli()
