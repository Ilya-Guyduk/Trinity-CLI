import cmd
import json
import xmlrpc.client
from TrinyCliConfigurator import CLIConfigurator
import readline
import tabulate
from termcolor import colored



class Tabulator:
    """docstring for Tabulator"""
    def __init__(self):
        pass

    def print_response_table(self, response):
        try:
            # Первая таблица
            if 'answer' in response:
                data = response['answer']
                if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                    retcode = data[0].get('retcode', '')
                    if retcode == 0:
                        retcode_colored = colored(retcode, 'green')
                        desc_colored = colored(data[0].get('desc', ''), 'green')
                    elif retcode == 1:
                        retcode_colored = colored(retcode, 'red')
                        desc_colored = colored(data[0].get('desc', ''), 'red')
                    else:
                        retcode_colored = colored(retcode, 'yellow')
                        desc_colored = colored(data[0].get('desc', ''), 'yellow')

                    data[0]['retcode'] = retcode_colored
                    data[0]['desc'] = desc_colored
                    answer_table = tabulate.tabulate(data, headers="keys", tablefmt="pipe", stralign='center')
                    print(answer_table)
                    print(colored("\n==========ANSWER=======================================================================", 'yellow'))

            # Вторая таблица
            if 'data' in response:
                data = response['data']
                if data is not None and isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                    data_table = tabulate.tabulate(data, headers="keys", tablefmt="grid", stralign='center')
                    print(data_table)
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
            #print("Received result:", result)  # Добавим эту строку для отладки
            self.tab.print_response_table(result)
        except Exception as e:
            print(f"Error sending command: {e}")

    def do_node(self, args):
        try:
            result = self.daemon_proxy.node(*args.split())
            #print("Received result:", result)  # Добавим эту строку для отладки
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
