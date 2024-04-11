# Trinyd Control CLI
The Trinyd Control CLI is a command-line interface (CLI) tool designed to manage the Trinyd daemon through RPC commands. It provides a convenient way to interact with the daemon, allowing users to send various commands and retrieve information about the system.

# Usage
To use the Trinyd Control CLI, follow the instructions below:

**Installation**: Ensure that Python is installed on your system. Clone the repository containing the CLI code.

**Configuration**: Customize the CLI configuration by editing the trinyd_cli_config.ini file. Specify the daemon host address, port, ID, key, and other optional parameters.

**Launching the CLI**: Execute the binary file from the command line or terminal. You can specify additional parameters such as the daemon host address and port.

```
triny_cli
```
**OR**
```
triny_cli --host <host_address> --port <port_number>
```
**Interacting with the CLI**: Once the CLI is launched, you can use various commands to manage the Trinyd daemon. Type help to view available commands and their descriptions.

**Sending Commands**: Use the node command followed by arguments to send a specific command to the Trinyd daemon. For example:

**Exiting the CLI**: To exit the CLI, type **exit** or press **Ctrl + D**.

## Features

**Command-Line Interface**: Provides an intuitive command-line interface for managing the Trinyd daemon.
**RPC Communication**: Communicates with the daemon using XML-RPC, allowing for remote command execution.
**Customization**: Supports customization through command-line arguments and configuration file settings.
**Error Handling**: Includes error handling to gracefully handle exceptions and display error messages.
## Requirements
None (no Python or dependencies required)
## Contributors
Ilya-Guyduk
## License
[License Information]
