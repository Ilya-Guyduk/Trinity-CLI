import argparse
import configparser
import os


class CLIConfigurator:
	"""docstring for ClassName"""
	def __init__(self):
		self.HISTORY_FILE = os.path.expanduser("~/.triny_cli_history")
		self.config = configparser.ConfigParser()
		self.configure_ini_file("./triny_cli.ini")


	def arguments(self):
	    parser = argparse.ArgumentParser(description="Trinyd Control CLI")

	    parser.add_argument('--host', 
	    					type=str, 
	    					default=f"{self.config.get('TRINY_CLI', 'host')}", 
	    					help=f"Daemon host address. Default is '{self.config.get('TRINY_CLI', 'host')}'.")

	    parser.add_argument('--port', 
	    					type=int, 
	    					default=f"{self.config.get('TRINY_CLI', 'port')}", 
	    					help=f"Daemon port. Default is {self.config.get('TRINY_CLI', 'port')}.")

	    parser.add_argument('--id', type=str, default='', help="Daemon ID. Default is an empty string.")
	    parser.add_argument('--key', type=str, default='', help="Daemon key. Default is an empty string.")
	    parser.add_argument('--xmlfile', type=str, default='', help="Path to an XML file. Default is an empty string.")
	    parser.add_argument('--nohuman', type=bool, default=False, help="Flag to enable non-human readable output. Default is False.")
	    parser.add_argument('--cmd', type=str, default='', help="Command to be executed. Default is an empty string.")

	    return parser.parse_args()



	    return parser.parse_args()

	def configure_ini_file(self, ini_file_path):
		# Проверяем, существует ли файл истории, и если нет, создаем его
	    if not os.path.exists(self.HISTORY_FILE):
	        open(self.HISTORY_FILE, 'a').close()
	    

	    # Create default values for the configuration
	    self.config['TRINY_CLI'] = {
	        'host': '127.0.0.1',
	        'port': '5555',
	        'id': '',
	        'key': '',
	        'xmlfile': '',
	        'nohuman': 'False',
	        'cmd': ''
	    }

	    # Check if the INI file already exists
	    if not os.path.exists(ini_file_path):
	        # Create the INI file with default values
	        with open(ini_file_path, 'w') as configfile:
	            self.config.write(configfile)
	    self.config.read(ini_file_path)

