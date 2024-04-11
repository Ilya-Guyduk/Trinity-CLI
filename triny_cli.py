import cmd
import json
import xmlrpc.client
import argparse
import configparser
from TrinyCliConfigurator import CLIConfigurator
import readline
import os
import tabulate
from termcolor import colored

CLI_ID="1"

HISTORY_FILE = os.path.expanduser("~/.triny_cli_history")

class CommandLine(cmd.Cmd):
    prompt = f'triny> '

    def __init__(self, daemon_address):
        super().__init__()
        self.daemon_proxy = xmlrpc.client.ServerProxy(daemon_address)




    def do_node(self, args):
        try:
            result = self.daemon_proxy.node(*args.split())
            if isinstance(result, list) and all(isinstance(item, dict) for item in result):
                headers = [colored(header, 'cyan') for header in result[0].keys()]
                rows = [[colored(str(value), 'yellow') for value in row.values()] for row in result]
                print(tabulate.tabulate(rows, headers=headers))
            else:
                print(result)
        except Exception as e:
            print(f"Error sending command: {e}")

    def help_node(self):

        print("Usage: node <arguments>")
        print("Send a command to the Trinyd daemon.")
        print("Arguments:")
        print("  <arguments>: The arguments to be passed to the node command.")
        print("Example: node start")


    def do_exit(self, args):
        return True

    def postcmd(self, stop, line):
        readline.write_history_file(HISTORY_FILE)
        return stop

if __name__ == "__main__":
    configurator = CLIConfigurator()
    args_cli = configurator.arguments()

    daemon_address = f'http://{args_cli.host}:{args_cli.port}'

    # Проверяем, существует ли файл истории, и если нет, создаем его
    if not os.path.exists(HISTORY_FILE):
        open(HISTORY_FILE, 'a').close()

    readline.read_history_file(HISTORY_FILE)

    command_line = CommandLine(daemon_address)
    command_line.cmdloop("Welcome to the Trinyd Control CLI. Type 'help' for commands.")
