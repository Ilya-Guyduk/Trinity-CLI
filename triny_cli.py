import cmd
import json
import xmlrpc.client
from TrinyCliConfigurator import CLIConfigurator
import readline
from rich import box
from rich.console import Console
from rich.table import Table

class Tabulator:
    def __init__(self):
        self.console = Console()

    def print_response_table(self, response):
        try:
            if 'answer' in response:
                answer_data = response['answer']
                if isinstance(answer_data, list) and len(answer_data) > 0 and isinstance(answer_data[0], dict):
                    answer_table = Table(box=box.ROUNDED)
                    for key in answer_data[0].keys():
                        answer_table.add_column(key)
                    for row in answer_data:
                        retcode = row.get('retcode', '')
                        if retcode == 0:
                            row_values = [f'[green]{str(value)}[/green]' for value in row.values()]
                        elif retcode == 1:
                            row_values = [f'[red]{str(value)}[/red]' for value in row.values()]
                        else:
                            row_values = [f'[yellow]{str(value)}[/yellow]' for value in row.values()]
                        answer_table.add_row(*row_values)
                    self.console.print(answer_table)
            if 'data' in response:
                data = response['data']
                if isinstance(data, dict) and len(data) > 0:
                    data_table = Table(box=box.ROUNDED)
                    for key in data.keys():
                        data_table.add_column(key)
                    row_values = [str(value) for value in data.values()]
                    data_table.add_row(*row_values)
                    self.console.print(data_table)
        except json.JSONDecodeError:
            print("Error decoding JSON data")



class CommandLine(cmd.Cmd):
    prompt = f'triny> '

    def __init__(self, daemon_address):
        super().__init__()
        self.daemon_proxy = xmlrpc.client.ServerProxy(daemon_address)
        self.tab = Tabulator()




    def help_node(self):
        args = ""
        try:
            result = self.daemon_proxy.node(*args.split())
            print("Received result:", result)  # Добавим эту строку для отладки
            self.tab.print_response_table(result)
        except Exception as e:
            print(f"Error sending command: {e}")

    def do_node(self, args):
        try:
            result = self.daemon_proxy.node(*args.split())
            print("Received result:", result)  # Добавим эту строку для отладки
            self.tab.print_response_table(result)
        except Exception as e:
            print(f"Error sending command: {e}")

    def do_self(self, args):
        try:
            result = self.daemon_proxy.self_method(*args.split())
            print("Received result:", result)  # Добавим эту строку для отладки
            self.tab.print_response_table(result)
        except Exception as e:
            print(f"Error sending command: {e}")

    
    def help_exit(self):
        print("Pass")

    def do_exit(self, args):
        return True




    def postcmd(self, stop, line):
        readline.write_history_file(configurator.HISTORY_FILE)
        return stop

if __name__ == "__main__":
    configurator = CLIConfigurator()
    args_cli = configurator.arguments()

    daemon_address = f'http://{args_cli.host}:{args_cli.port}'


    readline.read_history_file(configurator.HISTORY_FILE)

    command_line = CommandLine(daemon_address)
    command_line.cmdloop("Welcome to the Trinyd Control CLI. Type 'help' for commands.")
