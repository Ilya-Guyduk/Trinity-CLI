import argparse



class CLIConfigurator:
	"""docstring for ClassName"""
	def __init__(self):
		pass


	def arguments(self):

	    parser = argparse.ArgumentParser(description="Trinyd Control CLI")
	    parser.add_argument('--host', type=str, default='127.0.0.1', help="Daemon host address")
	    parser.add_argument('--port', type=int, default=5555, help="Daemon port")
	    parser.add_argument('--id', type=str, default='', help="Daemon ID")
	    parser.add_argument('--key', type=str, default='', help="Daemon key")
	    parser.add_argument('--xmlfile', type=str, default='', help="Daemon ID")
	    parser.add_argument('--nohuman', type=bool, default=False, help="Daemon ID")
	    parser.add_argument('--cmd', type=str, default='', help="Daemon ID")


	    return parser.parse_args()