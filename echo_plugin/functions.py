from .types import MessageNamespace


def show_message(namespace: MessageNamespace):
    message = namespace.message
    print(message)
